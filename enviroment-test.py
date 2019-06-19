import pygame
import numpy as np
import pygame.surfarray as surfarray
from random import randint

pygame.init()
clock = pygame.time.Clock()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")


class player:
    x = 50
    y = 50
    width = 50
    height = 50
    vel = 50

    def __init__(self, x, y, height, width, vel):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = vel

    def player_movement(self, obstacles):

        lower_side_collision = obstacles[px_to_grid(self.x), px_to_grid(self.y + self.height / 2 + 1)] != 0
        left_side_collision = obstacles[px_to_grid(self.x - self.width / 2 - 1), px_to_grid(self.y)] != 0
        right_side_collision = obstacles[px_to_grid(self.x + self.width / 2 + 1), px_to_grid(self.y)] != 0
        upper_side_collision = obstacles[px_to_grid(self.x), px_to_grid(self.y - self.height / 2 - 1)] != 0

        keys = pygame.key.get_pressed()

        if keys[
            pygame.K_LEFT] and self.x != 0 and not left_side_collision:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            self.x -= self.vel

        if keys[
            pygame.K_RIGHT] and self.x != 500 - self.width and not right_side_collision:  # Making sure the top right corner of our character is less than the screen width - its width
            self.x += self.vel

        if keys[pygame.K_UP] and self.y != 0 and not upper_side_collision:  # Same principles apply for the y coordinate
            self. y -= self.vel

        if keys[pygame.K_DOWN] and self.y != 500 - self.height and not lower_side_collision:
            self.y +=self. vel

        pygame.draw.rect(win, (0, 255, 255), (self.x, self.y,self.width, self.height))


class obstacles:
    obstacle_width = 50
    obstacle_height = 50
    number_of_obstacles = 5
    obstacles = np.zeros((10, 10))

    def __init__(self, obstacle_width, obstacle_height, number_of_obstacles):
        self.obstacle_height = obstacle_height
        self.obstacle_width = obstacle_width
        self.number_of_obstacles = number_of_obstacles

    def generate_obstacles(self):
        for i in range(self.number_of_obstacles):
            self.obstacles[randint(0, 9), randint(0, 9)] = 1

    def generate_enviroment(self):
        for X in range(10):

            for Y in range(10):
                if self.obstacles[X][Y] == 1:
                    pygame.draw.rect(win, (0, 255, 0), (grid_to_px(X), grid_to_px(Y), self.obstacle_width, self.obstacle_height))


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


player = player(50, 50, 50, 50, 50)
obstacles = obstacles(50, 50, 5 )
obstacles.generate_obstacles()
"""" right_upper_corner_collision = obstacles[px_to_grid(x + width / 2), px_to_grid(y - height / 2)] != 0
    left_upper_corner_collision = obstacles[px_to_grid(x - width / 2), px_to_grid(y - height / 2)] != 0
    right_lower_corner_collision = obstacles[px_to_grid(x + width / 2), px_to_grid(y + height / 2)] != 0
    left_lower_corner_collision = obstacles[px_to_grid(x - width / 2), px_to_grid(y + height / 2)] != 0
    """
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


    print(player.x,player.y)

    win.fill((0, 0, 0))
    player.player_movement(obstacles.obstacles)
    obstacles.generate_enviroment()

    pygame.display.update()
    clock.tick(10)

pygame.quit()
