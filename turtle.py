"""
Title: turret class
Author: Radin and Owen
Date-created: 5/14/2024
"""

import pygame
from my_sprite import MySprite
from background import Background
from Window import Window
import random


class Turtle(MySprite):

    def __init__(self, width=200, height=200, x=500, y=500, speed=5, file="media/turtle.png"):
        MySprite.__init__(self, width, height, x, y, speed, file)
        self.file_location = file
        self.surface = pygame.Surface
        self.surface = pygame.image.load(self.file_location).convert_alpha()
        self.turtles = []

    def createTurtles(self):
        for x in range(0, 10):
            self.turtles.append(Turtle())

    def placeTurtles(self):
        # places the tiles
        for x in range(len(self.turtles)):
            self.turtles[x].setX((64 * x + 200))
            self.turtles[x].setY((random.randint(30, 600)))


    def moveTurtles(self, window, max_height):
        for x in range(len(self.turtles)):
            self.turtles[x].bounceY(max_height)
            if self.turtles[x].dir_Y == -1:
                window.getScreen().blit(pygame.transform.flip(self.turtles[x].getSurface(), False, False), self.turtles[
                    x].getPosition())
            else:
                window.getScreen().blit(pygame.transform.flip(self.turtles[x].getSurface(), False, True), self.turtles[
                    x].getPosition())


    def checkTurtleCollision(self, position, width, height):
        for x in range(0, 16):
            for y in range(0, 10):
                if self.currentMap[x][y].getSprite() == "media/spike.png":
                    if position[0] >= self.currentMap[x][y].getX() - width \
                            and position[0] <= self.currentMap[x][y].getX() + self.currentMap[x][y].getWidth()\
                            and position[1] >= self.currentMap[x][y].getY() - height\
                            and position[1] <= self.currentMap[x][y].getY() + self.currentMap[x][y].getHeight():
                        return True
                    else:
                        pass