# test file

import pygame
from background import Background
from player import Player
from Window import Window

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

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        player.WASDMove(PRESSED_KEYS)

        player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        # Outputs
        WINDOW.clearScreen()

        SANDLAYER.updateTiles(WINDOW)
        TOPLAYER.updateTiles(WINDOW)
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        WINDOW.updateFrame()

