import pygame
import numpy as np
import pygame.surfarray as surfarray
from random import randint
import time
import sys
np.set_printoptions(threshold=sys.maxsize)
SCREEN_WIDTH = 1900
SCREEN_HEIGHT = 1000

BLOB_HEIGHT = 10
BLOB_WIDTH = 10


class player:
    x = 250
    y = 250
    width = 10
    height = 10
    vel = 50

    def __init__(self, x, y, height, width, vel):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.vel = vel

    def player_movement(self, obstacles, food,size):
        if food[grid.px_to_grid(self.x,size)][grid.px_to_grid(self.y,size)] == 1:
            print("delicious")
            food[grid.px_to_grid(self.x,size)][grid.px_to_grid(self.y,size)] = 0
        lower_side_collision = obstacles[
                                   grid.px_to_grid(self.x + self.width / 2,size), grid.px_to_grid(self.y + self.height,size)] != 0
        left_side_collision = obstacles[grid.px_to_grid(self.x,size), grid.px_to_grid(self.y + self.height / 2,size)] != 0
        right_side_collision = obstacles[
                                   grid.px_to_grid(self.x + self.width,size), grid.px_to_grid(self.y + self.height / 2,size)] != 0
        upper_side_collision = obstacles[grid.px_to_grid(self.x + self.width / 2,size), grid.px_to_grid(self.y,size)] != 0

        keys = pygame.key.get_pressed()

        if keys[
            pygame.K_LEFT] and self.x != 0 and not obstacles[grid.px_to_grid(self.x - self.vel,size), grid.px_to_grid(
            self.y,size)]:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
            self.x -= self.vel

        if keys[
            pygame.K_RIGHT] and self.x != 500 - self.width and not obstacles[
            grid.px_to_grid(self.x + self.vel,size), grid.px_to_grid(
                self.y,size)]:  # Making sure the top right corner of our character is less than the screen width - its width
            self.x += self.vel

        if keys[pygame.K_UP] and self.y != 0 and not obstacles[
            grid.px_to_grid(self.x,size), grid.px_to_grid(self.y - self.vel,size)]:  # Same principles apply for the y coordinate
            self.y -= self.vel

        if keys[pygame.K_DOWN] and self.y != 500 - self.height and not obstacles[
            grid.px_to_grid(self.x,size), grid.px_to_grid(self.y + self.vel,size)]:
            self.y += self.vel

        pygame.draw.rect(win, (0, 255, 255), (self.x, self.y, self.width, self.height))


