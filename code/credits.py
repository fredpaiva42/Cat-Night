import pygame, sys
import settings


class Credits:
    def __init__(self, surface):
        self.display_surface = surface

        self.credits = pygame.image.load("../img/background/Credits.png").convert()

        self.click = False

        # buttons
        self.button_back = pygame.image.load("../img/buttons/button_back.png").convert_alpha()
        self.button_back_rect = self.button_back.get_rect(center=(650,600))

    def show_buttons(self):
        self.display_surface.blit(self.button_back, self.button_back_rect)

    def run(self):
        settings.screen.blit(self.credits, (0, 0))
        click = pygame.mouse.get_pressed()
        self.show_buttons()

        if self.button_back_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 0

