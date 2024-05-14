"""
Title: Background Generator
Author: Radin and Owen
Date-Created: 5/14/2024
"""

from Window import Color
from Window import Window
from my_sprite import MySprite
import pygame

class ImageSprite(MySprite):

    def __init__(self, image_file_location):
        MySprite.__init__(self)
        self.__file_location = image_file_location
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = True

    # modifier methods

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

#class Base1:

if __name__ == "__main__":
    WINDOW = Window("First Layer")
    WINDOW.setColor(Color.BLUE)
    SANDLAYER = ImageSprite("media/goldensand.png")
    SANDLAYER.setScale(1.4)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        WINDOW.clearScreen()
        WINDOW.getScreen().blit(SANDLAYER.getSurface(), SANDLAYER.getPosition())
        WINDOW.updateFrame()

