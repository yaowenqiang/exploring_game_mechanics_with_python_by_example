import pygame

blocks = [
    [[1, 4, 7], [3, 4, 5]],  # straight
    [[1, 3, 4, 5, 7]],  # cross
    [[0, 1, 4, 5], [1, 3, 4, 6]],  # two on two 1
    [[1, 2, 3, 4], [0, 3, 4, 7]],  # two on two 2
    [[0, 1, 3, 6], [0, 1, 2, 5], [2, 5, 7, 8], [3, 6, 7, 8]],  # L 1
    [[1, 2, 5, 8], [5, 6, 7, 8], [8, 3, 6, 7], [0, 1, 2, 3]],  # L 2
    [[4, 6, 7, 8], [0, 3, 4, 6], [0, 1, 2, 4], [2, 4, 5, 8]],  # one on three

]

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
            pygame.draw.rect(screen, (100, 100, 100),
                             (x * grid_size + x_gap, y * grid_size + y_gap, grid_size, grid_size), 1)


while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True

    screen.fill((0, 0, 0))

    draw_grid(rows, cols, grid_size, x_gap, y_gap)
    pygame.display.update()

pygame.quit()
