import pygame
import logging
import random
from pygame import Vector2
from pygame.transform import rotozoom

def wrap_position(position, screen):
    x, y = position
    w, h = screen.get_size()
    return Vector2(x % w, y % h)

def blit_rotated(position, image, forward, screen):
    angle = forward.angle_to(Vector2(0, -1))
    rotated_surface = rotozoom(image, angle, 1.0)
    rotated_surface_size = Vector2(rotated_surface.get_size())
    blit_position = position - rotated_surface_size // 2
    screen.blit(rotated_surface, blit_position)

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
        self.bullets = []
        self.can_shoot = 0
        self.drift = (0,0)

    def update(self):
        is_key_pressed = pygame.key.get_pressed()
        if is_key_pressed[pygame.K_UP]:
            self.position += self.forward
            self.drift = (self.drift + self.forward ) / 2
        if is_key_pressed[pygame.K_LEFT]:
            self.forward = self.forward.rotate(-1)
        if is_key_pressed[pygame.K_RIGHT]:
            self.forward = self.forward.rotate(1)
        if is_key_pressed[pygame.K_SPACE] and self.can_shoot == 0:
            self.bullets.append(Bullet(Vector2(self.position), self.forward))
            self.can_shoot = 500

        if self.can_shoot > 0:
            self.can_shoot -= clock.get_time()
        else:
            self.can_shoot = 0

        self.position += self.drift

    def draw(self, screen):
        self.position = wrap_position(self.position, screen)
        blit_rotated(self.position, self.image, self.forward, screen)


class Asteroid:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/RoidStarter/asteroid1.png')
        self.velocity = Vector2(random.randint(-3, 3), random.randint(-3, 3))

    def update(self):
        self.position += self.velocity

    def draw(self, screen):
        self.position = wrap_position(self.position, screen)
        blit_rotated(self.position, self.image, self.velocity, screen)


class Bullet:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def update(self):
        self.position += self.velocity

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), [self.position.x, self.position.y, 5, 5])


ship = Ship((100, 700))
asteroids = []
for i in range(10):
    asteroids.append(
        Asteroid((random.randint(0, screen.get_width()), random.randint(0, screen.get_height())))
    )

while not game_over:
    clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gme_over = True

    screen.blit(background, (0, 0))
    ship.update()
    ship.draw(screen)
    for a in asteroids:
        a.update()
        a.draw(screen)

    for b in ship.bullets:
        b.update()
        b.draw(screen)
    pygame.display.update()

pygame.quit()
