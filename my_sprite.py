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

    def __init__(self, width=0, height=0, x=0, y=0, speed=10, file="ninja.png"):
        self.__width = width
        self.__height = height
        self._dimensions = (self.__width, self.__height)
        self.__x = x
        self.__y = y
        self.__position = (self.__x, self.__y)
        self.__speed = speed
        self.__dir_x = 1
        self.__dir_y = 1
        self.__file_location = file
        self._surface = pygame.Surface
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = True

    # Modifier Methods (setter methods)
    def marqueeX(self, max_x, min_x=0):
        self.__x += self.__speed

        if self.__x > max_x:
            self.__x = min_x - self._surface.get_width()

        self.__updatePosition()

    def WASDMove(self, pressed_keys):
        # polymorhpism example of modifying the WASDmove() method
        MySprite.WASDMove(self, pressed_keys)
        if pressed_keys[pygame.K_a] and self.__image_dir_x:
            # if a key is pressed and image is looking to the right
            self._surface = pygame.transform.flip(self._surface, True, False)
            self.__image_dir_x = False # image is now looking left
        if pressed_keys[pygame.K_d] and not self.__image_dir_x:
            # if d key is pressed and image is looking to the left
            self._surface = pygame.transform.flip(self._surface, True, False)
            self.__image_dir_x = True # image is now looking to the right

        self.__updatePosition()

    def setSpeed(self, new_speed):
        self.__speed = new_speed

    def setColor(self, new_color):
        """
        This only changes the variable, it does not change the surface
        :param new_color: Tuple
        :return: None
        """
        self._color = new_color


    def setX(self, x):
        self.__x = x
        self.__updatePosition()

    def setY(self, y):
        self.__y = y
        self.__updatePosition()

    def setPosition(self, x, y):
        self.__x = x
        self.__y = y
        # self.__position = (self.__x, self.__y)
        self.__updatePosition()

    def __updatePosition(self):
        self.__position = (self.__x, self.__y)

    # Accessor Methods (getter methods)
    def getSurface(self):
        return self._surface

    def getPosition(self):
        return self.__position

    def getWidth(self):
        return self._surface.get_width()

    def getHeight(self):
        return self._surface.get_height()

    def stopAtEdge(self, max_width, max_height, min_width=0, min_height=0):
        if self.__x > max_width - self._surface.get_width():
            self.__x = max_width - self._surface.get_width()
        if self.__x < min_width:
            self.__x = min_width

        if self.__y > max_height - self._surface.get_height():
            self.__y = max_height - self._surface.get_height()
        if self.__y < min_height:
            self.__y = min_height

        self.__position = (self.__x, self.__y)

    def bounceX(self, MAX_WIDTH):
        """
        Text will bounce back and forth on the borders
        :param MAX_WIDTH: int
        :return:
        """
        self.__x += self.__speed * self.__dir_x
        if self.__x > MAX_WIDTH - self._surface.get_width():
            self.__x = MAX_WIDTH - self._surface.get_width()
            self.__dir_x = -1
        elif self.__x < 0:
            self.__x = 0
            self.__dir_x = 1
        self.__position = (self.__x, self.__y)

    def bounceY(self, MAX_HEIGHT):
        """
        Text will bounce back and forth on the borders
        :param MAX_HEIGHT: int
        :return:
        """
        self.__y += self.__speed * self.__dir_y
        if self.__y > MAX_HEIGHT - self._surface.get_height():
            self.__y = MAX_HEIGHT - self._surface.get_height()
            self.__dir_y = -1
        elif self.__y < 0:
            self.__y = 0
            self.__dir_y = 1
        self.__position = (self.__x, self.__y)

    def isCollision(self, width, height, position):
        """
        use the width, height and position of an external sprite to test if it is colliding with the given sprite
        :param width: int
        :param height: int
        :param position: tuple
        :return: None
        """

        if position[0] >= self.__x - width and position[0] <= self.__x + self.getWidth() and \
            position[1] >= self.__y - height and position[1] <= self.__y + self.getHeight():
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
        self._surface = pygame.transform.scale(self._surface, (self.getWidth()*scale_x, self.getHeight()*scale_y))


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