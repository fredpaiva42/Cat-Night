import pygame, sys
from settings import screen
from level import Level
from game_data import king
from selection import Selection
from ui import UI
from player import Player
from game import Game
from menu import Menu
from menu_pause import MenuPause
from help import Help
import settings

# Pygame setup
pygame.init()
pygame.display.set_caption('Cat Night')
menu = Menu(screen)
menu_pause = MenuPause(screen)
bt_help = Help(screen)
clock = pygame.time.Clock()
game = Game()
bg = pygame.image.load("../img/background/selection_menu.png").convert()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if settings.GAME_STATE == 0:
        screen.fill('black')
        menu.run()
    if settings.GAME_STATE == 1:
        screen.blit(bg, (0, 0))
        game.run()
    if settings.GAME_STATE == 2:
        menu_pause.run()
    if settings.GAME_STATE == 3:
        bt_help.run()

    pygame.display.update()
    clock.tick(60)  # define fps
