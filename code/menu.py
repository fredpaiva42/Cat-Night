import pygame, sys
from game import Game
import settings


class Menu:
    def __init__(self, surface):
        self.display_surface = surface
        self.game = Game()

        self.bg = pygame.image.load("./img/background/img_menu.png").convert()

        self.click = False

        # buttons
        self.button_play = pygame.image.load("./img/buttons/start.png").convert_alpha()
        self.button_play_rect = self.button_play.get_rect(center=(1120, 380))
        self.button_options = pygame.image.load("./img/buttons/options.png").convert_alpha()
        self.button_options_rect = self.button_options.get_rect(center=(1120, 515))
        self.button_exit = pygame.image.load("./img/buttons/exit.png").convert_alpha()
        self.button_exit_rect = self.button_exit.get_rect(center=(1120, 650))

    def show_buttons(self):
        self.display_surface.blit(self.button_play, self.button_play_rect)
        self.display_surface.blit(self.button_options, self.button_options_rect)
        self.display_surface.blit(self.button_exit, self.button_exit_rect)

    def run(self):
        settings.screen.blit(self.bg, (0, 0))
        click = pygame.mouse.get_pressed()
        self.show_buttons()

        if self.button_play_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 1

        if self.button_exit_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                pygame.quit()
                sys.exit()
