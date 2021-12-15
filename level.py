import pygame
from support import import_csv_layout, import_graficos_cortados
from settings import tile_tamanho
from tiles import Tile, StaticTile
from enemy import Enemy



class Level:
    def __init__(self, level_dados, janela):
        # configuração geral
        self.display_janela = janela
        self.velocidade_de_deslizamento = 0.3

        # configuração do chão
        chao_layout = import_csv_layout(level_dados['chao'])
        self.chao_sprite = self.create_tile_group(chao_layout, 'chao')  # isso garante que estamos pegando o arquivo
        # certo, pois todos começam com id 0

        # configuração dos predios de fundo
        predios_layout = import_csv_layout(level_dados['predios'])
        self.predios_sprite = self.create_tile_group(predios_layout, 'predios')

        # configuração das estrelas e luas
        estrelas_e_luas_layout = import_csv_layout(level_dados['estrelas e luas'])
        self.estrelas_e_luas_sprite = self.create_tile_group(estrelas_e_luas_layout, 'estrelas e luas')

        # nuvens
        nuvens_layout = import_csv_layout(level_dados['nuvens'])
        self.nuvens_sprite = self.create_tile_group(nuvens_layout, 'nuvens')

        # casa1
        casa1_layout = import_csv_layout(level_dados['casa1'])
        self.casa1_sprite = self.create_tile_group(casa1_layout, 'casa1')

        # arbustos casa1
        arbustos_casa1_layout = import_csv_layout(level_dados['arbustos casa1'])
        self.arbustosCasa1_sprite = self.create_tile_group(arbustos_casa1_layout, 'arbustos casa1')

        # fundo casa2
        fundo_casa2_layout = import_csv_layout(level_dados['fundo casa2'])
        self.fundo_casa2_sprite = self.create_tile_group(fundo_casa2_layout, 'fundo casa2')

        # casa2 frente
        casa2_frente_layout = import_csv_layout(level_dados['casa2 frente'])
        self.casa2_frente_sprite = self.create_tile_group(casa2_frente_layout, 'casa2 frente')

        # telhado fundos
        telhado_fundos_layout = import_csv_layout(level_dados['telhado fundos'])
        self.telhado_fundos_sprite = self.create_tile_group(telhado_fundos_layout, 'telhado fundos')

        # arvores
        arvores_layout = import_csv_layout(level_dados['arvores'])
        self.arvores_sprite = self.create_tile_group(arvores_layout, 'arvores')

        # telhados
        telhados_layout = import_csv_layout(level_dados['telhados'])
        self.telhados_sprite = self.create_tile_group(telhados_layout, 'telhados')

        # fundo pizzaria
        fundo_pizzaria_layout = import_csv_layout(level_dados['fundo pizzaria'])
        self.fundo_pizzaria_sprite = self.create_tile_group(fundo_pizzaria_layout, 'fundo pizzaria')

        # pizzaria
        pizzaria_layout = import_csv_layout(level_dados['pizzaria'])
        self.pizzaria_sprite = self.create_tile_group(pizzaria_layout, 'pizzaria')

        # enfeites dos telhados
        enfeites_dos_telhados_layout = import_csv_layout(level_dados['enfeites dos telhados'])
        self.enfeites_dos_telhados_sprite = self.create_tile_group(enfeites_dos_telhados_layout,
                                                                   'enfeites dos telhados')

        # chamines
        chamines_layout = import_csv_layout(level_dados['chamines'])
        self.chamines_sprite = self.create_tile_group(chamines_layout, 'chamines')

        # buraco da janela
        buraco_da_janela_layout = import_csv_layout(level_dados['buraco da janela'])
        self.buraco_da_janela_sprite = self.create_tile_group(buraco_da_janela_layout, 'buraco da janela')

        # casa roxa
        casa_roxa_layout = import_csv_layout(level_dados['casa roxa'])
        self.casa_roxa_sprite = self.create_tile_group(casa_roxa_layout, 'casa roxa')

        # mato do predio verde
        mato_predio_verde_layout = import_csv_layout(level_dados['mato do predio verde'])
        self.mato_do_predio_verde_sprite = self.create_tile_group(mato_predio_verde_layout, 'mato do predio verde')

        # predio verde
        predio_verde_layout = import_csv_layout(level_dados['predio verde'])
        self.predio_verde_sprite = self.create_tile_group(predio_verde_layout, 'predio verde')

        # mato do predio verde
        mato_do_predio_verde_layout = import_csv_layout(level_dados['mato do predio verde'])
        self.mato_predio_verde_sprite = self.create_tile_group(mato_do_predio_verde_layout, 'mato do predio verde')

        # parede preta
        parede_preta_layout = import_csv_layout(level_dados['parede preta'])
        self.parede_preta_sprite = self.create_tile_group(parede_preta_layout, 'parede preta')

        # predio marron
        predio_marron_layout = import_csv_layout(level_dados['predio marron'])
        self.predio_marron_sprite = self.create_tile_group(predio_marron_layout, 'predio marron')

        # telhado predio marron
        telhado_predio_marron_layout = import_csv_layout(level_dados['telhado predio marron'])
        self.telhado_predio_marron_sprite = self.create_tile_group(telhado_predio_marron_layout,
                                                                   'telhado predio marron')

        # predio rosa
        predio_rosa_layout = import_csv_layout(level_dados['predio rosa'])
        self.predio_rosa_sprite = self.create_tile_group(predio_rosa_layout, 'predio rosa')

        # buraco das janelas
        buraco_das_janelas_layout = import_csv_layout(level_dados['buraco das janelas'])
        self.buraco_das_janelas_sprite = self.create_tile_group(buraco_das_janelas_layout, 'buraco das janelas')

        # predio azul
        predio_azul_layout = import_csv_layout(level_dados['predio azul'])
        self.predio_azul_sprite = self.create_tile_group(predio_azul_layout, 'predio azul')

        # predio vermelho
        predio_vermelho_layout = import_csv_layout(level_dados['predio vermelho'])
        self.predio_vermelho_sprite = self.create_tile_group(predio_vermelho_layout, 'predio vermelho')

        # telhado predio vermelho
        telhado_predio_vermelho_layout = import_csv_layout(level_dados['telhado predio vermelho'])
        self.telhado_predio_vermelho_sprite = self.create_tile_group(telhado_predio_vermelho_layout,
                                                                     'telhado predio vermelho')

        # hotel
        hotel_layout = import_csv_layout(level_dados['hotel'])
        self.hotel_sprite = self.create_tile_group(hotel_layout, 'hotel')

        # portas e janelas
        portas_e_janelas_layout = import_csv_layout(level_dados['portas e janelas'])
        self.portas_e_janelas_sprite = self.create_tile_group(portas_e_janelas_layout, 'portas e janelas')

        # sacadas
        sacadas_layout = import_csv_layout(level_dados['sacadas'])
        self.sacadas_sprite = self.create_tile_group(sacadas_layout, 'sacadas')

        # tapume e cercas
        tapumes_e_cercas_layout = import_csv_layout(level_dados['tapumes e cercas'])
        self.tapumes_e_cercas_sprite = self.create_tile_group(tapumes_e_cercas_layout, 'tapumes e cercas')

        # jardim da casa1
        jardim_da_casa1_layout = import_csv_layout(level_dados['jardim da casa1'])
        self.jardim_da_casa1_sprite = self.create_tile_group(jardim_da_casa1_layout, 'jardim da casa1')

        # escada casa1
        escada_casa1_layout = import_csv_layout(level_dados['escada casa1'])
        self.escada_casa1_sprite = self.create_tile_group(escada_casa1_layout, 'escada casa1')

        # decoracao
        decoracao_layout = import_csv_layout(level_dados['decoracao'])
        self.decoracao_sprite = self.create_tile_group(decoracao_layout, 'decoracao')

        # mato cena2
        mato_cena2_layout = import_csv_layout(level_dados['mato cena 2'])
        self.mato_cena2_sprite = self.create_tile_group(mato_cena2_layout, 'mato cena 2')

        # morro cena 2
        morro_cena2_layout = import_csv_layout(level_dados['morro cena2'])
        self.morro_cena2_sprite = self.create_tile_group(morro_cena2_layout, 'morro cena2')

        # escada morro
        escada_morro_layout = import_csv_layout(level_dados['escada morro'])
        self.escada_morro_sprite = self.create_tile_group(escada_morro_layout, 'escada morro')

        # mato complementar
        mato_complementar_layout = import_csv_layout(level_dados['mato complementar'])
        self.mato_complementar_sprite = self.create_tile_group(mato_complementar_layout, 'mato complementar')

        # mato complementar 2
        mato_complementar2_layout = import_csv_layout(level_dados['mato complementar 2'])
        self.mato_complementar2_sprite = self.create_tile_group(mato_complementar2_layout, 'mato complementar 2')

        # arbustos cena 2
        arbustos_cena2_layout = import_csv_layout(level_dados['arbustos cena2'])
        self.arbustos_cena2_sprite = self.create_tile_group(arbustos_cena2_layout, 'arbustos cena2')

        # escada cena
        escada_cena2_layout = import_csv_layout(level_dados['escada cena'])
        self.escada_cena2_sprite = self.create_tile_group(escada_cena2_layout, 'escada cena')

        # parte da frente da escada
        parte_da_frente_layout = import_csv_layout(level_dados['parte da frente da escada'])
        self.parte_da_frente_sprite = self.create_tile_group(parte_da_frente_layout, 'parte da frente da escada')

        # loja cena2
        loja_layout = import_csv_layout(level_dados['loja cena2'])
        self.loja_sprite = self.create_tile_group(loja_layout, 'loja cena2')

        # arvore2
        arvore2_layout = import_csv_layout(level_dados['arvore2'])
        self.arvore2_sprite = self.create_tile_group(arvore2_layout, 'arvore2')

        # enfeites da cena 2
        enfeites_cena2_layout = import_csv_layout(level_dados['enfeites da cena 2'])
        self.enfeites_cena2_sprite = self.create_tile_group(enfeites_cena2_layout, 'enfeites da cena 2')

        # grama
        grama_layout = import_csv_layout(level_dados['grama'])
        self.grama_sprite = self.create_tile_group(grama_layout, 'grama')

        # enfeites finais da cena 2
        enfeites_finais_cena2_layout = import_csv_layout(level_dados['enfeites da cena 2'])
        self.enfeites_finais_cena2_sprite = self.create_tile_group(enfeites_finais_cena2_layout, 'enfeites finais da '
                                                                                                 'cena 2')

        # escada cena 3
        escada_cena3_layout = import_csv_layout(level_dados['escada cena 3'])
        self.escada_cena3_sprite = self.create_tile_group(escada_cena3_layout, 'escada cena 3')

        # chao cena 3
        chao_cena3_layout = import_csv_layout(level_dados['chao cena 3'])
        self.chaoCena3_sprite = self.create_tile_group(chao_cena3_layout, 'chao cena 3')

        # plataformas
        plataformas_layout = import_csv_layout(level_dados['plataformas'])
        self.plataformas_sprite = self.create_tile_group(plataformas_layout, 'plataformas')

        # mato cena 3
        mato_cena3_layout = import_csv_layout(level_dados['mato cena 3'])
        self.mato_cena3_sprite = self.create_tile_group(mato_cena3_layout, 'mato cena 3')

        # ponte
        ponte_layout = import_csv_layout(level_dados['ponte'])
        self.ponte_sprite = self.create_tile_group(ponte_layout, 'ponte')

        # placa de bem vindo
        placa_de_bemvindo_layout = import_csv_layout(level_dados['placa de bem vindo'])
        self.placa_bemvindo_sprite = self.create_tile_group(placa_de_bemvindo_layout, 'placa de bem vindo')

        # arvores cena 3
        arvores_cena3_layout = import_csv_layout(level_dados['arvores cena 3'])
        self.arvores3_sprite = self.create_tile_group(arvores_cena3_layout, 'arvores cena 3')

        # props cena 3
        props_cena3_layout = import_csv_layout(level_dados['props cena 3'])
        self.props_cena3_sprite = self.create_tile_group(props_cena3_layout, 'props cena 3')

        # inimigos
        inimigos_layout = import_csv_layout(level_dados['inimigos'])
        self.inimigos_sprite = self.create_tile_group(inimigos_layout, 'inimigos')

        # constraints delimita onde o ratinho anda
        contraints_layout = import_csv_layout(level_dados['constraints'])
        self.contraints_sprite = self.create_tile_group(contraints_layout, 'constraints')

    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()

        for linha_index, linha in enumerate(layout):
            for coluna_index, val in enumerate(linha):
                if val != '-1':
                    x = coluna_index * tile_tamanho
                    y = linha_index * tile_tamanho

                    if type == 'chao':
                        chao_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = chao_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'predios':
                        predios_tile_list = import_graficos_cortados('./img/mp_cs_background.png')
                        tile_janela = predios_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'estrelas e luas':
                        estrelas_tile_list = import_graficos_cortados('./img/mp_cs_background.png')
                        tile_janela = estrelas_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'nuvens':
                        nuvens_tile_list = import_graficos_cortados('./img/mp_cs_background.png')
                        tile_janela = nuvens_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'casa1':
                        casa_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = casa_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'arbustos casa1':
                        arbustos_casa1_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = arbustos_casa1_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'fundo casa2':
                        fundo_casa2_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = fundo_casa2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'casa2 frente':
                        casa2_frente_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = casa2_frente_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'telhado fundos':
                        telhado_fundos_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = telhado_fundos_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'arvores':
                        arvores_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = arvores_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'telhados':
                        telhados_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = telhados_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'fundo pizzaria':
                        fundo_pizzaria_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = fundo_pizzaria_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'pizzaria':
                        pizzaria_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = pizzaria_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'enfeites dos telhados':
                        enfeites_dos_telhados_tile_list = import_graficos_cortados('./img/mp_cs_props.png')
                        tile_janela = enfeites_dos_telhados_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'chamines':
                        chamines_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = chamines_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'buraco da janela':
                        buraco_da_janela_tile_list = import_graficos_cortados('./img/mp_cs_doors_windows.png')
                        tile_janela = buraco_da_janela_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'casa roxa':
                        casa_roxa_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = casa_roxa_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'mato do predio verde':
                        mato_do_predio_verde_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = mato_do_predio_verde_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'predio verde':
                        predio_verde_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = predio_verde_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'parede preta':
                        parede_preta_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = parede_preta_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'predio marron':
                        predio_marron_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = predio_marron_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'telhado predio marron':
                        telhado_predio_marron_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = telhado_predio_marron_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'predio rosa':
                        predio_rosa_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = predio_rosa_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'buraco das janelas':
                        buraco_das_janelas_tile_list = import_graficos_cortados('./img/mp_cs_doors_windows.png')
                        tile_janela = buraco_das_janelas_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'predio azul':
                        predio_azul_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = predio_azul_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'predio vermelho':
                        predio_vermelho_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = predio_vermelho_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'telhado predio vermelho':
                        telhado_predio_vermelho_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = telhado_predio_vermelho_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'hotel':
                        hotel_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = hotel_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'portas e janelas':
                        portas_e_janelas_tile_list = import_graficos_cortados('./img/mp_cs_doors_windows.png')
                        tile_janela = portas_e_janelas_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'sacadas':
                        sacadas_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = sacadas_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'tapumes e cercas':
                        tapumes_e_cercas_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = tapumes_e_cercas_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'jardim da casa1':
                        jardim_da_casa1_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = jardim_da_casa1_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'escada casa1':
                        escada_casa1_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = escada_casa1_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'decoracao':
                        decoracao_tile_list = import_graficos_cortados('./img/mp_cs_props.png')
                        tile_janela = decoracao_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'mato cena 2':
                        mato_cena2_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = mato_cena2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'morro cena2':
                        morro_cena2_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = morro_cena2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'escada morro':
                        escada_morro_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = escada_morro_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'mato complementar':
                        mato_complementar_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = mato_complementar_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'mato complementar 2':
                        mato_complementar2_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = mato_complementar2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'arbustos cena2':
                        arbustos_cena2_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = arbustos_cena2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'escada cena':
                        escada_cena2_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = escada_cena2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'parte da frente da escada':
                        parte_da_frente_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = parte_da_frente_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'loja cena2':
                        loja_tile_list = import_graficos_cortados('./img/mp_cs_doors_windows.png')
                        tile_janela = loja_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'arvore2':
                        arvore2_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = arvore2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'enfeites da cena 2':
                        enfeites_cena2_tile_list = import_graficos_cortados('./img/mp_cs_props.png')
                        tile_janela = enfeites_cena2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'grama':
                        grama_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = grama_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'enfeites finais da cena 2':
                        enfeites_finais_cena2_tile_list = import_graficos_cortados('./img/mp_cs_props.png')
                        tile_janela = enfeites_finais_cena2_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'escada cena 3':
                        escada_cena3_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = escada_cena3_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'chao cena 3':
                        chao_cena3_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = chao_cena3_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'plataformas':
                        plataformas_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = plataformas_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'mato cena 3':
                        mato_cena3_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = mato_cena3_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'ponte':
                        ponte_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = ponte_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'placa de bem vindo':
                        placa_bemvindo_tile_list = import_graficos_cortados('./img/mp_cs_buildings.png')
                        tile_janela = placa_bemvindo_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'arvores cena 3':
                        arvores_cena3_tile_list = import_graficos_cortados('./img/mp_cs_vegetation.png')
                        tile_janela = arvores_cena3_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'props cena 3':
                        props_cena3_tile_list = import_graficos_cortados('./img/mp_cs_props.png')
                        tile_janela = props_cena3_tile_list[int(val)]
                        sprite = StaticTile(tile_tamanho, x, y, tile_janela)
                        sprite_group.add(sprite)

                    if type == 'inimigos':
                        sprite = Enemy(tile_tamanho, x, y, './img/rato/')
                        sprite_group.add(sprite)

                    if type == 'constraints':
                        sprite = Tile(tile_tamanho, x, y)
                        sprite_group.add(sprite)

        return sprite_group

    # def rato_colisao_reverse(self):
    #     for enemy in self.inimigos_sprite.sprites():
    #         if pygame.sprite.spritecollide(enemy, self.contraints_sprite, False):
    #             enemy.reverse()

    def run(self):
        # onde vou executar o nivel
        # deve colocar na ordem das camadas

        cor_ceu = (34, 27, 56)
        self.display_janela.fill(cor_ceu)

        # chão
        self.chao_sprite.update(self.velocidade_de_deslizamento)
        self.chao_sprite.draw(self.display_janela)


        # predios de fundo
        self.predios_sprite.update(self.velocidade_de_deslizamento)
        self.predios_sprite.draw(self.display_janela)


        # estrelas e luas
        self.estrelas_e_luas_sprite.update(self.velocidade_de_deslizamento)
        self.estrelas_e_luas_sprite.draw(self.display_janela)


        # nuvens
        self.nuvens_sprite.update(self.velocidade_de_deslizamento)
        self.nuvens_sprite.draw(self.display_janela)


        # casa1
        self.casa1_sprite.update(self.velocidade_de_deslizamento)
        self.casa1_sprite.draw(self.display_janela)


        # arbustos da casa1
        self.arbustosCasa1_sprite.update(self.velocidade_de_deslizamento)
        self.arbustosCasa1_sprite.draw(self.display_janela)


        # fundo casa2
        self.fundo_casa2_sprite.update(self.velocidade_de_deslizamento)
        self.fundo_casa2_sprite.draw(self.display_janela)


        # casa2
        self.casa2_frente_sprite.update(self.velocidade_de_deslizamento)
        self.casa2_frente_sprite.draw(self.display_janela)


        # telhado fundos
        self.telhado_fundos_sprite.update(self.velocidade_de_deslizamento)
        self.telhado_fundos_sprite.draw(self.display_janela)


        # arvores
        self.arvores_sprite.update(self.velocidade_de_deslizamento)
        self.arvores_sprite.draw(self.display_janela)


        # telhados
        self.telhados_sprite.update(self.velocidade_de_deslizamento)
        self.telhados_sprite.draw(self.display_janela)


        # fundo pizzaria
        self.fundo_pizzaria_sprite.update(self.velocidade_de_deslizamento)
        self.fundo_pizzaria_sprite.draw(self.display_janela)


        # pizzaria
        self.pizzaria_sprite.update(self.velocidade_de_deslizamento)
        self.pizzaria_sprite.draw(self.display_janela)


        # enfeites dos telhados
        self.enfeites_dos_telhados_sprite.update(self.velocidade_de_deslizamento)
        self.enfeites_dos_telhados_sprite.draw(self.display_janela)


        # chamines
        self.chamines_sprite.update(self.velocidade_de_deslizamento)
        self.chamines_sprite.draw(self.display_janela)


        # buraco da janela
        self.buraco_da_janela_sprite.update(self.velocidade_de_deslizamento)
        self.buraco_da_janela_sprite.draw(self.display_janela)


        # casa roxa
        self.casa_roxa_sprite.update(self.velocidade_de_deslizamento)
        self.casa_roxa_sprite.draw(self.display_janela)


        # mato do predio verde
        self.mato_do_predio_verde_sprite.update(self.velocidade_de_deslizamento)
        self.mato_do_predio_verde_sprite.draw(self.display_janela)


        # predio verde
        self.predio_verde_sprite.update(self.velocidade_de_deslizamento)
        self.predio_verde_sprite.draw(self.display_janela)


        # parede preta
        self.parede_preta_sprite.update(self.velocidade_de_deslizamento)
        self.parede_preta_sprite.draw(self.display_janela)


        # predio marron
        self.predio_marron_sprite.update(self.velocidade_de_deslizamento)
        self.predio_marron_sprite.draw(self.display_janela)


        # telhado predio marron
        self.telhado_predio_marron_sprite.update(self.velocidade_de_deslizamento)
        self.telhado_predio_marron_sprite.draw(self.display_janela)


        # predio rosa
        self.predio_rosa_sprite.update(self.velocidade_de_deslizamento)
        self.predio_rosa_sprite.draw(self.display_janela)


        # buraco das janelas
        self.buraco_das_janelas_sprite.update(self.velocidade_de_deslizamento)
        self.buraco_das_janelas_sprite.draw(self.display_janela)


        # predio azul
        self.predio_azul_sprite.update(self.velocidade_de_deslizamento)
        self.predio_azul_sprite.draw(self.display_janela)


        # predio vermelho
        self.predio_vermelho_sprite.update(self.velocidade_de_deslizamento)
        self.predio_vermelho_sprite.draw(self.display_janela)


        # telhado predio vermelho
        self.telhado_predio_vermelho_sprite.update(self.velocidade_de_deslizamento)
        self.telhado_predio_vermelho_sprite.draw(self.display_janela)


        # hotel
        self.hotel_sprite.update(self.velocidade_de_deslizamento)
        self.hotel_sprite.draw(self.display_janela)


        # portas e janelas
        self.portas_e_janelas_sprite.update(self.velocidade_de_deslizamento)
        self.portas_e_janelas_sprite.draw(self.display_janela)


        # sacadas
        self.sacadas_sprite.update(self.velocidade_de_deslizamento)
        self.sacadas_sprite.draw(self.display_janela)


        # tapumes e cercas
        self.tapumes_e_cercas_sprite.update(self.velocidade_de_deslizamento)
        self.tapumes_e_cercas_sprite.draw(self.display_janela)

        # jardim da casa1
        self.jardim_da_casa1_sprite.update(self.velocidade_de_deslizamento)
        self.jardim_da_casa1_sprite.draw(self.display_janela)


        # escada casa1
        self.escada_casa1_sprite.update(self.velocidade_de_deslizamento)
        self.escada_casa1_sprite.draw(self.display_janela)


        # decoracao
        self.decoracao_sprite.update(self.velocidade_de_deslizamento)
        self.decoracao_sprite.draw(self.display_janela)


        # mato cena2
        self.mato_cena2_sprite.update(self.velocidade_de_deslizamento)
        self.mato_cena2_sprite.draw(self.display_janela)


        # morro cena2
        self.morro_cena2_sprite.update(self.velocidade_de_deslizamento)
        self.morro_cena2_sprite.draw(self.display_janela)


        # escada morro
        self.escada_morro_sprite.update(self.velocidade_de_deslizamento)
        self.escada_morro_sprite.draw(self.display_janela)

        # mato complementar
        self.mato_complementar_sprite.update(self.velocidade_de_deslizamento)
        self.mato_complementar_sprite.draw(self.display_janela)


        # mato complementar 2
        self.mato_complementar2_sprite.update(self.velocidade_de_deslizamento)
        self.mato_complementar2_sprite.draw(self.display_janela)


        # arbustos cena 2
        self.arbustos_cena2_sprite.update(self.velocidade_de_deslizamento)
        self.arbustos_cena2_sprite.draw(self.display_janela)


        # escada cena
        self.escada_cena2_sprite.update(self.velocidade_de_deslizamento)
        self.escada_cena2_sprite.draw(self.display_janela)


        # parte da frente da escada
        self.parte_da_frente_sprite.update(self.velocidade_de_deslizamento)
        self.parte_da_frente_sprite.draw(self.display_janela)


        # loja
        self.loja_sprite.update(self.velocidade_de_deslizamento)
        self.loja_sprite.draw(self.display_janela)


        # arvore2
        self.arvore2_sprite.update(self.velocidade_de_deslizamento)
        self.arvore2_sprite.draw(self.display_janela)


        # enfeites da cena 2
        self.enfeites_cena2_sprite.update(self.velocidade_de_deslizamento)
        self.enfeites_cena2_sprite.draw(self.display_janela)


        # grama
        self.grama_sprite.update(self.velocidade_de_deslizamento)
        self.grama_sprite.draw(self.display_janela)


        # enfeites finais da cena 2
        self.enfeites_finais_cena2_sprite.update(self.velocidade_de_deslizamento)
        self.enfeites_finais_cena2_sprite.draw(self.display_janela)


        # escada cena 3
        self.escada_cena3_sprite.update(self.velocidade_de_deslizamento)
        self.escada_cena3_sprite.draw(self.display_janela)


        # chão cena 3
        self.chaoCena3_sprite.update(self.velocidade_de_deslizamento)
        self.chaoCena3_sprite.draw(self.display_janela)


        # plataformas
        self.plataformas_sprite.update(self.velocidade_de_deslizamento)
        self.plataformas_sprite.draw(self.display_janela)


        # mato cena 3
        self.mato_cena3_sprite.update(self.velocidade_de_deslizamento)
        self.mato_cena3_sprite.draw(self.display_janela)


        # ponte
        self.ponte_sprite.update(self.velocidade_de_deslizamento)
        self.ponte_sprite.draw(self.display_janela)


        # placa de bem vindo
        self.placa_bemvindo_sprite.update(self.velocidade_de_deslizamento)
        self.placa_bemvindo_sprite.draw(self.display_janela)


        # arvores cena 3
        self.arvores3_sprite.update(self.velocidade_de_deslizamento)
        self.arvores3_sprite.draw(self.display_janela)


        # props cena 3
        self.props_cena3_sprite.update(self.velocidade_de_deslizamento)
        self.props_cena3_sprite.draw(self.display_janela)


        # inimigos
        self.inimigos_sprite.update(self.velocidade_de_deslizamento)
        self.contraints_sprite.update(self.velocidade_de_deslizamento)
        # self.rato_colisao_reverse()
        self.inimigos_sprite.draw(self.display_janela)


