import pygame


class UI:
    def __init__(self, surface, current_character):
        # setup
        self.display_surface = surface
        self.current_character = current_character
        self.path = './ui/stats0.png'

        if self.current_character == 1:
            self.path = './ui/stats.png'
        if self.current_character == 2:
            self.path = './ui/stats2.png'
        if self.current_character == 3:
            self.path = './ui/stats3.png'

        # health
        self.health_bar = pygame.image.load(self.path).convert_alpha()
        self.health_bar_topleft = (115, 20)
        self.bar_max_width = 150
        self.bar_height = 8

        # inventory
        self.inventory = pygame.image.load('./ui/inventario.png').convert_alpha()
        self.inventory_rect = self.inventory.get_rect(center=(725, 60))

    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (20, 10))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, '#FF0044', health_bar_rect)

    def show_inventory(self):
        self.display_surface.blit(self.inventory, self.inventory_rect)
