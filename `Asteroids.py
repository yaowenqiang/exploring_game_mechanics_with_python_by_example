import pygame
import logging
import  random
from pygame import Vector2
from pygame.transform import rotozoom
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
        angle = self.forward.angle_to(Vector2(0, -1))
        rotated_surface = rotozoom(self.image, angle, 1.0)
        rotated_surface_size = Vector2(rotated_surface.get_size())
        blit_position = self.position - rotated_surface_size // 2
        screen.blit(rotated_surface, blit_position)


class Asteroid:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/RoidStarter/asteroid1.png')
        self.velocity = Vector2(random.randint(-3, 3), random.randint(-3, 3))

    def update(self):
        self.position += self.velocity

    def draw(self, screen):
        screen.blit(self.image, self.position)


ship = Ship((100, 700))
asteroids = []
for i in range(10):
    asteroids.append(
        Asteroid((random.randint(0, screen.get_width()), random.randint(0, screen.get_height())))
    )



while not game_over:
    clock.tick(55)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gme_over = True

    screen.blit(background, (0,0))
    ship.update()
    ship.draw(screen)
    for a in asteroids:
        print(a.position)
        a.update()
        a.draw(screen)
    pygame.display.update()

pygame.quit()

