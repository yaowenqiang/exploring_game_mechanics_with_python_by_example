import pygame
from pygame import Vector2
pygame.init()
screen = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Roids")

background = pygame.image.load("images/RoidStarter/space.png")

game_over = False


class Ship:
    def __init__(self, position):
        self.position = Vector2(position)
        self.image = pygame.image.load('images/RoidStarter/ship.png')

    def update(self):
        pass

    def draw(self, screen):
        screen.blit(self.image, self.position)


ship = Ship((100, 100))


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gme_over = True

    screen.blit(background, (0,0))
    ship.update()
    ship.draw(screen)
    pygame.display.update()

pygame.quit()

