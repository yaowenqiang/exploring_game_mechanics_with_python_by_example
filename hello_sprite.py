import pygame

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

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
    screen.blit(sprite1, (screen.get_width() / 2 - sprite_width / 2, screen.get_height() / 2 - sprite_height / 2))
    pygame.display.update()
pygame.quit()
