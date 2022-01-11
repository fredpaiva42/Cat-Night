import pygame
from support import import_folder
from random import randint


class Fireball(pygame.sprite.Sprite):
    def __init__(self, pos, speed, screen_width):
        super().__init__()
        self.import_character_assets()
        self.animation_speed = 0.15
        self.frame_index = 0
        self.image = self.animations['fire'][self.frame_index]
        self.rect = self.image.get_rect(center=pos)
        self.speed = speed
        self.width_x_constraint = screen_width
        self.facing_right = True

    def import_character_assets(self):
        self.animations = {'idle': [], 'run': [], 'jump': [], 'fall': [], 'attack': [], 'attack2': [], 'fire': []}
        character_path = '../img/character/mage/'

        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)

    def animate(self):
        animation = self.animations['fire']
        if self.speed > 0:
            self.facing_right = True
        else:
            self.facing_right = False

        # loop over frame index
        self.frame_index += self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def destroy(self):
        if self.rect.x <= - 50 or self.rect.x >= self.width_x_constraint + 800:
            self.kill()

    def update(self):
        self.animate()
        self.rect.x += self.speed
        self.destroy()

