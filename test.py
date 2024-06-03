# test file

import pygame
from background import Background
from player import Player
from Window import Window, Color

class healthBar():
    global Player, X, Y

    def __init__(self, width=1, height=1, x=500, y=480):
        self.__width = width
        self.__height = height
        self.__dimensions = (self.__width, self.__height)
        self._x = x
        self._y = y
        self.__updatePosition = (self._x, self._y)
        self.__color = Color.RED
        self.__surface = pygame.Surface(self.__dimensions, pygame.SRCALPHA, 32)
        self.__surface.fill(self.__color)

    def getSurface(self):
        return self.__surface

    def getPosition(self, x, y):
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        return self.position

    def setColor(self, color):
        self.__color = color
        self.__surface.fill(self.__color)


    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def setScale(self, scale_x, scale_y):
        """
        changes the scale of the image, making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return: None
        """
        if scale_y is None:
            scale_y = scale_x
        self.__surface = pygame.transform.scale(self.__surface, (self.getWidth()*scale_x, self.getHeight()*scale_y))



if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("test")


    SANDLAYER = Background()
    TOPLAYER = Background()
    SANDLAYER.setMap(SANDLAYER.backgroundSand)
    TOPLAYER.setMap(TOPLAYER.levelThreeTiles)


    # background sand
    SANDLAYER.createTiles()
    SANDLAYER.placeTiles()
    SANDLAYER.scaleTiles()

    TOPLAYER.createTiles()
    TOPLAYER.placeTiles()
    TOPLAYER.scaleTiles()


    player = Player()
    health = healthBar(50, 10)


    healthFrame = healthBar(50, 10)
    healthFrame.setScale(1.0, 1.0)
    healthFrame.setColor(Color.GREY)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        X, Y = player.WASDMove(TOPLAYER, PRESSED_KEYS)

        player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        # Outputs
        WINDOW.clearScreen()

        SANDLAYER.updateTiles(WINDOW)
        TOPLAYER.updateTiles(WINDOW)
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X, Y - 20))
        WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X, Y - 20))
        WINDOW.updateFrame()

