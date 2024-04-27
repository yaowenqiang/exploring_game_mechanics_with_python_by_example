import pygame

# 初始化pygame
pygame.init()

# 设置窗口大小
window_size = (1920, 1080)

screen = pygame.display.set_mode(window_size, 0, 32)

pygame.display.set_caption('hello pygame')
screen.fill((0, 0, 0))

game_over = False

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
pygame.quit()
