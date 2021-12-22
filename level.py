import pygame
from support import import_csv_layout, import_cut_graphics
from settings import tile_size, screen_height, screen_width
from tiles import Tile, StaticTile
from player import Player
from decoration import Water


class Level:
    def __init__(self, level_data, surface):
        # configuração geral
        self.display_surface = surface
        self.world_shift = 0
        self.current_x = None

        # player
        player_layout = import_csv_layout(level_data['player'])
        self.player = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.player_setup(player_layout)

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

        # decoration
        level_width = (len(chao_layout[0]) - 77.5) * tile_size
        self.water = Water(screen_height - 35, level_width)

        # TRANSIÇÃO PARA CENA 2
        transicao_layout = import_csv_layout(level_data['transicao'])
        self.transicao_sprite = self.create_tile_group(transicao_layout, 'transicao')

        # CENA 2
        # parede_preta
        parede_preta_layout = import_csv_layout(level_data['parede_preta'])
        self.parede_preta_sprite = self.create_tile_group(parede_preta_layout, 'parede_preta')

        # predio_rosa
        predio_rosa_layout = import_csv_layout(level_data['predio_rosa'])
        self.predio_rosa_sprite = self.create_tile_group(predio_rosa_layout, 'predio_rosa')

        # predio_azul
        predio_azul_layout = import_csv_layout(level_data['predio_azul'])
        self.predio_azul_sprite = self.create_tile_group(predio_azul_layout, 'predio_azul')

        # chão cena 2
        chao_cena2_layout = import_csv_layout(level_data['chao_cena2'])
        self.chao_cena2_sprite = self.create_tile_group(chao_cena2_layout, 'chao_cena2')

        # predio_verde
        predio_verde_layout = import_csv_layout(level_data['predio_verde'])
        self.predio_verde_sprite = self.create_tile_group(predio_verde_layout, 'predio_verde')

        # predio_marron
        predio_marron_layout = import_csv_layout(level_data['predio_marron'])
        self.predio_marron_sprite = self.create_tile_group(predio_marron_layout, 'predio_marron')

        # predio_vermelho
        predio_vermelho_layout = import_csv_layout(level_data['predio_vermelho'])
        self.predio_vermelho_sprite = self.create_tile_group(predio_vermelho_layout, 'predio_vermelho')

        # vegetacao
        vegetacao_layout = import_csv_layout(level_data['vegetacao'])
        self.vegetacao_sprite = self.create_tile_group(vegetacao_layout, 'vegetacao')

        # portas_janelas_cena2
        portas_janelas_cena2_layout = import_csv_layout(level_data['portas_janelas_cena2'])
        self.portas_janelascena2_sprite = self.create_tile_group(portas_janelas_cena2_layout, 'portas_janelas_cena2')

        # props_cena2
        props_cena2_layout = import_csv_layout(level_data['props_cena2'])
        self.props_cena2_sprite = self.create_tile_group(props_cena2_layout, 'props_cena2')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        tile_list_all = import_cut_graphics('img/background/mp_cs_tilemap_all 1.png')
        tile_list_vegetation = import_cut_graphics('img/background/mp_cs_vegetation 1.png')

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

                    if type == 'transicao':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'parede_preta':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_rosa':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_azul':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'chao_cena2':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_verde':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_marron':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'predio_vermelho':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'vegetacao':
                        tile_surface = tile_list_vegetation[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'portas_janelas_cena2':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

                    if type == 'props_cena2':
                        tile_surface = tile_list_all[int(val)]
                        sprite = StaticTile(tile_size, x, y, tile_surface)
                        sprite_group.add(sprite)

        return sprite_group

    def player_setup(self, layout):
        for row_index, row in enumerate(layout):
            for col_index, val in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if val == '0':
                    sprite = Player((x, y), self.display_surface)
                    self.player.add(sprite)

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        collidable_sprites = self.chao_sprite.sprites() + self.transicao_sprite.sprites() + self.chao_cena2_sprite.sprites() + self.predio_verde_sprite.sprites() + self.predio_azul_sprite.sprites() + self.predio_rosa_sprite.sprites() + self.parede_preta_sprite.sprites()
        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()
        collidable_sprites = self.chao_sprite.sprites() + self.transicao_sprite.sprites() + self.chao_cena2_sprite.sprites() + self.predio_verde_sprite.sprites() + self.predio_azul_sprite.sprites() + self.predio_rosa_sprite.sprites() + self.parede_preta_sprite.sprites()

        for sprite in collidable_sprites:
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0.1:
            player.on_ceiling = False

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = -6
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift = + 6
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 6

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def run(self):
        # onde vou executar o nivel
        # deve colocar na ordem das camadas

        cor_ceu = (34, 27, 56)
        self.display_surface.fill(cor_ceu)

        # CENA 1

        # chão
        self.chao_sprite.update(self.world_shift)
        self.chao_sprite.draw(self.display_surface)

        # nuvens
        self.nuvens_sprite.update(self.world_shift)
        self.nuvens_sprite.draw(self.display_surface)

        # predios
        self.predios_sprite.update(self.world_shift)
        self.predios_sprite.draw(self.display_surface)

        # casa_1
        self.casa1_sprite.update(self.world_shift)
        self.casa1_sprite.draw(self.display_surface)

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

        # telhados
        self.telhados_sprite.update(self.world_shift)
        self.telhados_sprite.draw(self.display_surface)

        # grades_casa2
        self.grades_casa2_sprite.update(self.world_shift)
        self.grades_casa2_sprite.draw(self.display_surface)

        # portas_surfaces
        self.portas_janelas_sprite.update(self.world_shift)
        self.portas_janelas_sprite.draw(self.display_surface)

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

        # jardim_casa1
        self.jardim_casa1_sprite.update(self.world_shift)
        self.jardim_casa1_sprite.draw(self.display_surface)

        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.get_player_on_ground()
        self.vertical_movement_collision()
        self.scroll_x()
        self.player.draw(self.display_surface)

        # water
        self.water.draw(self.display_surface, self.world_shift)

        # TRANSIÇÃO CENA 2
        self.transicao_sprite.update(self.world_shift)
        self.transicao_sprite.draw(self.display_surface)

        # CENA 2

        # parede_preta
        self.parede_preta_sprite.update(self.world_shift)
        self.parede_preta_sprite.draw(self.display_surface)

        # predio_rosa
        self.predio_rosa_sprite.update(self.world_shift)
        self.predio_rosa_sprite.draw(self.display_surface)

        # predio_azul
        self.predio_azul_sprite.update(self.world_shift)
        self.predio_azul_sprite.draw(self.display_surface)

        # chao_cena2
        self.chao_cena2_sprite.update(self.world_shift)
        self.chao_cena2_sprite.draw(self.display_surface)

        # predio_verde
        self.predio_verde_sprite.update(self.world_shift)
        self.predio_verde_sprite.draw(self.display_surface)

        # predio_marron
        self.predio_marron_sprite.update(self.world_shift)
        self.predio_marron_sprite.draw(self.display_surface)

        # predio_vermelho
        self.predio_vermelho_sprite.update(self.world_shift)
        self.predio_vermelho_sprite.draw(self.display_surface)

        # vegetacao
        self.vegetacao_sprite.update(self.world_shift)
        self.vegetacao_sprite.draw(self.display_surface)

        # portas_janelas_cena2
        self.portas_janelascena2_sprite.update(self.world_shift)
        self.portas_janelascena2_sprite.draw(self.display_surface)

        # props_cena2
        self.props_cena2_sprite.update(self.world_shift)
        self.props_cena2_sprite.draw(self.display_surface)