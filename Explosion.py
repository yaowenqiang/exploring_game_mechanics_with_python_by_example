import pygame
import settings


class Explosion:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("images/explode.png")
        self.frame_x = 3
        self.frame_y = 3
        self.sprite_size = 32

    def draw(self, screen):
        screen.blit(self.image,
                    [self.x * self.sprite_size + settings.x_offset,
                     self.y * self.sprite_size + settings.y_offset,
                     self.sprite_size, self.sprite_size],
                    [self.frame_x * self.sprite_size, self.sprite_size * self.frame_y, self.sprite_size,
                     self.sprite_size])

        self.frame_x -= 1
        if self.frame_x <= 0:
            self.frame_x = 3
            self.frame_y -= 1
