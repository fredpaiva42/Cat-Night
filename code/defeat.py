import pygame, sys
import settings
from game_data import characters
from support import import_folder
from ui import UI

class Cat(pygame.sprite.Sprite):
    def __init__(self, pos, path):
        super().__init__()
        self.frames = import_folder(path)
        self.frames_index = 0
        self.image = self.frames[self.frames_index]
        self.rect = self.image.get_rect(center=pos)

    def animate(self):
        self.frames_index += 0.1
        if self.frames_index >= len(self.frames):
            self.frames_index = 0
        self.image = self.frames[int(self.frames_index)]

    def update(self):
        self.animate()


class Defeat:
    def __init__(self,current_character, max_character, surface):
        self.display_surface = surface
        self.display_surface = surface
        self.max_character = max_character
        self.current_character = current_character
        # sprites
        self.setup_cat()

        self.click = False

        # buttons
        self.button_back = pygame.image.load("../img/buttons/button_back.png").convert_alpha()
        self.button_back_rect = self.button_back.get_rect(center=(640, 550))

    def show_buttons(self):
        self.display_surface.blit(self.button_back, self.button_back_rect)

    def setup_cat(self):
        self.cat = pygame.sprite.Group()

        if self.current_character == 0:
            node_sprite = Cat((650, 336), "../img/death/0/")
            self.cat.add(node_sprite)
        if self.current_character == 1:
            node_sprite = Cat((650, 336), "../img/death/1/")
            self.cat.add(node_sprite)
        if self.current_character == 2:
            node_sprite = Cat((650, 336), "../img/death/2/")
            self.cat.add(node_sprite)
        if self.current_character == 3:
            node_sprite = Cat((650, 336), "../img/death/3/")
            self.cat.add(node_sprite)

    def run(self):
        click = pygame.mouse.get_pressed()

        self.cat.update()
        self.cat.draw(self.display_surface)

        self.show_buttons()

        if self.button_back_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = -1
