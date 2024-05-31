"""
Title: abstract my_sprite class
Author: Radin and Owen
Date-created: 5/14/2024
"""

import pygame
from my_sprite import MySprite
from background import Background
from Window import Color


class Player(MySprite):

    def __init__(self, width=200, height=200, x=500, y=500, speed=10, file="media/ninja.png"):
        MySprite.__init__(self, width, height, x, y, speed, file)
        self.file_location = file
        self.surface = pygame.Surface
        self.surface = pygame.image.load(self.file_location).convert_alpha()
        self.__health = 0
        self.takeDamageTime = 0
        self.x = x
        self.y = y

    def WASDMove(self, top_layer, pressed_keys):
        speed = self.speed
        if pressed_keys[pygame.K_d]:
            if not top_layer.checkHorizontalBorder(self.getX(), self.getY(), self.getWidth(), self.speed):
                self.x += self.speed
                if not self.image_dir_x:
                    self.surface = pygame.transform.flip(self.surface, True, False)
                    self.image_dir_x = True
            else:
                pass
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
        return self.x, self.y
        #self.updatePosition()

    def X(self):
        return self.x


    def Y(self):
        return self.y


    def updateHealth(self, new_health):
        self.__health = new_health

    def updateSpeed(self, new_speed):
        self.speed = new_speed

    def invulnerableFrames(self, tick):
        # need variable that increases each main program loop (tick)
        if tick < self.takeDamageTime + 100:
            # if the tick is less than 100 frames after the initial hit
            self.canTakeDamage = False
            if tick - self.canTakeDamage % 25 == 0:
                # if it is a multiple of 25 frames away from the initial hit, flash sprite
                self.surface = pygame.image.load("media/nothing.png").convert_alpha()
            else:
                self.surface = pygame.Surface
                self.surface = pygame.image.load(self.file_location).convert_alpha()

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


if __name__ == "__main__":
    from Window import Window

    pygame.init()
    WINDOW = Window("image sprite")
    CHARACTER = Player()
    HEALTH = healthBar(50, 10)
    CHARACTER.setScale(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        X, Y = CHARACTER.WASDMove(PRESSED_KEYS)
        print(X, Y)
        CHARACTER.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        # Outputs
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(CHARACTER.getSurface(), CHARACTER.getPosition())
        WINDOW.getScreen().blit(HEALTH.getSurface(), HEALTH.getPosition(X, Y - 20))
        WINDOW.updateFrame()
