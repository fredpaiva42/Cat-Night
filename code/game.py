import pygame, sys
from settings import *
from level import Level
from game_data import king
from selection import Selection
from ui import UI
from player import Player
import settings

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

    def create_level(self, current_character):
        self.level = Level(current_character, screen, self.create_selection, self.change_health, self.bar_health_reset, self.cur_health)
        self.status = 'level'

        # user interface
        self.ui = UI(screen, current_character)

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
            self.selection = Selection(0, self.max_character, screen, self.create_level)
            self.status = 'selection'

    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            settings.GAME_STATE = 0

        if self.status == 'selection':
            self.selection.run()
        else:
            self.level.run()
            self.ui.show_health(self.cur_health, self.max_health)
            self.ui.show_inventory()
            self.check_game_over()