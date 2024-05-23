# test file

import pygame
from spike_1 import spikeOne
from player import Player
from Window import Window

if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("test")

    player = Player()

    spike_1 = spikeOne()
    spike_1.setScale(2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        PRESSED_KEYS = pygame.key.get_pressed()

        # Processing
        player.WASDMove(PRESSED_KEYS)

        player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

        if spike_1.isCollision(player.getWidth(), player.getHeight(), player.getPosition()):
            print("yes")


        if PRESSED_KEYS[pygame.K_SPACE]:
            oldX = player.x
            oldY = player.y
            player.setPosition(oldX, oldY)
            player.surface = pygame.image.load("media/nothing.png").convert_alpha()

        else:
            oldX = player.x
            oldY = player.y
            player.surface = pygame.image.load(player.file_location).convert_alpha()
            player.setPosition(oldX, oldY)


        # Outputs
        WINDOW.clearScreen()
        WINDOW.getScreen().blit(spike_1.getSurface(), spike_1.getPosition())
        WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
        WINDOW.updateFrame()

