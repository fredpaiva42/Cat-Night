import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width, screen
from tiles import Tile, StaticTile
from player import Player
from decoration import Water
from enemy import Enemy
from enemy import Boss
from game_data import characters
from particles import ParticleEffect
from ui import UI


class Level:
    def __init__(self, current_character, surface, musicManager, create_selection, change_health, bar_health_reset, cur_health):
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

        # configuração do chão
        chao_layout = import_csv_layout(level_data['chao'])
        self.chao_sprite = self.create_tile_group(chao_layout, 'chao')  # isso garante que estamos pegando o arquivo
        # certo, pois todos começam com id 0

        # nuvens
        nuvens_layout = import_csv_layout(level_data['nuvens'])
        self.nuvens_sprite = self.create_tile_group(nuvens_layout, 'nuvens')

        # predios
        predios_layout = import_csv_layout(level_data['predios'])
        self.predios_sprite = self.create_tile_group(predios_layout, 'predios')

        # casa_1
        casa_1_layout = import_csv_layout(level_data['casa_1'])
        self.casa1_sprite = self.create_tile_group(casa_1_layout, 'casa_1')

        # arvore_casa1
        arvore_layout = import_csv_layout(level_data['arvore'])
        self.arvore_sprite = self.create_tile_group(arvore_layout, 'arvore')

        # casa2_fachada
        casa2_fachada_layout = import_csv_layout(level_data['casa2_fachada'])
        self.casa2_fachada_sprite = self.create_tile_group(casa2_fachada_layout, 'casa2_fachada')

        # casa2_fundos
        casa2_fundos_layout = import_csv_layout(level_data['casa2_fundos'])
        self.casa2_fundos_sprite = self.create_tile_group(casa2_fundos_layout, 'casa2_fundos')

        # pizzaria
        pizzaria_layout = import_csv_layout(level_data['pizzaria'])
        self.pizzaria_sprite = self.create_tile_group(pizzaria_layout, 'pizzaria')

        # telhados_fundos
        telhados_fundos_layout = import_csv_layout(level_data['telhados_fundos'])
        self.telhados_fundos_sprite = self.create_tile_group(telhados_fundos_layout, 'telhados_fundos')

        # telhados
        telhados_layout = import_csv_layout(level_data['telhados'])
        self.telhados_sprite = self.create_tile_group(telhados_layout, 'telhados')

        # grades_casa2
        grades_casa2_layout = import_csv_layout(level_data['grades_casa2'])
        self.grades_casa2_sprite = self.create_tile_group(grades_casa2_layout, 'grades_casa2')

        # portas_janelas
        portas_janelas_layout = import_csv_layout(level_data['portas_janelas'])
        self.portas_janelas_sprite = self.create_tile_group(portas_janelas_layout, 'portas_janelas')

        # tapumes
        tapumes_layout = import_csv_layout(level_data['tapumes'])
        self.tapumes_sprite = self.create_tile_group(tapumes_layout, 'tapumes')

        # arbustos_casa1
        arbustos_casa1_layout = import_csv_layout(level_data['arbustos_casa1'])
        self.arvore_casa1_sprite = self.create_tile_group(arbustos_casa1_layout, 'arbustos_casa1')

        # carro
        carro_layout = import_csv_layout(level_data['carro'])
        self.carro_sprite = self.create_tile_group(carro_layout, 'carro')

        # cercas
        cercas_layout = import_csv_layout(level_data['cercas'])
        self.cercas_sprite = self.create_tile_group(cercas_layout, "cercas")

        # jardim_casa1
        jardim_casa1_layout = import_csv_layout(level_data['jardim_casa1'])
        self.jardim_casa1_sprite = self.create_tile_group(jardim_casa1_layout, 'jardim_casa1')

        # escada
        escada_layout = import_csv_layout(level_data['escada'])
        self.escada_sprites = self.create_tile_group(escada_layout, 'escada')

        # sombras
        sombras_layout = import_csv_layout(level_data['sombras'])
        self.sombras_sprites = self.create_tile_group(sombras_layout, 'sombras')

        # casa 3
        casa_3_layout = import_csv_layout(level_data['casa_3'])
        self.casa_3_sprites = self.create_tile_group(casa_3_layout, 'casa_3')

        # extra casa 3
        extra_casa3_layout = import_csv_layout(level_data['extra_casa3'])
        self.extra_casa3_sprites = self.create_tile_group(extra_casa3_layout, 'extra_casa3')

        # jardim casa 3
        jardim_casa3_layout = import_csv_layout(level_data['jardim_casa3'])
        self.jardim_casa3_sprites = self.create_tile_group(jardim_casa3_layout, 'jardim_casa3')

        # grades cima
        grades_cima_layout = import_csv_layout(level_data['grades_cima'])
        self.grades_cima_sprites = self.create_tile_group(grades_cima_layout, 'grades_cima')

        # grades extra
        grades_extra_layout = import_csv_layout(level_data['grades_extra'])
        self.grades_extra_sprites = self.create_tile_group(grades_extra_layout, 'grades_extra')

        # extra predio 4
        extra_predio4_layout = import_csv_layout(level_data['extra_predio4'])
        self.extra_predio4_sprites = self.create_tile_group(extra_predio4_layout, 'extra_predio4')

        # predio 4
        predio_4_layout = import_csv_layout(level_data['predio_4'])
        self.predio_4_sprites = self.create_tile_group(predio_4_layout, 'predio_4')

        # subsolo_emcima
        subsolo_emcima_layout = import_csv_layout(level_data['subsolo_emcima'])
        self.subsolo_emcima_sprites = self.create_tile_group(subsolo_emcima_layout, 'subsolo_emcima')

        # subsolo
        subsolo_layout = import_csv_layout(level_data['subsolo'])
        self.subsolo_sprites = self.create_tile_group(subsolo_layout, 'subsolo')

        # parede subsolo
        parede_subsolo_layout = import_csv_layout(level_data['parede_subsolo'])
        self.parede_subsolo_sprites = self.create_tile_group(parede_subsolo_layout, 'parede_subsolo')

        # estrelas
        estrelas_layout = import_csv_layout(level_data['estrelas'])
        self.estrelas_sprites = self.create_tile_group(estrelas_layout, 'estrelas')

        # hotel
        hotel_layout = import_csv_layout(level_data['hotel'])
        self.hotel_sprites = self.create_tile_group(hotel_layout, 'hotel')

        # predio alto
        predio_alto_layout = import_csv_layout(level_data['predio_alto'])
        self.predio_alto_sprites = self.create_tile_group(predio_alto_layout, 'predio_alto')

        # ponte
        ponte_layout = import_csv_layout(level_data['ponte'])
        self.ponte_sprites = self.create_tile_group(ponte_layout, 'ponte')

        # floresta
        floresta_layout = import_csv_layout(level_data['floresta'])
        self.floresta_sprites = self.create_tile_group(floresta_layout, 'floresta')

        # chao_floresta
        chao_floresta_layout = import_csv_layout(level_data['chao_floresta'])
        self.chao_floresta_sprites = self.create_tile_group(chao_floresta_layout, 'chao_floresta')

        # enemies
        enemy_layout = import_csv_layout(level_data['enemies'])
        self.enemy_sprites = self.create_tile_group(enemy_layout, 'enemies')

        # constraints
        constraints_layout = import_csv_layout(level_data['constraints'])
        self.constraints_sprites = self.create_tile_group(constraints_layout, 'constraints')

        # ITENS
        # colher
        colher_layout = import_csv_layout(level_data['colher'])
        self.colher_sprites = self.create_tile_group(colher_layout, 'colher')

        # pergaminho
        pergaminho_layout = import_csv_layout(level_data['pergaminho'])
        self.pergaminho_sprites = self.create_tile_group(pergaminho_layout, 'pergaminho')

        # colar
        colar_layout = import_csv_layout(level_data['colar'])
        self.colar_sprites = self.create_tile_group(colar_layout, 'colar')

        # perfume
        perfume_layout = import_csv_layout(level_data['perfume'])
        self.perfume_sprites = self.create_tile_group(perfume_layout, 'perfume')

        # capuz
        capuz_layout = import_csv_layout(level_data['capuz'])
        self.capuz_sprites = self.create_tile_group(capuz_layout, 'capuz')

        # anel
        anel_layout = import_csv_layout(level_data['anel'])
        self.anel_sprites = self.create_tile_group(anel_layout, 'anel')

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

                    if type == 'chao':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'nuvens':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predios':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'casa_1':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'arvore':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'casa2_fachada':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'casa2_fundos':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'pizzaria':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'telhados_fundos':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'telhados':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'grades_casa2':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'portas_janelas':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'tapumes':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'arbustos_casa1':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'carro':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'cercas':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'jardim_casa1':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'escada':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'sombras':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'casa_3':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'extra_casa3':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'jardim_casa3':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'grades_cima':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'grades_extra':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'extra_predio4':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_4':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'subsolo_emcima':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'subsolo':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'parede_subsolo':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'estrelas':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'hotel':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_alto':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'ponte':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'floresta':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'chao_floresta':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'enemies':
                        sprite = Enemy(tile_size, x, y, '../img/enemies/rat/run', 'run')
                        sprite_group.add(sprite)

                    if type == 'constraints':
                        sprite = Tile(tile_size, x, y)
                        sprite_group.add(sprite)

                    if type == 'colher':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'pergaminho':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'colar':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'perfume':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'capuz':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'anel':
                        tile_surface = tile_list_items[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'chave':
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
                    sprite = Boss(tile_size, x, y, '../img/enemies/dog/run', 'run')
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
        #boss_collisions = pygame.sprite.spritecollide(player, boss, False)
        #boss_rect = boss.sprite.get_rect()
        if boss.sprite.rect.colliderect(player.attack_collision_rect) and self.player_sprite.sprite.attack and not boss.sprite.invincible:
            print("atacou")
            boss.sprite.hp -= self.player_damage
            boss.sprite.invincible = True
            boss.sprite.hurt_time = pygame.time.get_ticks()
            print(boss.sprite.hp)
        if boss.sprite.rect.colliderect(player.collision_rect):
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
                        sprites.remove(item)

    def granade_collision_check(self):
        player = self.player_sprite.sprite
        if self.boss_sprite.sprite.grenades:
            for grenade in self.boss_sprite.sprite.grenades:
                if grenade.rect.colliderect(player.rect):
                    self.player_sprite.sprite.get_damage(-10)


    def arrow_collision_check(self):
        boss_sprite = self.boss_sprite.sprite
        if self.player_sprite.sprite.arrows:
            for arrow in self.player_sprite.sprite.arrows:
                for enemy in self.enemy_sprites:
                    if arrow.rect.colliderect(enemy.rect):
                        death_sprite = ParticleEffect(enemy.rect.center, 'rat_death')
                        self.rat_death_sprite.add(death_sprite)
                        enemy.kill()
                        arrow.kill()
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

        # estrelas
        self.estrelas_sprites.update(self.world_shift)
        self.estrelas_sprites.draw(self.display_surface)

        # nuvens
        self.nuvens_sprite.update(self.world_shift)
        self.nuvens_sprite.draw(self.display_surface)

        # predios
        self.predios_sprite.update(self.world_shift)
        self.predios_sprite.draw(self.display_surface)

        # chão
        self.chao_sprite.update(self.world_shift)
        self.chao_sprite.draw(self.display_surface)

        # chão floresta
        self.chao_floresta_sprites.update(self.world_shift)
        self.chao_floresta_sprites.draw(self.display_surface)

        # parede subsolo
        self.parede_subsolo_sprites.update(self.world_shift)
        self.parede_subsolo_sprites.draw(self.display_surface)

        # subsolo
        self.subsolo_sprites.update(self.world_shift)
        self.subsolo_sprites.draw(self.display_surface)

        # floresta
        self.floresta_sprites.update(self.world_shift)
        self.floresta_sprites.draw(self.display_surface)

        # em cima subsolo
        self.subsolo_emcima_sprites.update(self.world_shift)
        self.subsolo_emcima_sprites.draw(self.display_surface)


        # ponte
        self.ponte_sprites.update(self.world_shift)
        self.ponte_sprites.draw(self.display_surface)

        # hotel
        self.hotel_sprites.update(self.world_shift)
        self.hotel_sprites.draw(self.display_surface)

        # predio 4
        self.predio_4_sprites.update(self.world_shift)
        self.predio_4_sprites.draw(self.display_surface)

        # predio 4 extra
        self.extra_predio4_sprites.update(self.world_shift)
        self.extra_predio4_sprites.draw(self.display_surface)

        # escada
        self.escada_sprites.update(self.world_shift)
        self.escada_sprites.draw(self.display_surface)

        # casa_1
        self.casa1_sprite.update(self.world_shift)
        self.casa1_sprite.draw(self.display_surface)

        # casa 3
        self.casa_3_sprites.update(self.world_shift)
        self.casa_3_sprites.draw(self.display_surface)

        # grades extra
        self.grades_extra_sprites.update(self.world_shift)
        self.grades_extra_sprites.draw(self.display_surface)

        # perfume
        self.perfume_sprites.update(self.world_shift)
        self.perfume_sprites.draw(self.display_surface)

        # grades em cima
        self.grades_cima_sprites.update(self.world_shift)
        self.grades_cima_sprites.draw(self.display_surface)

        # arvore_casa1
        self.arvore_sprite.update(self.world_shift)
        self.arvore_sprite.draw(self.display_surface)

        # casa2_fachada
        self.casa2_fachada_sprite.update(self.world_shift)
        self.casa2_fachada_sprite.draw(self.display_surface)

        # casa2_fundos
        self.casa2_fundos_sprite.update(self.world_shift)
        self.casa2_fundos_sprite.draw(self.display_surface)

        # pizzaria
        self.pizzaria_sprite.update(self.world_shift)
        self.pizzaria_sprite.draw(self.display_surface)

        # telhados_fundos
        self.telhados_fundos_sprite.update(self.world_shift)
        self.telhados_fundos_sprite.draw(self.display_surface)

        # predio alto
        self.predio_alto_sprites.update(self.world_shift)
        self.predio_alto_sprites.draw(self.display_surface)

        # telhados
        self.telhados_sprite.update(self.world_shift)
        self.telhados_sprite.draw(self.display_surface)

        # grades_casa2
        self.grades_casa2_sprite.update(self.world_shift)
        self.grades_casa2_sprite.draw(self.display_surface)

        # jardim casa 3
        self.jardim_casa3_sprites.update(self.world_shift)
        self.jardim_casa3_sprites.draw(self.display_surface)

        # extra casa 3
        self.extra_casa3_sprites.update(self.world_shift)
        self.extra_casa3_sprites.draw(self.display_surface)

        # capuz
        self.capuz_sprites.update(self.world_shift)
        self.capuz_sprites.draw(self.display_surface)

        # anel
        self.anel_sprites.update(self.world_shift)
        self.anel_sprites.draw(self.display_surface)

        # portas janelas
        self.portas_janelas_sprite.update(self.world_shift)
        self.portas_janelas_sprite.draw(self.display_surface)

        # sombras
        self.sombras_sprites.update(self.world_shift)
        self.sombras_sprites.draw(self.display_surface)

        # pergaminho
        self.pergaminho_sprites.update(self.world_shift)
        self.pergaminho_sprites.draw(self.display_surface)

        # colar
        self.colar_sprites.update(self.world_shift)
        self.colar_sprites.draw(self.display_surface)

        # tapumes
        self.tapumes_sprite.update(self.world_shift)
        self.tapumes_sprite.draw(self.display_surface)

        # arbustos_casa1
        self.arvore_casa1_sprite.update(self.world_shift)
        self.arvore_casa1_sprite.draw(self.display_surface)

        # carro
        self.carro_sprite.update(self.world_shift)
        self.carro_sprite.draw(self.display_surface)

        # cercas
        self.cercas_sprite.update(self.world_shift)
        self.cercas_sprite.draw(self.display_surface)

        # colher
        self.colher_sprites.update(self.world_shift)
        self.colher_sprites.draw(self.display_surface)

        # jardim_casa1
        self.jardim_casa1_sprite.update(self.world_shift)
        self.jardim_casa1_sprite.draw(self.display_surface)

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

        self.check_enemy_collisions()
        self.check_boss_death()
        self.arrow_collision_check()
        self.check_got_item()