class obstacles_and_food:
    x_start = 10
    y_start = 10
    width = 25
    height = 25
    number_of_obstacles = 5

    def __init__(self, obstacle_width, obstacle_height, number_of_obstacles, obstacles, food):
        self.obstacle_height = obstacle_height
        self.obstacle_width = obstacle_width
        self.number_of_obstacles = number_of_obstacles
        self.obstacles = obstacles
        self.food = food

    def invert_array(self):
        for i in range(len(self.obstacles[0])):
            for j in range(len(self.obstacles[0])):
                self.obstacles[i][j] = not self.obstacles[i][j]

    def generate_obstacles(self):
        X, Y = self.x_start, self.y_start
        self.obstacles[X, Y] = 1

        for i in range(self.number_of_obstacles):

            neigborhoodX, neigborhoodY = self.generate_neighborhood()
            random = randint(0, len(neigborhoodX) - 1)
            X, Y = neigborhoodX[random], neigborhoodY[random]
            self.obstacles[X, Y] = 1
            if i > self.number_of_obstacles / 4:
                foodpropab = randint(0, 10)
                if foodpropab > 3:
                    self.food[X, Y] = 1
            elif i > self.number_of_obstacles / 3:
                foodpropab = randint(0, 10)
                if foodpropab > 10:
                    self.food[X, Y] = 1
            elif i > self.number_of_obstacles / 2:
                foodpropab = randint(0, 10)
                if foodpropab > 10:
                    self.food[X, Y] = 1
            elif i < self.number_of_obstacles / 2:
                foodpropab = randint(0, 10)
                if foodpropab > 10:
                    self.food[X, Y] = 1

            self.generate_enviroment(BLOB_WIDTH)
            clock.tick(60)
            pygame.display.update()
            pygame.event.pump()

        self.invert_array()

    def generate_neighborhood(self):

        #print(self.obstacles)
        neighborhoodX = []
        neighborhoodY = []
        x_indexes, y_indexes = np.where(self.obstacles == 1)

        #print(len(x_indexes))
        for i in range(len(x_indexes)):
            if x_indexes[i] < len(self.obstacles[0]) - 1 and y_indexes[i] < len(self.obstacles[0]) - 1:

                right_neigborhood = self.obstacles[x_indexes[i] + 1, y_indexes[i]]

                upper_neighborhood = self.obstacles[x_indexes[i], y_indexes[i] - 1]
                lower_neighborhood = self.obstacles[x_indexes[i], y_indexes[i] + 1]
                left_neighborhood = self.obstacles[x_indexes[i] - 1, y_indexes[i]]

                if right_neigborhood == 0:
                    neighborhoodX.append(x_indexes[i] + 1)
                    neighborhoodY.append(y_indexes[i])
                    #print('right')

                if left_neighborhood == 0:
                    neighborhoodX.append(x_indexes[i] - 1)
                    neighborhoodY.append(y_indexes[i])
                    #print('left')
                if lower_neighborhood == 0:
                    neighborhoodX.append(x_indexes[i])
                    neighborhoodY.append(y_indexes[i] + 1)
                    #print('lower')
                if upper_neighborhood == 0:
                    neighborhoodX.append(x_indexes[i])
                    neighborhoodY.append(y_indexes[i] - 1)
                    #print('upper')

        return neighborhoodX, neighborhoodY

    def generate_enviroment(self,size):
        for X in range(int(SCREEN_WIDTH/ self.obstacle_width)):

            for Y in range(int(SCREEN_HEIGHT / self.obstacle_height)):


                if self.obstacles[X][Y] == 1:
                    pygame.draw.rect(win, (0, 255, 0), (
                        grid.grid_to_px(X,self.obstacle_width), grid.grid_to_px(Y,self.obstacle_height), self.obstacle_width, self.obstacle_height))

                if self.obstacles[X][Y] == 0 and self.food[X][Y] == 1:
                    pygame.draw.rect(win, (255, 0, 255), (
                        grid.grid_to_px(X,size), grid.grid_to_px(Y,size), self.obstacle_width, self.obstacle_height))


run = True


class grid:
    width = 500
    height = 500

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def grid_to_px(X,size):
        x = X * size
        return x

    def px_to_grid(x,size):
        X = round(x / size)
        return X


pygame.init()
clock = pygame.time.Clock()
game_grid = grid(SCREEN_WIDTH, SCREEN_HEIGHT)
obstacles_array = np.zeros((int(game_grid.width / BLOB_WIDTH), int(game_grid.height / BLOB_HEIGHT)))
food_array = np.zeros((int(game_grid.width / BLOB_WIDTH), int(game_grid.height / BLOB_HEIGHT)))
win = pygame.display.set_mode((game_grid.width, game_grid.height))
pygame.display.set_caption("First Game")
player = player(100, 100, 10, 10, 10)
obstacles = obstacles_and_food(BLOB_WIDTH, BLOB_HEIGHT, 10000, obstacles_array, food_array)
obstacles.generate_obstacles()
print(obstacles.obstacles)
print(obstacles.obstacles.shape)
"""" right_upper_corner_collision = obstacles[px_to_grid(x + width / 2), px_to_grid(y - height / 2)] != 0
    left_upper_corner_collision = obstacles[px_to_grid(x - width / 2), px_to_grid(y - height / 2)] != 0
    right_lower_corner_collision = obstacles[px_to_grid(x + width / 2), px_to_grid(y + height / 2)] != 0
    left_lower_corner_collision = obstacles[px_to_grid(x - width / 2), px_to_grid(y + height / 2)] != 0
    """
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # print(player.x,player.y)

    win.fill((0, 0, 0))
    player.player_movement(obstacles.obstacles, obstacles.food,BLOB_WIDTH)
    obstacles.generate_enviroment(BLOB_WIDTH)

    pygame.display.update()

    clock.tick(10)

pygame.quit()
