import pygame, sys
import settings
from game_data import characters
from support import import_folder
from ui import UI

class Bau(pygame.sprite.Sprite):
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

class Chest:
        def __init__(self, surface):
            self.display_surface = surface
            # sprites
            self.setup_chest()

            self.click = False

            # buttons
            self.button_continue = pygame.image.load("../img/buttons/button_continue.png").convert_alpha()
            self.button_continue_rect = self.button_continue.get_rect(center=(640, 550))

        def show_buttons(self):
            self.display_surface.blit(self.button_continue, self.button_continue_rect)

        def setup_chest(self):
            self.chest = pygame.sprite.Group()

            node_sprite = Bau((650, 336), "../img/chest/")
            self.chest.add(node_sprite)

        def run(self):
            click = pygame.mouse.get_pressed()

            self.chest.update()
            self.chest.draw(self.display_surface)

            self.show_buttons()

            if self.button_continue_rect.collidepoint(pygame.mouse.get_pos()):
                if click[0] == 1:
                    settings.GAME_STATE = 7