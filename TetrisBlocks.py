import pygame

grid_size = 30
pygame.init()

screen = pygame.display.set_mode((800, 600))

cols = screen.get_width() // grid_size
rows = screen.get_height() // grid_size

x_gap = (screen.get_width() - cols * grid_size) // 2
y_gap = (screen.get_height() - rows * grid_size) // 2

pygame.display.set_caption("Tetris")

game_over = False


def draw_grid(rows, cols, grid_size, x_gap, y_gap):
    for y in range(rows):
        for x in range(cols):
            pygame.draw.rect(screen, (100, 100, 100), (x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size), 1)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill((0, 0, 0))

    draw_grid(rows, cols, grid_size, x_gap, y_gap)
    pygame.display.update()

pygame.quit()
