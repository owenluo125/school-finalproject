# test file

import pygame
from background import Background
from player import Player, healthBar
from Window import Window, Color


if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("test")


    SANDLAYER = Background()
    TOPLAYER = Background()
    SANDLAYER.setMap(SANDLAYER.backgroundSand)
    TOPLAYER.setMap(TOPLAYER.levelFourTiles)


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

    player.setPosition(TOPLAYER.levelFourPosition[0], TOPLAYER.levelFourPosition[1])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        X, Y = player.WASDMove(TOPLAYER, PRESSED_KEYS)
        OriginalWidth = health.width()
        print(OriginalWidth)

        if PRESSED_KEYS[pygame.K_r]:
            health.setNewWidth(OriginalWidth - 5)


        player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        # Outputs
        WINDOW.clearScreen()

        SANDLAYER.updateTiles(WINDOW)
        TOPLAYER.updateTiles(WINDOW)
        # for radin
        TOPLAYER.checkSpikeCollision(player.getPosition(), player.getWidth(), player.getHeight())
        TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
        WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
        WINDOW.updateFrame()

