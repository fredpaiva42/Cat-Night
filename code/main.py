import pygame, sys
from settings import screen
from game import Game
from menu import Menu
from menu_pause import MenuPause
from help import Help
from musicManager import MusicManager
import settings
from credits import Credits
from victory import Victory
from chest import Chest


def reset_setup():
    menu = Menu(screen)
    game = Game(musicManager)
    return menu, game

pygame.init()
pygame.display.set_caption('Cat Night')
musicManager = MusicManager()
menu_pause = MenuPause(screen)
bt_help = Help(screen)
clock = pygame.time.Clock()
bg = pygame.image.load("../img/background/selection_menu.png").convert()
credits = Credits(screen)
chest = Chest(screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if settings.GAME_STATE == -1:
        menu, game = reset_setup()
        musicManager.loadMusic("menu", 0.1)
        settings.GAME_STATE = 0

    if settings.GAME_STATE == 0:
        screen.fill('black')
        menu.run()
    if settings.GAME_STATE == 1:
        screen.blit(bg, (0, 0))
        game.run()
    if settings.GAME_STATE == 2:
        menu_pause.run(musicManager)
    if settings.GAME_STATE == 3:
        bt_help.run()
    if settings.GAME_STATE == 4:
        game.defeat.run()
    if settings.GAME_STATE == 5:
        credits.run()
    if settings.GAME_STATE == 6:
        chest.run(game.inventory.collected_all())
    if settings.GAME_STATE == 7 or settings.GAME_STATE == 8:
        print(settings.GAME_STATE)
        victory = Victory(screen)
        victory.run()


    pygame.display.update()
    clock.tick(60)  # define fps
