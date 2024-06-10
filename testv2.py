# test file

import pygame
from background import Background
from player import Player, healthBar
from Window import Window, Color
from turtle import Turtle
from EndTexts import ImageSprite


if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("test")
    LOSE = ImageSprite("media/you-lose-text-with-neon.png")
    turtle = Turtle()
    turtle.createTurtles()
    turtle.placeTurtles()


    SANDLAYER = Background()
    TOPLAYER = Background()
    SANDLAYER.setMap(SANDLAYER.backgroundSand)
    TOPLAYER.setMap(TOPLAYER.levelFiveTiles)


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

    player.setPosition(TOPLAYER.levelFivePosition[0], TOPLAYER.levelFivePosition[1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        X, Y = player.WASDMove(TOPLAYER, PRESSED_KEYS)
        OriginalWidth = health.width()

        player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        # Outputs
        WINDOW.clearScreen()

        SANDLAYER.updateTiles(WINDOW)
        TOPLAYER.updateTiles(WINDOW)
        # for radin
        if TOPLAYER.checkSpikeCollision(player.getPosition(), player.getWidth(), player.getHeight()):
            health.setNewWidth(OriginalWidth - 1)
        if turtle.checkTurtleCollision(player.getPosition(), player.getWidth(), player.getHeight()):
            health.setNewWidth(OriginalWidth - 1)
        TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
        turtle.moveTurtles(WINDOW, WINDOW.getVirtualHeight())
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
        WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
        WINDOW.updateFrame()
        if health.getWidth() == 0:
            WINDOW.clearScreen()
            WINDOW.getScreen().blit(LOSE.getSurface(), LOSE.getPosition())
            WINDOW.updateFrame()



