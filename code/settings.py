import pygame
vertical_tile_qtd = 21
tile_size = 32

GAME_STATE = -1
SOUND = True
COLLECTED_ALL = False

screen_height = vertical_tile_qtd * tile_size
screen_width = 1300

flags = pygame.SCALED
screen = pygame.display.set_mode((screen_width, screen_height), flags)