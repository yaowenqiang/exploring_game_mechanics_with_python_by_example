import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, y_speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/bullet.png")
        self.x = x - self.image.get_width() // 2
        self.y = y
        self.dy = y_speed
        self.rect = self.image.get_rect()
        self.rect.topleft = (self.x, self.y)

    def draw(self, screen):
        self.y -= self.dy
        self.rect.topleft = (self.x, self.y)
        screen.blit(self.image, [self.x, self.y, self.image.get_width(), self.image.get_height()])
