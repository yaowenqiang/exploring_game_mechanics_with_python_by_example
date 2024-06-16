import pygame
import settings
from pygame.locals import *
from Bullet import Bullet
from pygame.sprite import Sprite


class Player(Sprite):
    def __init__(self, ypos):
        Sprite.__init__(self)
        self.image = pygame.image.load("images/ship.png")
        self.x = 10
        self.y = ypos
        self.bullets = []
        self.font = pygame.font.SysFont("Arial", 25)
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)
        self.lives = 3

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.x += 3
        elif keys[K_LEFT]:
            self.x -= 3
        if keys[K_SPACE]:
            self.bullets.append(Bullet(self.x + self.image.get_width() // 2, self.y, 20))

        self.rect.topleft = (self.x, self.y)

        for l in pygame.sprite.spritecollide(self, settings.abullets, 0):
            settings.abullets.remove(l)
            l.kill()
            self.lives -= 1

    def draw(self, screen):
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])
        self.text_lives = self.font.render(f"Lives: {self.lives}", True, (255, 100, 100))
        screen.blit(self.text_lives, [0, 0])

        for b in self.bullets:
            b.draw(screen)
