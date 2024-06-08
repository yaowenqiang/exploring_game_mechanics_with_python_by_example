import pygame
from pygame.locals import *

class GamePlay:
    def __init__(self, screen):
        # self.font = pygame.font.SysFont()
        self.font = pygame.font.SysFont('Arial', 20)
        self.title = self.font.render("This is where the game is", True, (255,255,255))
        self.title_position = (10,10)
        self.main_menu = None
        self.text_color = (255,255,255)
        self.button_color = (0,0,170)
        self.button_over_color = (255,50, 50)
        self.button_width = 50
        self.button_height = 20
        self.button_rect =[screen.get_width() - self.button_width,
                           0,
                           self.button_width,
                           self.button_height
                           ]
        self.button_font = pygame.font.SysFont('Arial', 15)
        self.button_text = self.button_font.render('Back', True, self.text_color)
        self.mouse_x, self.mouse_y = (0,0)



    def update(self, events):
        pass

    def draw(self, screen):
        screen.blit(self.title, self.title_position)



