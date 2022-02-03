import pygame
import settings
from victory import Victory


class UI:
    def __init__(self, surface, current_character):
        # setup
        self.display_surface = surface
        self.current_character = current_character
        self.path = '../ui/stats0.png'

        if self.current_character == 1:
            self.path = '../ui/stats.png'
        if self.current_character == 2:
            self.path = '../ui/stats2.png'
        if self.current_character == 3:
            self.path = '../ui/stats3.png'

        # health
        self.health_bar = pygame.image.load(self.path).convert_alpha()
        self.health_bar_topleft = (115, 20)
        self.bar_max_width = 150
        self.bar_height = 8

        # pause button
        self.button_pause = pygame.image.load('../img/buttons/pause.png').convert_alpha()
        self.button_rect = self.button_pause.get_rect(center=(1170, 50))

        # help button
        self.button_help = pygame.image.load('../img/buttons/button_help.png').convert_alpha()
        self.button_help_rect = self.button_pause.get_rect(center=(1240, 50))

    def show_health(self, current, full):
        self.display_surface.blit(self.health_bar, (20, 10))
        current_health_ratio = current / full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft, (current_bar_width, self.bar_height))
        pygame.draw.rect(self.display_surface, '#FF0044', health_bar_rect)

    def show_pause_button(self):
        self.display_surface.blit(self.button_pause, self.button_rect)

    def show_help_button(self):
        self.display_surface.blit(self.button_help, self.button_help_rect)


class Inventory:
    def __init__(self, surface):
        self.surface = surface
        self.slots = []

        self.image = pygame.image.load('../ui/inventario.png').convert_alpha()
        self.inventory_rect = self.image.get_rect(center=(900, 50))

    def collected_all(self):
        return (len(self.slots)) >= 6

    def run(self, got_item, id_item):
        self.surface.blit(self.image, self.inventory_rect)
        for slot in self.slots:
            slot.run(self.surface)

        if got_item:
            self.slots.append(InventorySlot(id_item))


class InventorySlot:
    def __init__(self, id_item):
        if id_item == 1:
            self.image = pygame.image.load('../img/items/colher.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)

        elif id_item == 2:
            self.image = pygame.image.load('../img/items/pergaminho.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)

        elif id_item == 3:
            self.image = pygame.image.load('../img/items/colar.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)

        elif id_item == 4:
            self.image = pygame.image.load('../img/items/perfume.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)

        elif id_item == 5:
            self.image = pygame.image.load('../img/items/capuz.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)

        elif id_item == 6:
            self.image = pygame.image.load('../img/items/anel.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)

        elif id_item == 7:
            self.image = pygame.image.load('../img/items/chave.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.topleft = (658 + (57 * id_item), 35)
            # ganha o jogo
            settings.GAME_STATE = 6


    def run(self, surface):
        surface.blit(self.image, self.rect)
