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


class Background(MySprite):
    # 18 * 10
    def __init__(self, width=200, height=200, file="media/goldensand.png"):
        MySprite.__init__(self, width, height, file="media/goldensand.png")
        self.__file_location = file
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = True

        # todo
        self.currentMap

        self.backgroundSand = [[], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

        self.levelOneTiles = [["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

        self.levelTwoTiles = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "1", "0", "0", "0", "0", "0", "1", "1", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "1", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["0", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "1", "0", "0", "0", "0", "0", "1", "1", "1"],
                    ["1", "1", "0", "0", "0", "0", "1", "1", "1", "1"]]

        self.levelThreeTiles = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "0", "1", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "1", "0", "0", "1", "0", "0", "0", "1"],
                    ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1"],
                    ["1", "0", "1", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "1", "0", "1", "1", "0", "0", "0", "1"],
                    ["1", "0", "1", "0", "0", "1", "1", "1", "1", "1"],
                    ["1", "0", "1", "1", "0", "1", "0", "0", "0", "1"],
                    ["1", "0", "1", "0", "0", "1", "0", "1", "0", "1"],
                    ["1", "0", "1", "0", "1", "1", "0", "1", "0", "1"],
                    ["1", "0", "1", "0", "0", "0", "0", "1", "0", "1"],
                    ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1"],
                    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]

        self.levelFourTiles = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "2", "2", "2", "2", "2", "2", "2", "1"],
                    ["1", "0", "2", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "2", "0", "0", "2", "0", "0", "0", "1"],
                    ["1", "0", "2", "2", "2", "2", "2", "2", "0", "1"],
                    ["1", "0", "2", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "2", "0", "2", "2", "0", "0", "0", "1"],
                    ["1", "0", "2", "0", "0", "2", "2", "2", "2", "1"],
                    ["1", "0", "2", "2", "0", "2", "0", "0", "0", "1"],
                    ["1", "0", "2", "0", "0", "2", "0", "2", "0", "1"],
                    ["1", "0", "2", "0", "2", "2", "0", "2", "0", "1"],
                    ["1", "0", "2", "0", "0", "0", "0", "2", "0", "1"],
                    ["1", "0", "2", "2", "2", "2", "2", "2", "0", "1"],
                    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]]

    def createTiles(self, map):
        # creates the tiles
        for x in range(0, 16):
            for y in range(0, 10):
                try:
                    if str(map[x][y]) == "0":
                        map[x][y] = Background()
                    if str(map[x][y]) == "1":
                        map[x][y] = Background()
                        map[x][y].setSprite("media/water.png")
                    elif str(map[x][y]) == "2":
                        map[x][y] = Background()
                        map[x][y].setSprite("media/spike.png")
                except:
                    map[x].append(Background())
                    map[x][y].setSprite("media/goldensand.png")


    def placeTiles(self, map):
        # places the tiles
        for x in range(len(map)):
            for y in range(len(map[x])):
                map[x][y].setX((64 * x))
                map[x][y].setY((64 * y))

    def scaleTiles(self, map):
        # scales the tiles up
        for x in range(len(map)):
            for tile in map[x]:
                tile.setScale(2)

    def updateTiles(self, map, window):
        for x in range(len(map)):
            for y in range(len(map[x])):
                window.getScreen().blit(map[x][y].getSurface(), map[x][y].getPosition())


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

    def setMap(self, map):
        self.currentMap = self.map

    def checkBorder(self, player):
        # todo


if __name__ == "__main__":
    WINDOW = Window("First Layer")
    SANDLAYER = Background()

    # background sand
    SANDLAYER.createTiles(SANDLAYER.backgroundSand)
    SANDLAYER.placeTiles(SANDLAYER.backgroundSand)
    SANDLAYER.scaleTiles(SANDLAYER.backgroundSand)

    SANDLAYER.createTiles(SANDLAYER.levelFourTiles)
    SANDLAYER.placeTiles(SANDLAYER.levelFourTiles)
    SANDLAYER.scaleTiles(SANDLAYER.levelFourTiles)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.clearScreen()
        SANDLAYER.updateTiles(SANDLAYER.backgroundSand)
        SANDLAYER.updateTiles(SANDLAYER.levelFourTiles)
        WINDOW.updateFrame()
