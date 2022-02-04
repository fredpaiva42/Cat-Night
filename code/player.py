import pygame
from support import import_folder
from arrow import Arrow
from fireball import Fireball
from settings import screen_width


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, surface, current_character, create_jump_particles, change_health, bar_health_reset, cur_health):
        super().__init__()
        self.current_character = current_character
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft=pos)
        self.player_sprite = pygame.sprite.GroupSingle()
        self.gameClock = pygame.time.Clock()


        # dust particles
        self.import_dust_run_particles()
        self.dust_frame_index = 0
        self.dust_animation_speed = 0.15
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        # Arrow setup
        self.ready = True
        self.arrow_time = 0
        self.arrow_cooldown = 2000
        self.arrows = pygame.sprite.Group()

        self.fire_cooldown = 2000


        # player movement
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -18
        self.collision_rect = pygame.Rect(self.rect.topleft, (55, self.rect.height))  # depois preciso padronizar
        self.attack_collision_rect = pygame.Rect(self.rect.left - 60, self.rect.top, self.rect.width + 120, self.rect.height)
        self.attackCd = 0
        self.pressedQ = False
        self.pressedW = False
        # todos os sprites dos gatos com o mesmo tamanho, ai vai ficar perfeito (mudar o 50)

        # player status
        self.status = 'idle'
        self.facing_right = True
        self.attack = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        # health management
        self.change_health = change_health
        self.bar_health_reset = bar_health_reset
        self.cur_health = cur_health
        self.invincible = False
        self.invincibility_duration = 1000
        self.hurt_time = 0

    def import_character_assets(self):
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': [], 'attack': [], 'attack2': [], 'damage': [],
                           'death': []}
        if self.current_character == 0:
            character_path = '../img/character/king/'

            for animation in self.animations.keys():
                full_path = character_path + animation
                self.animations[animation] = import_folder(full_path)

        if self.current_character == 1:
            character_path = '../img/character/knight/'

            for animation in self.animations.keys():
                full_path = character_path + animation
                self.animations[animation] = import_folder(full_path)

        if self.current_character == 2:
            character_path = '../img/character/meowolas/'

            for animation in self.animations.keys():
                full_path = character_path + animation
                self.animations[animation] = import_folder(full_path)

        if self.current_character == 3:
            character_path = '../img/character/mage/'

            for animation in self.animations.keys():
                full_path = character_path + animation
                self.animations[animation] = import_folder(full_path)

    def import_dust_run_particles(self):
        self.dust_run_particles = import_folder('../img/character/dust_particles/run')

    def animate(self):
        if self.invincible:
            self.status = 'damage'

        animation = self.animations[self.status]

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
            self.rect.bottomleft = self.collision_rect.bottomleft
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
            self.rect.bottomright = self.collision_rect.bottomright

        self.rect = self.image.get_rect(midbottom=self.rect.midbottom)

    def run_dust_animation(self):
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.dust_animation_speed
            if self.dust_frame_index >= len(self.dust_run_particles):
                self.dust_frame_index = 0

            dust_particle = self.dust_run_particles[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(6, 10)
                self.display_surface.blit(dust_particle, pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(6, 10)
                flipped_dust_particle = pygame.transform.flip(dust_particle, True, False)
                self.display_surface.blit(flipped_dust_particle, pos)

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
            self.attack = False
            self.attackCd += self.gameClock.tick(60) / 1000
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
            self.attack = False
            self.attackCd += self.gameClock.tick(60) / 1000
        elif keys[pygame.K_q]:
            self.pressedQ = True
            self.attack = True
            self.attackCd = 0

        elif keys[pygame.K_w]:
            self.pressedW = True
            self.attack = True
            self.attackCd = 0
            if self.current_character == 2 and self.ready:
                if self.facing_right:
                    self.shoot_arrow(self.speed, '../img/character/meowolas/arrow/right/')
                else:
                    self.shoot_arrow(-self.speed, '../img/character/meowolas/arrow/left/')
                self.ready = False
                self.arrow_time = pygame.time.get_ticks()

            if self.current_character == 3 and self.ready:
                if self.facing_right:
                    self.shoot_fire(self.speed)
                else:
                    self.shoot_fire(-self.speed)
                self.ready = False
                self.arrow_time = pygame.time.get_ticks()
        else:
            self.direction.x = 0
            self.pressedW = False
            self.pressedQ = False
            self.attackCd += self.gameClock.tick(60) / 1000
        if keys[pygame.K_UP] and self.on_ground:
            self.attack = False
            self.jump()



    def get_status(self):
        if self.direction.y < 0:
            self.status = 'jump'
        elif self.direction.y > 1:
            self.status = 'fall'
        else:
            if self.direction.x == 1 or self.direction.x == -1:
                self.status = 'run'
            elif self.pressedQ:
                self.status = 'attack'
            elif self.pressedW:
                self.status = 'attack2'
            else:
                self.status = 'idle'

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.collision_rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def get_damage(self, damage):
        if not self.invincible:
            self.change_health(damage)
            self.invincible = True
            self.attack = False
            self.hurt_time = pygame.time.get_ticks()

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False


    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if self.current_character == 2:
                if current_time - self.arrow_time >= self.arrow_cooldown:
                    self.ready = True
            else:
                if current_time - self.arrow_time >= self.fire_cooldown:
                    self.ready = True

    def shoot_arrow(self, speed, path):
        self.arrows.add(Arrow(self.rect.center, speed, self.rect.x, path))

    def shoot_fire(self, speed):
        self.arrows.add(Fireball(self.rect.center, speed, self.rect.x))

    def update(self):
        self.get_input()
        self.get_status()
        self.animate()
        self.run_dust_animation()
        self.recharge()
        self.arrows.update()
        self.invincibility_timer()
