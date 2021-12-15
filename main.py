import pygame, sys
from settings import *
from level import Level
from game_data import level_0

# Pygame setup
pygame.init()
tela = pygame.display.set_mode((tela_largura, tela_altura))
relogio = pygame.time.Clock()
level = Level(level_0, tela)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    tela.fill('black')
    level.run()

    pygame.display.update()
    relogio.tick(60)  # define fps
