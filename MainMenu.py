import pygame
from pygame.locals import *

class MainMenu:
    def __init__(self):
        # self.font = pygame.font.SysFont()
        self.font = pygame.font.SysFont('Arial', 80)
        self.title = self.font.render("Alien invasion!", True, (255,255,255))
        self.title_position = (10,10)
        self.gameplay_scene = None

    def update(self, events):
        for event in events:
            key_pressed = pygame.key.get_pressed()
            print(key_pressed)
            if key_pressed[K_SPACE]:
                return self.gameplay_scene
        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)



