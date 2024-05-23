"""
Title: Background Generator
Author: Radin and Owen
Date-Created: 5/14/2024
"""

from Window import Color
from Window import Window
from my_sprite import MySprite
from random import randint
import pygame


class ImageSprite(MySprite):
    # 36 * 20
    def __init__(self, width=200, height=200, file="media/goldensand.png"):
        MySprite.__init__(self, width, height, file="media/goldensand.png")
        self.__file_location = file
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = True

        self.tiles = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    def createTiles(self):
        # creates the tiles
        for x in range(0, 32):
            for y in range(0, 20):
                self.tiles[x].append(ImageSprite())

    def placeTiles(self):
        # places the tiles
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                self.tiles[x][y].setX((32 * x))
                self.tiles[x][y].setY((32 * y))

    def scaleTiles(self):
        # scales the tiles up
        for x in range(len(self.tiles)):
            for tile in self.tiles[x]:
                tile.setScale(1)

    def updateTiles(self):
        for x in range(len(self.tiles)):
            for y in range(len(self.tiles[x])):
                WINDOW.getScreen().blit(self.tiles[x][y].getSurface(), self.tiles[x][y].getPosition())


    def setX(self, x):
        self.x = x
        self.updatePosition()

    def setY(self, y):
        self.y = y
        self.updatePosition()

    def setPosition(self, x, y):
        self.x = x
        self.y = y
        # self.position = (self.x, self.y)
        self.updatePosition()


    def updatePosition(self):
        self.position = (self.x, self.y)


if __name__ == "__main__":
    WINDOW = Window("First Layer")
    SANDLAYER = ImageSprite()
    SANDLAYER.createTiles()
    SANDLAYER.placeTiles()
    SANDLAYER.scaleTiles()


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        SANDLAYER.updateTiles()
        WINDOW.updateFrame()

