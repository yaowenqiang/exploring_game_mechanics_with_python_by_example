import pygame
from pygame.locals import *

# 初始化pygame
pygame.init()

# 设置窗口大小
window_size = (1920, 1080)
# window_size = (800, 600)

sprite1 = pygame.image.load('./images/football.png')
sprite1 = pygame.transform.scale(sprite1, (128, 128))

sprite_width = sprite1.get_width()
sprite_height = sprite1.get_height()

screen = pygame.display.set_mode(window_size, 0, 32)

pygame.display.set_caption('hello Sprite')
screen.fill((0, 0, 0))

game_over = False
x, y = (0, 0)

clock = pygame.time.Clock()

while not game_over:
    dt = clock.tick(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

        elif event.type == pygame.MOUSEMOTION:
            x, y = event.pos
            x -= sprite_width / 2
            y -= sprite_height / 2

    pressed = pygame.key.get_pressed()
    if pressed[K_UP]:
        y -= 0.5 * dt
    if pressed[K_DOWN]:
        y += 0.5 * dt
    if pressed[K_LEFT]:
        x -= 0.5 * dt
    if pressed[K_RIGHT]:
        x += 0.5 * dt
    if pressed[K_SPACE]:
        x = 0
        y = 0
    if x > (screen.get_width() - sprite_width):
        x = screen.get_width() - sprite_width
    if x < 0:
        x = 0
    if y > (screen.get_height() - sprite_height):
        y = screen.get_height() - sprite_height
    if y < 0:
        y = 0
    screen.fill((0, 0, 0))
    screen.blit(sprite1, (x, y))
    pygame.display.update()
pygame.quit()
