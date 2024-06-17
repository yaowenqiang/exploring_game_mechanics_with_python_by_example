import pygame

pygame.init()

screen = pygame.display.set_mode((300, 300))

screen.fill('white')

pygame.display.set_caption("My First Pygame Program")

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            down = False

    pygame.display.flip()
