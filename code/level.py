import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width, SOUND
from tiles import Tile, StaticTile
from player import Player
from decoration import Water
from enemy import Enemy
from enemy import Boss
from game_data import characters
from particles import ParticleEffect


class Level:
    def __init__(self, current_character, surface, musicManager, create_selection, change_health, bar_health_reset,
                 cur_health):
        # configuração geral
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None
        self.create_selection = create_selection
        self.change_health = change_health
        self.bar_health_reset = bar_health_reset
        self.cur_health = cur_health
        self.clock = pygame.time.Clock()
        self.musicManager = musicManager

        # selection connection
        self.create_selection = create_selection
        self.current_character = current_character
        level_data = characters[self.current_character]
        self.new_max_character = level_data['unlock']

        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player_sprite = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout, change_health, bar_health_reset, cur_health)
        self.player_damage = 10

        # boss
        boss_layout = import_csv_layout(level_data['boss'])
        self.boss_sprite = pygame.sprite.GroupSingle()
        self.boss_setup(boss_layout)
        self.is_final_fight = False

        # item
        self.item_id = 0
        self.got_item = False
        self.qtd_items_collected = 0

        # dust
        self.dust_sprite = pygame.sprite.GroupSingle()
        self.player_on_ground = False

        # rat death
        self.rat_death_sprite = pygame.sprite.Group()
        self.cat_death_sprite = pygame.sprite.Group()
        self.alive = True

        # boss death
        self.boss_death_sprite = pygame.sprite.Group()
        self.boss_death = False

        # CENA 1

        self.grupos_sprites_cenario = []
        nomes_sprites_cenario = ['estrelas', 'nuvens', 'predios', 'parede_subsolo', 'subsolo', 'floresta',
                                 'subsolo_emcima', 'ponte', 'hotel', 'predio_4', 'extra_predio4', 'casa_1', 'casa_3',
                                 'grades_extra', 'perfume','grades_cima', 'arvore', 'casa2_fachada', 'casa2_fundos',
                                 'pizzaria', 'telhados_fundos', 'predio_alto', 'telhados', 'grades_casa2', 'jardim_casa3',
                                 'extra_casa3', 'anel', 'capuz', 'portas_janelas', 'sombras', 'pergaminho', 'colar',
                                 'tapumes', 'arbustos_casa1', 'carro', 'cercas', 'colher', 'jardim_casa1']

        self.vegetation_sprites_names = ['arvore', 'arbustos_casa1', 'jardim_casa1', 'jardim_casa3', 'floresta']
        self.all_tiles_sprites_names = ['estrelas', 'nuvens', 'predios', 'parede_subsolo', 'subsolo', 'subsolo_emcima',
                                        'ponte', 'hotel', 'predio_4', 'extra_predio4', 'casa_1', 'casa_3', 'grades_extra',
                                        'grades_cima', 'casa2_fachada', 'casa2_fundos', 'pizzaria',
                                        'telhados_fundos', 'predio_alto', 'telhados', 'grades_casa2', 'extra_casa3',
                                        'portas_janelas', 'sombras', 'tapumes', 'carro', 'cercas']
        self.items_sprites_names = ['perfume', 'anel', 'capuz', 'colar', 'colher', 'pergaminho']

        # criação dos grupos de sprites
        for nome in nomes_sprites_cenario:
            layout = import_csv_layout(level_data[nome])
            if nome == 'colher':
                self.colher_sprites = self.colher_sprites = self.create_tile_group(layout, nome)
                grupo_sprite = self.colher_sprites
            elif nome == 'pergaminho':
                self.pergaminho_sprites = self.create_tile_group(layout, nome)
                grupo_sprite = self.pergaminho_sprites
            elif nome == 'colar':
                self.colar_sprites = self.create_tile_group(layout, nome)
                grupo_sprite = self.colar_sprites
            elif nome == 'perfume':
                self.perfume_sprites = self.create_tile_group(layout, nome)
                grupo_sprite = self.perfume_sprites
            elif nome == 'capuz':
                self.capuz_sprites = self.create_tile_group(layout, nome)
                grupo_sprite = self.capuz_sprites
            elif nome == 'anel':
                self.anel_sprites = self.create_tile_group(layout, nome)
                grupo_sprite = self.anel_sprites
            else:
                grupo_sprite = self.create_tile_group(layout, nome)
            self.grupos_sprites_cenario.append(grupo_sprite)

        # CONFIGURAÇÃO DOS SPRITES QUE TEM USO EXCLUSIVO
        # chão
        chao_layout = import_csv_layout(level_data['chao'])
        self.chao_sprite = self.create_tile_group(chao_layout, 'chao')  # isso garante que estamos pegando o arquivo
        # certo, pois todos começam com id 0

        # escada
        escada_layout = import_csv_layout(level_data['escada'])
        self.escada_sprites = self.create_tile_group(escada_layout, 'escada')

        # chao_floresta
        chao_floresta_layout = import_csv_layout(level_data['chao_floresta'])
        self.chao_floresta_sprites = self.create_tile_group(chao_floresta_layout, 'chao_floresta')

        # enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # constraints
        constraints_layout = import_csv_layout(level_data['constraints'])
        self.constraints_sprites = self.create_tile_group(constraints_layout, 'constraints')

        # chave
        chave_layout = import_csv_layout(level_data['chave'])
        self.chave_sprites = self.create_tile_group(chave_layout, 'chave')

        self.items_dict = {
            self.colher_sprites: 1,
            self.pergaminho_sprites: 2,
            self.colar_sprites: 3,
            self.perfume_sprites: 4,
            self.capuz_sprites: 5,
            self.anel_sprites: 6,
        }

        # decoration
        level_width = (len(chao_layout[0]) - 77.5) * tile_size
        self.water = Water(screen_height - 35, level_width)

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        tile_list_all = import_cut_graphics('../img/background/mp_cs_tilemap_all 1.png')
        tile_list_vegetation = import_cut_graphics('../img/background/mp_cs_vegetation 1.png')
        tile_list_items = import_cut_graphics('../img/background/items_tiles.png')

        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                if val != '-1':
                    x = col_index * tile_size
                    y = row_index * tile_size

                    for name in self.all_tiles_sprites_names:
                        if type == name:
                            tile_surface = tile_list_all[int(val)]
                            sprite = StaticTile(tile_size, x, y, tile_surface)
                            sprite_group.add(sprite)
                            break

                    for name in self.vegetation_sprites_names:
                        if type == name:
                            tile_surface = tile_list_vegetation[int(val)]
                            sprite = StaticTile(tile_size, x, y, tile_surface)
                            sprite_group.add(sprite)
                            break

                    for name in self.items_sprites_names:
                        if type == name:
                            tile_surface = tile_list_items[int(val)]
                            sprite = StaticTile(tile_size, x, y, tile_surface)
                            sprite_group.add(sprite)
                            break

                    if type == 'chao':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    elif type == 'escada':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    elif type == 'chao_floresta':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    elif type == 'enemies':
                        sprite = Enemy(tile_size, x, y, '../img/enemies/rat/run', 'run')
                        sprite_group.add(sprite)

                    elif type == 'constraints':
                        sprite = Tile(tile_size, x, y)
                        sprite_group.add(sprite)

                    elif type == 'chave':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout, change_health, bar_health_reset, cur_health):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface, self.current_character, self.create_jump_particles,
                                    change_health, bar_health_reset, cur_health)
                    self.player_sprite.add(sprite)

    def boss_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Boss(tile_size, x, y, '../img/enemies/dog/run', 'run', self.musicManager)
                    self.boss_sprite.add(sprite)

    def rat_collision_reverse(self):
        for enemy in self.enemy_sprites.sprites():
            if pygame.sprite.spritecollide(enemy, self.constraints_sprites, False):
                enemy.reverse()

    def boss_collision_reverse(self):
        boss = self.boss_sprite.sprite
        if pygame.sprite.spritecollide(boss, self.constraints_sprites, False):
            boss.reverse()

    def create_jump_particles(self, pos):
        if self.player.sprite.facing_right:
            pos -= pygame.math.Vector2(10, 5)
        else:
            pos += pygame.math.Vector2(10, -5)
        jump_particle_sprite = ParticleEffect(pos, 'jump')
        self.dust_sprite.add(jump_particle_sprite)

    def horizontal_movement_collision(self):
        player = self.player_sprite.sprite
        player.collision_rect.x += player.direction.x * player.speed
        collidable_sprites = self.chao_sprite.sprites() + self.escada_sprites.sprites() + self.chao_floresta_sprites.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.collision_rect):
                if player.direction.x < 0:
                    player.collision_rect.left = sprite.rect.right
                    player.on_left = True
                elif player.direction.x > 0:
                    player.collision_rect.right = sprite.rect.left
                    player.on_right = True

    def vertical_movement_collision(self):
        player = self.player_sprite.sprite
        player.apply_gravity()
        collidable_sprites = self.chao_sprite.sprites() + self.escada_sprites.sprites() + self.chao_floresta_sprites.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.collision_rect):
                if player.direction.y > 0:
                    player.collision_rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.collision_rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True
                if not self.is_final_fight:
                    if sprite in self.chao_floresta_sprites.sprites():
                        self.is_final_fight = True
                        if SOUND:
                            self.musicManager.loadMusic("boss_fight", 0.1)
                        player.cur_health = 100

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False

    def scroll_x(self):
        player = self.player_sprite.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = -6
            player.speed = 0
        elif player_x > screen_width - (screen_width / 3) and direction_x > 0:
            self.world_shift = + 6
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def get_player_on_ground(self):
        if self.player_sprite.sprite.on_ground:
            self.player_sprite_on_ground = True
        else:
            self.player_sprite_on_ground = False

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10, 15)
            else:
                offset = pygame.math.Vector2(-10, 15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom - offset, 'land')
            self.dust_sprite.add(fall_dust_particle)

    def check_death(self):
        if self.player_sprite.sprite.rect.top > screen_height:
            self.create_selection(self.current_character, 0)
            self.bar_health_reset(self.cur_health)
            self.status = 'selection'

    def check_enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player_sprite.sprite, self.enemy_sprites, False)

        if enemy_collisions:
            for enemy in enemy_collisions:

                if self.player_sprite.sprite.attack:
                    death_sprite = ParticleEffect(enemy.rect.center, 'rat_death')
                    self.rat_death_sprite.add(death_sprite)
                    enemy.kill()
                    self.alive = False
                else:
                    self.player_sprite.sprite.get_damage(-10)

    def check_boss_collisions(self):
        boss = self.boss_sprite
        player = self.player_sprite.sprite
        # boss_collisions = pygame.sprite.spritecollide(player, boss, False)
        # boss_rect = boss.sprite.get_rect()
        if pygame.sprite.spritecollide(player, boss, False):
            if self.player_sprite.sprite.attack and not boss.sprite.invincible:
                print("atacou")
                boss.sprite.hp -= self.player_damage
                boss.sprite.invincible = True
                boss.sprite.hurt_time = pygame.time.get_ticks()
                print(boss.sprite.hp)
            elif not boss.sprite.invincible:
                print("colidiu")
                player.get_damage(-10)

    def check_boss_death(self):
        boss = self.boss_sprite.sprite
        if boss and boss.hp <= 0:
            death_sprite = ParticleEffect(boss.rect.center, 'boss_death')
            self.boss_death_sprite.add(death_sprite)
            boss.kill()
            self.boss_death = True
            # adiciona a chave ao dict para poder colectar
            self.items_dict[self.chave_sprites] = 7
            self.musicManager.loadMusic("victory", 0.1)

    def check_got_item(self):
        player = self.player_sprite.sprite
        keys = pygame.key.get_pressed()

        for sprites, idItem in self.items_dict.items():
            for item in sprites:
                rect = item.rect
                if rect.colliderect(player):
                    if keys[pygame.K_SPACE]:
                        self.musicManager.loadSound("item_collect", 0.2)
                        self.got_item = True
                        self.item_id = idItem
                        self.qtd_items_collected += 1
                        sprites.remove(item)

    def granade_collision_check(self):
        player = self.player_sprite.sprite
        if self.boss_sprite.sprite.grenades:
            for grenade in self.boss_sprite.sprite.grenades:
                if grenade.rect.colliderect(player.rect):
                    self.player_sprite.sprite.get_damage(-15)

    def arrow_collision_check(self):
        boss_sprite = self.boss_sprite.sprite
        if self.player_sprite.sprite.arrows:
            for arrow in self.player_sprite.sprite.arrows:
                for enemy in self.enemy_sprites:
                    if arrow.rect.colliderect(enemy.rect):
                        death_sprite = ParticleEffect(enemy.rect.center, 'rat_death')
                        self.rat_death_sprite.add(death_sprite)
                        self.alive = False
                        enemy.kill()
                        arrow.kill()
                if arrow:
                    if arrow.rect.colliderect(boss_sprite.rect) and not boss_sprite.invincible:
                        boss_sprite.hp -= self.player_damage
                        boss_sprite.invincible = True
                        boss_sprite.hurt_time = pygame.time.get_ticks()
                        arrow.kill()

    def run(self):
        # onde vou executar o nivel
        # deve colocar na ordem das camadas

        cor_ceu = (34, 27, 56)
        self.display_surface.fill(cor_ceu)

        # water
        self.water.draw(self.display_surface, self.world_shift)

        # CENA 1

        for sprite_group in self.grupos_sprites_cenario:
            sprite_group.update(self.world_shift)
            sprite_group.draw(self.display_surface)

        # chão
        self.chao_sprite.update(self.world_shift)
        self.chao_sprite.draw(self.display_surface)

        # chão floresta
        self.chao_floresta_sprites.update(self.world_shift)
        self.chao_floresta_sprites.draw(self.display_surface)

        # escada
        self.escada_sprites.update(self.world_shift)
        self.escada_sprites.draw(self.display_surface)

        # chave
        self.chave_sprites.update(self.world_shift)
        # caso o boss tenha morrido, mostra a chave
        if self.boss_death:
            self.chave_sprites.draw(self.display_surface)

        # enemies
        self.enemy_sprites.update(self.world_shift)
        self.constraints_sprites.update(self.world_shift)
        self.rat_collision_reverse()
        self.enemy_sprites.draw(self.display_surface)
        if self.alive:
            self.rat_death_sprite.update(self.world_shift)
            self.rat_death_sprite.draw(self.display_surface)

        # boss
        # boss health bar
        if self.is_final_fight and not self.boss_death:
            self.boss_sprite.sprite.run()
            self.boss_sprite.sprite.show_boss_health(self.display_surface)
            self.boss_sprite.sprite.grenades.draw(self.display_surface)

        if not self.boss_death:
            self.boss_sprite.update(self.world_shift)
            self.boss_collision_reverse()
            self.boss_sprite.draw(self.display_surface)
            self.check_boss_collisions()
            self.granade_collision_check()

        self.boss_death_sprite.update(self.world_shift)
        self.boss_death_sprite.draw(self.display_surface)

        # dust particles
        self.dust_sprite.update(self.world_shift)
        self.dust_sprite.draw(self.display_surface)

        # player
        self.player_sprite.update()
        self.player_sprite.sprite.arrows.draw(self.display_surface)
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.scroll_x()
        self.player_sprite.draw(self.display_surface)
        self.check_death()

        # check collisions
        self.check_enemy_collisions()
        self.check_boss_death()
        self.arrow_collision_check()
        self.check_got_item()
