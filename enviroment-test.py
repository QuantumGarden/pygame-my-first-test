import pygame
import numpy as np
import pygame.surfarray as surfarray
from random import randint

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 50
y = 50
width = 50
height = 50
obstacle_width = 50
obstacle_height = 50
vel = 50

run = True


def grid_to_px(X):
    x = X * 50
    return x


def px_to_grid(x):
    if x >= 450:
        X = 9
    else:
        X = round(x / 50)
    return X


def generate_enviroment():
    for X in range(10):

        for Y in range(10):
            if obstacles[X][Y] == 1:
                pygame.draw.rect(win, (0, 255, 0), (grid_to_px(X), grid_to_px(Y), obstacle_width, obstacle_height))


obstacles = np.zeros((10, 10))
obstacles[randint(0, 9), randint(0, 9)] = 1
obstacles[randint(0, 9), randint(0, 9)] = 1
obstacles[randint(0, 9), randint(0, 9)] = 1
obstacles[randint(0, 9), randint(0, 9)] = 1
print(obstacles)
"""" right_upper_corner_collision = obstacles[px_to_grid(x + width / 2), px_to_grid(y - height / 2)] != 0
    left_upper_corner_collision = obstacles[px_to_grid(x - width / 2), px_to_grid(y - height / 2)] != 0
    right_lower_corner_collision = obstacles[px_to_grid(x + width / 2), px_to_grid(y + height / 2)] != 0
    left_lower_corner_collision = obstacles[px_to_grid(x - width / 2), px_to_grid(y + height / 2)] != 0
    """
while run:


    lower_side_collision = obstacles[px_to_grid(x), px_to_grid(y + height / 2 + 1)] != 0
    left_side_collision = obstacles[px_to_grid(x - width / 2 - 1), px_to_grid(y)] != 0
    right_side_collision = obstacles[px_to_grid(x +width  / 2 + 1), px_to_grid(y)] != 0
    upper_side_collision = obstacles[px_to_grid(x ), px_to_grid(y-height/2-1)] != 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

 
    if keys[
        pygame.K_LEFT] and x != 0 and not left_side_collision:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[
        pygame.K_RIGHT] and x != 500 - width and not  right_side_collision:  # Making sure the top right corner of our character is less than the screen width - its width
        x += vel

    if keys[pygame.K_UP] and y != 0 and not upper_side_collision:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y != 500 - height and not lower_side_collision:
        y += vel

    # print(px_to_grid(x), px_to_grid(y))
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (0, 255, 255), (x, y, width, height))
    generate_enviroment()

    pygame.display.update()
    clock.tick(10)

pygame.quit()
