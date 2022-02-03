import pygame, sys
import settings
from game_data import characters
from support import import_folder
from ui import UI

class Gammer(pygame.sprite.Sprite):
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


class Victory:
    def __init__(self, surface):
        self.display_surface = surface
        self.win = False
        # sprites
        self.setup_gammer()

        self.click = False

        # buttons
        self.button_back = pygame.image.load("../img/buttons/button_esc.png").convert_alpha()
        self.button_back_rect = self.button_back.get_rect(center=(640, 550))

    def show_buttons(self):
        self.display_surface.blit(self.button_back, self.button_back_rect)

    def setup_gammer(self):
        self.gammer = pygame.sprite.Group()
        if self.win:
            node_sprite = Gammer((650, 336), "../img/gammer/happy/")
            self.gammer.add(node_sprite)
        else:
            node_sprite = Gammer((650, 336), "../img/gammer/angry/")
            self.gammer.add(node_sprite)


    def run(self):
        keys = pygame.key.get_pressed()

        self.gammer.update()
        self.gammer.draw(self.display_surface)

        self.show_buttons()

        if keys[pygame.K_ESCAPE]:
            settings.GAME_STATE = 0

