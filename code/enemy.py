import pygame
from tiles import AnimatedTile
from random import randint
from grenade import Grenade


class Enemy(AnimatedTile):
    def __init__(self, size, x, y, path ,type):
        super().__init__(size, x, y, path)
        self.alive = True
        self.frame_index = 0
        self.animation_speed = 0.5
        if type == 'run':
            self.rect.y += size - self.image.get_size()[1]
        self.speed = randint(3, 5)

    def move(self):
        self.rect.x += self.speed

    def reverse_image(self):
        if self.speed < 0:
            self.image = pygame.transform.flip(self.image, True, False)

    def reverse(self):
        self.speed *= -1

    def update(self, shift):
        if self.alive:
            self.rect.x -= shift
        self.animate()
        if self.alive:
            self.move()
        self.reverse_image()

class Boss(Enemy):
    def __init__(self, size, x, y, path ,type, musicManager):
        super().__init__(size, x, y, path, type)
        self.total_hp = 120 #150
        self.hp = 120
        self.speed = 2
        self.musicManager = musicManager

        # attack setup
        self.minimal_cd = 7000
        self.maximal_cd = 10000
        self.ready = True
        self.grenade_time = 0
        self.grenade_cooldown = randint(self.minimal_cd, self.maximal_cd)
        self.grenades = pygame.sprite.Group()
        self.grenade_speed = 7

        self.invincible = False
        self.invincibility_duration = 400
        self.hurt_time = 0
        self.rage = False

        # health bar
        self.health_bar = pygame.image.load("../ui/boss_stats.png").convert_alpha()
        self.bar_max_width = 298
        self.bar_height = 8

    def show_boss_health(self, display_surface):
        display_surface.blit(self.health_bar, (435, 45))
        current_health_ratio = self.hp / self.total_hp
        current_bar_width = self.bar_max_width * current_health_ratio
        pygame.draw.rect(display_surface, '#FF0044', (544,117,int(current_bar_width),9))

        if not self.rage:
            if current_health_ratio <= 1/3:
                self.rage = True
                self.minimal_cd = 1000
                self.maximal_cd = 5000
                self.musicManager.loadMusic("rage", 0.1)
                if self.speed > 0:
                    self.speed += 2
                else:
                    self.speed -= 2

    def attack(self):
        if self.speed > 0:
            self.grenades.add(Grenade(self.rect.center, self.grenade_speed, self.rect.x))
            if self.rage:
                self.grenades.add(Grenade(self.rect.center, -self.grenade_speed, self.rect.x))
        else:
            self.grenades.add(Grenade(self.rect.center, -self.grenade_speed, self.rect.x))
            if self.rage:
                self.grenades.add(Grenade(self.rect.center, self.grenade_speed, self.rect.x))
        self.ready = False
        self.grenade_time = pygame.time.get_ticks()

    def recharge(self):
        if not self.ready:
            current_time = pygame.time.get_ticks()
            if current_time - self.grenade_time >= self.grenade_cooldown:
                self.ready = True

    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False

    def update_attack_cd(self):
        self.minimal_cd -= 5
        self.minimal_cd += 5
        self.grenade_cooldown = randint(min(3000, self.minimal_cd), min(5000, self.maximal_cd))

    def run(self):
        if self.ready:
            self.attack()
        self.recharge()
        self.update_attack_cd()
        self.grenades.update()
        self.invincibility_timer()