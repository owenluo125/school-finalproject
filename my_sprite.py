"""
Title: abstract my_sprite class
Author: Radin and Owen
Date-created: 5/14/2024
"""

import pygame


class MySprite:
    """
    Abstract sprite class to build other sprites
    """

    def __init__(self, width=0, height=0, x=0, y=0, speed=10, file="media/ninja.png"):
        self.__width = width
        self.__height = height
        self._dimensions = (self.__width, self.__height)
        self.x = x
        self.y = y
        self.position = (self.x, self.y)
        self.speed = speed
        self.dir_X = 1
        self.dir_Y = 1
        self.__file_location = file
        self.surface = pygame.Surface
        self.surface = pygame.image.load(self.__file_location).convert_alpha()
        self.image_dir_x = True

    # Modifier Methods (setter methods)
    def marqueeX(self, max_x, min_x=0):
        self.x += self.speed

        if self.x > max_x:
            self.x = min_x - self.surface.get_width()

        self.updatePosition()

    def setSpeed(self, new_speed):
        self.speed = new_speed

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

    # Accessor Methods (getter methods)
    def getSurface(self):
        return self.surface

    def getPosition(self):
        return self.position

    def getWidth(self):
        return self.surface.get_width()

    def getHeight(self):
        return self.surface.get_height()

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self.x > max_width - self.surface.get_width():
            self.x = max_width - self.surface.get_width()
        if self.x < min_width:
            self.x = min_width

        if self.y > max_height - self.surface.get_height():
            self.y = max_height - self.surface.get_height()
        if self.y < min_height:
            self.y = min_height

        self.position = (self.x, self.y)

    def bounceX(self, MAX_WIDTH):
        """
        Text will bounce back and forth on the borders
        :param MAX_WIDTH: int
        :return:
        """
        self.x += self.speed * self.dir_X
        if self.x > MAX_WIDTH - self.surface.get_width():
            self.x = MAX_WIDTH - self.surface.get_width()
            self.dir_X = -1
        elif self.x < 0:
            self.x = 0
            self.dir_X = 1
        self.position = (self.x, self.y)

    def bounceY(self, MAX_HEIGHT):
        """
        Text will bounce back and forth on the borders
        :param MAX_HEIGHT: int
        :return:
        """
        self.y += self.speed * self.dir_Y
        if self.y > MAX_HEIGHT - self.surface.get_height():
            self.y = MAX_HEIGHT - self.surface.get_height()
            self.dir_Y = -1
        elif self.y < 0:
            self.y = 0
            self.dir_Y = 1
        self.position = (self.x, self.y)

    def isCollision(self, width, height, position):
        """
        use the width, height and position of an external sprite to test if it is colliding with the given sprite
        :param width: int
        :param height: int
        :param position: tuple
        :return: None
        """

        if position[0] >= self.x - width and position[0] <= self.x + self.getWidth() and \
            position[1] >= self.y - height and position[1] <= self.y + self.getHeight():
            return True
        else:
            return False

    def setScale(self, scale_x, scale_y=None):
        """
        changes the scale of the image, making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return:
        """
        if scale_y is None:
            scale_y = scale_x
        self.surface = pygame.transform.scale(self.surface, (self.getWidth()*scale_x, self.getHeight()*scale_y))



if __name__ == "__main__":
    from Window import Window

    pygame.init()
    WINDOW = Window("image sprite")
    CHARACTER = MySprite(100, 100, 500, 500, 10, "media/ninja.png")
    CHARACTER.setScale(0.5)
    offset_y = 70

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        CHARACTER.WASDMove(PRESSED_KEYS)

        CHARACTER.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0, offset_y)

        # Outputs
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(CHARACTER.getSurface(), CHARACTER.getPosition())
        WINDOW.updateFrame()