import pygame

class SecondMenu:
    def __init__(self):
        # self.font = pygame.font.SysFont()
        self.font = pygame.font.SysFont('Arial', 80)
        self.title = self.font.render("This is second!", True, (255,255,255))
        self.title_position = (10,10)

    def update(self, events):
        return self

    def draw(self, screen):
        screen.blit(self.title, self.title_position)



