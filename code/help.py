import pygame, sys
import settings


class Help:
    def __init__(self, surface):
        self.display_surface = surface

        self.help = pygame.image.load("../img/background/img_controls.png").convert_alpha()

        self.click = False

        # buttons
        self.button_back = pygame.image.load("../img/buttons/button_back.png").convert_alpha()
        self.button_back_rect = self.button_back.get_rect(center=(440, 168))

    def show_buttons(self):
        self.display_surface.blit(self.button_back, self.button_back_rect)

    def run(self):
        settings.screen.blit(self.help, (settings.screen_width / 2 - 350, settings.screen_height / 2 - 270))
        click = pygame.mouse.get_pressed()
        self.show_buttons()

        if self.button_back_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 1

