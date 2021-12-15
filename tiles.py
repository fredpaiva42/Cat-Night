import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self, tamanho, x, y):
        super().__init__()
        self.image = pygame.Surface((tamanho, tamanho))

        self.rect = self.image.get_rect(topleft=(x, y))

    # faz o cenário se mover
    def update(self, shift):
        self.rect.x -= shift


class StaticTile(Tile):  # herda da classe Tile
    def __init__(self, tamanho, x, y, janela):
        super().__init__(tamanho, x, y)
        self.image = janela

class AnimatedTile(Tile):
    def __init__(self, tamanho, x, y, path):
        super().__init__(tamanho, x, y)
        self.frames = import_folder(path)
        self.frame_index = 0
        self.image = self.frames[self.frame_index]

    def animate(self):
        self.frame_index += 0.15
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self, shift):
        self.animate()
        self.rect.x -= shift




