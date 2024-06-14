import pygame
from pygame.locals import *
from Bullet import Bullet

class Player:
    def __init__(self, ypos):
        self.image = pygame.image.load("images/ship.png")
        self.x = 10
        self.y = ypos
        self.bullets = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += 3
        elif keys[K_LEFT]:
            self.x -= 3
        if keys[K_SPACE]:
            self.bullets.append(Bullet(self.x + self.image.get_width() // 2, self.y, 20))

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])

        for b in self.bullets:
            b.draw(screen)
