from csv import reader
from settings import tile_tamanho
import pygame
from os import walk

def import_folder(path):
    surface_list = []
    for _,__, image_files in walk(path):
        for image in image_files:
            full_path = path + '/' + image
            image_surf = pygame.image.load(full_path).convert_alpha()
            surface_list.append(image_surf)
    return surface_list


# importa o caminho do arquivo csv
def import_csv_layout(path):
    chao_mapa = []
    with open(path) as mapa:
        level = reader(mapa, delimiter=',')
        for linha in level:
            chao_mapa.append(list(linha))
        return chao_mapa


# importa a imagem e corta
def import_graficos_cortados(path):
    janela = pygame.image.load(path).convert_alpha()
    tile_num_x = int(janela.get_size()[0] / tile_tamanho)
    tile_num_y = int(janela.get_size()[1] / tile_tamanho)

    tiles_cortados = []
    for linha in range(tile_num_y):
        for coluna in range(tile_num_x):
            x = coluna * tile_tamanho
            y = linha * tile_tamanho
            new_janela = pygame.Surface((tile_tamanho, tile_tamanho), flags=pygame.SRCALPHA) #isso resolve o problema das camadas
            new_janela.blit(janela, (0, 0), pygame.Rect(x, y, tile_tamanho, tile_tamanho))
            tiles_cortados.append(new_janela)

    return tiles_cortados
