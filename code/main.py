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
from defeat import Defeat
from musicManager import MusicManager
import settings
from credits import Credits
from victory import Victory
from chest import Chest

# Pygame setup
pygame.init()
pygame.display.set_caption('Cat Night')
musicManager = MusicManager()
menu = Menu(screen)
menu_pause = MenuPause(screen)
bt_help = Help(screen)
game = Game(musicManager)
clock = pygame.time.Clock()
bg = pygame.image.load("../img/background/selection_menu.png").convert()
credits = Credits(screen)
chest = Chest(screen)
victory = Victory(screen)

musicManager.loadMusic("menu", 0.1)

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
        menu_pause.run(musicManager)
    if settings.GAME_STATE == 3:
        bt_help.run()
    if settings.GAME_STATE == 4:
        game.defeat.run()
    if settings.GAME_STATE == 5:
        credits.run()
    if settings.GAME_STATE == 6:
        chest.run()
    if settings.GAME_STATE == 7:
        victory.run()


    pygame.display.update()
    clock.tick(60)  # define fps
