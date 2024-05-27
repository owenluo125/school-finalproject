# test file

import pygame
from background import Background
from player import Player
from Window import Window

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("test")


    SANDLAYER = Background()

    # background sand
    SANDLAYER.createTiles(SANDLAYER.backgroundSand)
    SANDLAYER.placeTiles(SANDLAYER.backgroundSand)
    SANDLAYER.scaleTiles(SANDLAYER.backgroundSand)

    SANDLAYER.createTiles(SANDLAYER.levelFourTiles)
    SANDLAYER.placeTiles(SANDLAYER.levelFourTiles)
    SANDLAYER.scaleTiles(SANDLAYER.levelFourTiles)

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
        SANDLAYER.updateTiles(SANDLAYER.backgroundSand, WINDOW)
        SANDLAYER.updateTiles(SANDLAYER.levelFourTiles, WINDOW)
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        SANDLAYER.getSprite()
        WINDOW.updateFrame()

