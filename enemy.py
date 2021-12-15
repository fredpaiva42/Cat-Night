import pygame
from tiles import AnimatedTile
from random import randint


class Enemy(AnimatedTile):
    def __int__(self, size, x, y):
        super().__init__(size, x, y, './img/rato/')
        # self.speed = randint(3, 5)

    def move(self):
        self.rect.x += 3

    def reverse_image(self):
        if 3 > 0:
            self.image = pygame.transform.flip(self.image, True, False) # eixo x = True, eixo y = False

    # def reverse(self):


    def update(self, shift):
        self.rect.x += shift
        self.animate()
        self.move()
