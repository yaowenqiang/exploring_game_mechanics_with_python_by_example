import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))

screen.fill('white')

pygame.display.set_caption("Draw shapes.")


pygame.draw.line(screen, 'black', (0,0), (300, 300), 5)
pygame.draw.lines(screen, 'orange', True, [(100, 100), (200, 100), (100, 200)], 5)

pygame.draw.rect(screen, 'red', (50, 50, 100, 100), 7)

pygame.draw.circle(screen, 'red', (200, 150), 50, 1)

pygame.draw.ellipse(screen, 'yellow', (200, 100, 100, 50), 4)

pygame.draw.polygon(screen, 'blue', ((250, 75), (300, 25), (350, 75)), 0)

done = True

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            down = False

    pygame.display.flip()
