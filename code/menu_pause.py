import pygame, sys
import settings
class MenuPause:
    def __init__(self, surface):
        self.display_surface = surface

        self.menu_pause = pygame.image.load("../img/background/menu_pause.png").convert_alpha()

        self.click = False

        # buttons
        self.button_home = pygame.image.load("../img/buttons/buttonHome.png").convert_alpha()
        self.button_home_rect = self.button_home.get_rect(center=(645, 280))
        self.button_resume = pygame.image.load("../img/buttons/buttonResume.png").convert_alpha()
        self.button_resume_rect = self.button_resume.get_rect(center=(645, 365))
        self.soundYes = pygame.image.load("../img/buttons/soundYes.png").convert_alpha()
        self.soundYes_rect = self.soundYes.get_rect(center=(605, 500))
        self.soundNo = pygame.image.load("../img/buttons/soundNo.png").convert_alpha()
        self.soundNo_rect = self.soundNo.get_rect(center=(685, 500))


    def show_buttons(self):
        self.display_surface.blit(self.button_home, self.button_home_rect)
        self.display_surface.blit(self.button_resume, self.button_resume_rect)
        self.display_surface.blit(self.soundYes, self.soundYes_rect)
        self.display_surface.blit(self.soundNo, self.soundNo_rect)

    def run(self):
        settings.screen.blit(self.menu_pause, (settings.screen_width /2 - 350, settings.screen_height /2 - 200))
        click = pygame.mouse.get_pressed()
        self.show_buttons()

        if self.button_home_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 0

        if self.button_resume_rect.collidepoint(pygame.mouse.get_pos()):
            if click[0] == 1:
                settings.GAME_STATE = 1
