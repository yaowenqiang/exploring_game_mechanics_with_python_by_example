import pygame

pygame.init()
w_width = 500
w_height = 500

screen = pygame.display.set_mode((w_width, w_height))

screen.fill('white')

pygame.display.set_caption("Handling Keyboard Events")

x = 0
y = 0
width = 50
height = 50
val = 5

clock = pygame.time.Clock()

done = True

is_jump = False
jump_count = 10
neg = 0

while done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            down = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP] and y > 0:
        y -= val

    if keys[pygame.K_DOWN] and y < w_height - width:
        y += val

    if not is_jump:
        if keys[pygame.K_LEFT] and x > 0:
            x -= val

        if keys[pygame.K_RIGHT] and x < w_width - width:
            x += val

        if keys[pygame.K_SPACE]:
            is_jump = True
    else:
        if is_jump:
            if jump_count >= -10:  # 10 frames up and 10 frames down
                neg = 1
                if jump_count < 0:
                    neg = -1
                y -= (jump_count ** 2) * neg * 0.5
                # parabolic motion(抛物线运动)
                jump_count -= 1
            else:
                jump_count = 10
                is_jump = False

    screen.fill('white')
    pygame.draw.rect(screen, 'black', (x, y, width, height))
    clock.tick(60)

    pygame.display.flip()
