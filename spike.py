"""
Title: spike 1
Author: Radin and Owen
Date-created: 5/15/2024
"""

import pygame
from my_sprite import MySprite


class Spike(MySprite):
    def __init__(self, width=0, height=0, x=0, y=0, speed=10, file="media/spike.png"):
        MySprite.__init__(self, width=0, height=0, x=0, y=0, speed=10, file="media/spike.png")
        self.__file_location = file
        self._surface = pygame.Surface
        self._surface = pygame.image.load(self.__file_location).convert_alpha()


if __name__ == "__main__":
    from Window import Window

    pygame.init()
    WINDOW = Window("image sprite")
    CHARACTER = Spike(100, 100, 0, 0)
    CHARACTER.setScale(5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()


        CHARACTER.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        # Outputs
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(CHARACTER.getSurface(), CHARACTER.getPosition())
        WINDOW.updateFrame()
