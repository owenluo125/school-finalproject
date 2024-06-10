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
#from player import healthBar

class Background(MySprite):
    # 18 * 10
    def __init__(self, width=200, height=200, file="media/goldensand.png"):
        MySprite.__init__(self, width, height, file="media/goldensand.png")
        self.file_location = file
        self.surface = pygame.image.load(self.file_location).convert_alpha()
        self.image_dir_x = True

        self.currentMap = []

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
                    ["0", "0", "0", "0", "0", "9", "0", "0", "0", "0"],
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
                    ["1", "1", "0", "9", "0", "0", "1", "1", "1", "1"]]

        self.levelThreeTiles = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "0", "0", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "1", "1", "1", "1", "1", "1", "1", "1"],
                    ["1", "0", "1", "0", "0", "0", "0", "0", "0", "1"],
                    ["1", "0", "1", "9", "0", "1", "0", "0", "0", "1"],
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
                    ["1", "0", "2", "9", "0", "2", "0", "0", "0", "1"],
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

        self.levelOnePosition = (50, 480)
        self.levelTwoPosition = (150, 350)
        self.levelThreePosition = (80, 520)
        self.levelFourPosition = (80, 520)

    def createTiles(self):
        # creates the tiles
        for x in range(0, 16):
            for y in range(0, 10):
                try:
                    if str(self.currentMap[x][y]) == "0":
                        self.currentMap[x][y] = Background()
                        self.file_location = "media/goldensand.png"
                        self.surface = pygame.image.load(self.file_location).convert_alpha()
                    if str(self.currentMap[x][y]) == "1":
                        self.currentMap[x][y] = Background()
                        self.file_location = "media/water.png"
                        self.surface = pygame.image.load(self.file_location).convert_alpha()
                        self.currentMap[x][y].setSprite("media/water.png")
                    elif str(self.currentMap[x][y]) == "2":
                        self.currentMap[x][y] = Background()
                        self.file_location = "media/spike.png"
                        self.surface = pygame.image.load(self.file_location).convert_alpha()
                        self.currentMap[x][y].setSprite("media/spike.png")
                    elif str(self.currentMap[x][y]) == "9":
                        self.currentMap[x][y] = Background()
                        self.file_location = "media/finish.png"
                        self.surface = pygame.image.load(self.file_location).convert_alpha()
                        self.currentMap[x][y].setSprite("media/finish.png")
                except:
                    self.currentMap[x].append(Background())
                    self.currentMap[x][y].setSprite("media/goldensand.png")


    def placeTiles(self):
        # places the tiles
        for x in range(len(self.currentMap)):
            for y in range(len(self.currentMap[x])):
                self.currentMap[x][y].setX((64 * x))
                self.currentMap[x][y].setY((64 * y))

    def scaleTiles(self):
        # scales the tiles up
        for x in range(len(self.currentMap)):
            for tile in self.currentMap[x]:
                tile.setScale(2)

    def updateTiles(self, window):
        for x in range(len(self.currentMap)):
            for y in range(len(self.currentMap[x])):
                window.getScreen().blit(self.currentMap[x][y].getSurface(), self.currentMap[x][y].getPosition())


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
        self.currentMap = map

    def checkTopBorder(self, height, position, speed):
        for x in range(0, 16):
            for y in range(0, 10):
                if self.currentMap[x][y].getSprite() == "media/water.png":
                    if self.currentMap[x][y].getY() >= position[1]:
                        if self.currentMap[x][y].getY() <= (position[1] + height):
                            if position[0] + height >= self.currentMap[x][y].getX() - speed:
                                if position[0] <= self.currentMap[x][y].getX() + self.currentMap[x][y].getWidth() + \
                                        speed:
                                    return True
                else:
                    pass

    def checkBottomBorder(self, height, position, speed):
        for x in range(0, 16):
            for y in range(0, 10):
                if self.currentMap[x][y].getSprite() == "media/water.png":
                    if position[1] >= self.currentMap[x][y].getY():
                        if position[1] - (self.currentMap[x][y].getY() + self.currentMap[x][y].getHeight())<= speed:
                            if position[0] + height >= self.currentMap[x][y].getX() - speed:
                                if position[0] <= self.currentMap[x][y].getX() + self.currentMap[x][y].getWidth() + \
                                        speed:
                                    return True
                else:
                    pass

    def checkRightBorder(self, height, position, speed):
        for x in range(0, 16):
            for y in range(0, 10):
                if self.currentMap[x][y].getSprite() == "media/water.png":
                    if position[0] >= self.currentMap[x][y].getX() + self.currentMap[x][y].getWidth():
                        if position[0] - (self.currentMap[x][y].getX() + self.currentMap[x][y].getWidth()) <= speed:
                            if position[1] + height >= self.currentMap[x][y].getY() - speed:
                                if position[1] <= self.currentMap[x][y].getY() + self.currentMap[x][y].getHeight() + \
                                        speed:
                                    return True
                else:
                    pass

    def checkLeftBorder(self, height, position, speed):
        for x in range(0, 16):
            for y in range(0, 10):
                if self.currentMap[x][y].getSprite() == "media/water.png":
                    if self.currentMap[x][y].getX() >= position[0] + height:
                        if self.currentMap[x][y].getX() - (position[0] + height) <= speed:
                            if position[1] + height >= self.currentMap[x][y].getY() - speed:
                                if position[1] <= self.currentMap[x][y].getY() + self.currentMap[x][y].getHeight() + \
                                        speed:
                                    return True
                else:
                    pass

    # checks if there is a collision between water and the player on their side
    def checkSpikeCollision(self, position, width, height):
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
# TOPLAYER.checkSpikeCollision(player.getPosition(), player.getWidth(), player.getHeight()) == True:
    def checkFinish(self, position, width, height):
        for x in range(0, 16):
            for y in range(0, 10):
                if self.currentMap[x][y].getSprite() == "media/finish.png":
                    if position[0] >= self.currentMap[x][y].getX() - width \
                            and position[0] <= self.currentMap[x][y].getX() + self.currentMap[x][y].getWidth()\
                            and position[1] >= self.currentMap[x][y].getY() - height\
                            and position[1] <= self.currentMap[x][y].getY() + self.currentMap[x][y].getHeight():
                        print("yo")
                        return True
                    else:
                        pass





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
