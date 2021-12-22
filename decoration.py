from settings import vertical_tile_qtd, tile_size, screen_width
import pygame
from tiles import AnimatedTile


class Water:
    def __init__(self, top, level_width):
        water_start = + screen_width * 1.62
        water_tile_width = 192
        tile_x_amount = int((level_width + screen_width) / water_tile_width)
        self.water_sprites = pygame.sprite.Group()

        for tile in range(tile_x_amount):
            x = tile * water_tile_width + water_start
            y = top
            sprite = AnimatedTile(192, x, y, './img/background/decoration/')
            self.water_sprites.add(sprite)

    def draw(self, surface, shift):
        self.water_sprites.update(shift)
        self.water_sprites.draw(surface)
