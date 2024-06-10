# test file

import pygame
from background import Background
from player import Player, healthBar
from Window import Window, Color
from turtle import Turtle


if __name__ == "__main__":
    pygame.init()
    WINDOW = Window("test")
    while True:
        # show start screenssssss
        break

    while True:
        SANDLAYER = Background()
        TOPLAYER = Background()
        SANDLAYER.setMap(SANDLAYER.backgroundSand)
        TOPLAYER.setMap(TOPLAYER.levelOneTiles)


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

        player.setPosition(TOPLAYER.levelOnePosition[0], TOPLAYER.levelOnePosition[1])

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
            TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
            WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
            WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
            WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
            WINDOW.updateFrame()

            if TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight()):
                break
        break

    while True:
        SANDLAYER = Background()
        TOPLAYER = Background()
        SANDLAYER.setMap(SANDLAYER.backgroundSand)
        TOPLAYER.setMap(TOPLAYER.levelTwoTiles)

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

        player.setPosition(TOPLAYER.levelTwoPosition[0], TOPLAYER.levelTwoPosition[1])

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
            TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
            WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
            WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
            WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
            WINDOW.updateFrame()

            if TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight()):
                break
        break

    while True:
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
        health = healthBar(50, 10)

        healthFrame = healthBar(50, 10)
        healthFrame.setScale(1.0, 1.0)
        healthFrame.setColor(Color.GREY)

        player.setPosition(TOPLAYER.levelThreePosition[0], TOPLAYER.levelThreePosition[1])

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
            TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
            WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
            WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
            WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
            WINDOW.updateFrame()

            if TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight()):
                break
        break

    while True:
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

            player.stopAtEdge(WINDOW.getVirtualWidth(), WINDOW.getVirtualHeight(), 0)

            # Outputs
            WINDOW.clearScreen()

            SANDLAYER.updateTiles(WINDOW)
            TOPLAYER.updateTiles(WINDOW)
            # for radin
            if TOPLAYER.checkSpikeCollision(player.getPosition(), player.getWidth(), player.getHeight()):
                health.setNewWidth(OriginalWidth - 1)
            TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
            WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
            WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
            WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
            WINDOW.updateFrame()

            if TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight()):
                break
        break

    while True:
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

        turtle = Turtle()
        turtle.createTurtles()
        turtle.placeTurtles()

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
            turtle.moveTurtles(WINDOW, WINDOW.getVirtualHeight())
            # for radin
            if TOPLAYER.checkSpikeCollision(player.getPosition(), player.getWidth(), player.getHeight()):
                health.setNewWidth(OriginalWidth - 1)
            if turtle.checkTurtleCollision(player.getPosition(), player.getWidth(), player.getHeight()):
                health.setNewWidth(OriginalWidth - 1)
            TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
            WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
            WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
            WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
            WINDOW.updateFrame()

            if TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight()):
                break
        break

    while True:
        SANDLAYER = Background()
        TOPLAYER = Background()
        SANDLAYER.setMap(SANDLAYER.backgroundSand)
        TOPLAYER.setMap(TOPLAYER.levelSixTiles)

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

        turtle = Turtle()
        turtle.createTurtles()
        turtle.placeTurtles()

        player.setPosition(TOPLAYER.levelSixPosition[0], TOPLAYER.levelSixPosition[1])

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
            turtle.moveTurtles(WINDOW, WINDOW.getVirtualHeight())
            # for radin
            if TOPLAYER.checkSpikeCollision(player.getPosition(), player.getWidth(), player.getHeight()):
                health.setNewWidth(OriginalWidth - 1)
            if turtle.checkTurtleCollision(player.getPosition(), player.getWidth(), player.getHeight()):
                health.setNewWidth(OriginalWidth - 1)
            TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight())
            WINDOW.getScreen().blit(player.getSurface(), player.getPosition())
            WINDOW.getScreen().blit(healthFrame.getSurface(), healthFrame.getPosition(X - 5, Y - 20))
            WINDOW.getScreen().blit(health.getSurface(), health.getPosition(X - 5, Y - 20))
            WINDOW.updateFrame()

            if TOPLAYER.checkFinish(player.getPosition(), player.getWidth(), player.getHeight()):
                break
        break