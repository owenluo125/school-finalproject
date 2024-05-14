"""
Title: abstract my_sprite class
Author: Radin and Owen
Date-created: 5/14/2024
"""

import pygame
from my_sprite import MySprite


class Player(MySprite):
    def __init__(self, width, height, x, y, speed, file):
        MySprite.__init__(self, width=0, height=0, x=0, y=0, speed=10, file="media/ninja.png")
        self.__file_location = file
        self._surface = pygame.Surface
        self._surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__health = 0

    def WASDMove(self, pressed_keys):
        if pressed_keys[pygame.K_d]:
            self.x += self.speed
            if not self.image_dir_x:
                self.surface = pygame.transform.flip(self.surface, True, False)
                self.image_dir_x = True
        if pressed_keys[pygame.K_a]:
            self.x -= self.speed
            if self.image_dir_x:
                self.surface = pygame.transform.flip(self.surface, True, False)
                self.image_dir_x = False  # image is now looking left
        if pressed_keys[pygame.K_w]:
            self.y -= self.speed
        if pressed_keys[pygame.K_s]:
            self.y += self.speed

        self.updatePosition()

    def updateHealth(self, new_health):
        self.__health = new_health

    def updateSpeed(self, new_speed):
        self.speed = new_speed


if __name__ == "__main__":
    from Window import Window

    pygame.init()
    WINDOW = Window("image sprite")
    CHARACTER = Player(100, 100, 500, 500, 10, "media/ninja.png")
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