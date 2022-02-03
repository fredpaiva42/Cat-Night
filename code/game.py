import pygame, sys
from settings import *
from level import Level
from game_data import king
from selection import Selection
from ui import UI
from ui import Inventory
from player import Player
from menu_pause import MenuPause
from help import Help
import settings
from defeat import Defeat
from  defeat import Death


class Game:
    def __init__(self):
        # game atributes
        self.max_character = 3
        self.max_health = 100
        self.cur_health = 100
        self.count_damage = 0
        self.start_character = 0

        # character selection
        self.selection = Selection(self.start_character, self.max_character, screen, self.create_level)
        self.status = 'selection'

        # initializing button pause, get position
        self.button_pause = pygame.image.load('../img/buttons/pause.png').convert_alpha()
        self.button_pause_rect = self.button_pause.get_rect(center=(1170, 50))

        #  initializing button help, get position
        self.button_help = pygame.image.load('../img/buttons/button_help.png').convert_alpha()
        self.button_help_rect = self.button_pause.get_rect(center=(1240, 50))

        # Menu Pause
        self.menu_pause = pygame.image.load("../img/background/menu_pause.png").convert()

    def create_level(self, current_character):
        self.level = Level(current_character, screen, self.create_selection, self.change_health, self.bar_health_reset,
                           self.cur_health)
        self.status = 'level'

        # user interface
        self.ui = UI(screen, current_character)

        self.death = Death(current_character)

        self.inventory = Inventory(screen)

    def create_selection(self, current_character, new_max_character):
        if new_max_character > self.max_character:
            self.max_character = new_max_character
        self.selection = Selection(current_character, self.max_character, screen, self.create_level)
        self.status = 'selection'

    def change_health(self, amount):
        self.cur_health += amount
        return self.cur_health

    def bar_health_reset(self, amount):
        self.cur_health -= amount
        return self.cur_health

    def check_game_over(self):
        if self.cur_health <= 0:
            self.cur_health = 100
            settings.GAME_STATE = 4
            self.selection = Selection(0, self.max_character, screen, self.create_level)
            self.status = 'selection'

    def run(self):
        click = pygame.mouse.get_pressed()
        if self.button_pause_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 2
        if self.button_help_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 3

        if self.status == 'selection':
            self.selection.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_pause_button()
            self.ui.show_help_button()
            self.inventory.run(self.level.got_item, self.level.item_id)
            self.check_game_over()
