import pygame
import logging
from pygame import Vector2
# from pygame import rotozoom
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Roids")

logging.basicConfig(level=logging.DEBUG)

background = pygame.image.load("images/RoidStarter/space.png")

game_over = False
clock = pygame.time.Clock()


class Ship:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/RoidStarter/ship.png')
        self.forward = Vector2(0, -1)

    def update(self):
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_UP]:
            self.position += self.forward
        if is_key_pressed[pygame.K_LEFT]:
            self.forward = self.forward.rotate(-1)
        if is_key_pressed[pygame.K_RIGHT]:
            self.forward = self.forward.rotate(1)

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        screen.blit(rotated_image, self.position)


class Asteroid:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/RoidStarter/asteroid1.png')

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.position)


ship = Ship((100, 700))
asteroid = Asteroid((300, 300))


while not game_over:
    clock.tick(55)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gme_over = True

    screen.blit(background, (0,0))
    ship.update()
    asteroid.update()
    ship.draw(screen)
    asteroid.draw(screen)
    pygame.display.update()

pygame.quit()

