import settings
import pygame

class Story:
    def __init__(self, surface):
        self.display_surface = surface

        self.story = pygame.image.load("../img/background/story.png").convert_alpha()

        self.click = False


    def run(self):
        settings.screen.blit(self.story, (0,0))
        key = pygame.key.get_pressed()

        if key[pygame.K_RETURN]:
            settings.GAME_STATE = 1
