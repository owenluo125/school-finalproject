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

    def __init__(self, image_file_location, x, y):
        MySprite.__init__(self, x=x, y=y)
        self.__x = x
        self.__y = y
        self.__position = (x, y)
        self.__file_location = image_file_location
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = True

    #modifier methods
    def Path(self):
        for i in range(500):



    def setScale(self, scale_x, scale_y=None):
        """
        changes the scale of the image, making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return: None
        """
        if scale_y is None:
            scale_y = scale_x
        self._surface = pygame.transform.scale(self._surface, (self.getWidth()*scale_x, self.getHeight()*scale_y))

    def setPosition(self):
        return self.position


if __name__ == "__main__":
    WINDOW = Window("First Layer")
    WINDOW.setColor(Color.BLUE)
    SAND_PATHWAY = []
    for i in range(600):
        SANDLAYER = ImageSprite("Media/goldensand.png", randint(0, 1000), randint(0, 600))
        SANDLAYER.setScale(1.4)
        SANDLAYER.setPosition()
        SAND_PATHWAY.append(SANDLAYER)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WINDOW.clearScreen()
        for SANDS in SAND_PATHWAY:
            WINDOW.getScreen().blit(SANDS.getSurface(), SANDS.getPosition())
        WINDOW.updateFrame()

