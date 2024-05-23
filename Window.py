"""
Title: Windows
Author: Radin and Owen
Date-created: 5/13/2024
"""
import pygame

class Color:
    WHITE = (255, 255, 255)
    GREY = (50, 50, 50)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (55, 118, 171)
    ORANGE = (255, 145, 0)
    PURPLE = (175, 25, 255)
    YELLOW = (225, 225, 30)


class Window:
    """
    Create the window that will load for pygame
    :return: None
    """

    def __init__(self, title, width=1024, height=640, fps=30):
        # text that appears in the title bar
        self.__title = title
        # width of the window frame
        self.__width = width
        # height of the window frame
        self.__height = height
        # window dimensions
        self.__dimension = (self.__width, self.__height)
        # frames per second
        self.__fps = fps
        # background color
        self.__bg_color = Color.BLUE
        # clock object that tracks time
        self.__clock = pygame.time.Clock()
        # base surface that all surfaces are overlaid on top
        self.__screen = pygame.display.set_mode(self.__dimension)
        # colors the screen surface
        self.__screen.fill(self.__bg_color)
        # sets the window caption with the title
        pygame.display.set_caption(self.__title)

    # Modifier Methods
    def updateFrame(self):
        """
        This updates the window object based on the fps
        :return:
        """
        # waits the appropriate amount of time based on FPS before finishing the loop
        self.__clock.tick(self.__fps)
        # updates the computer screen with the new frame
        pygame.display.flip()

    def clearScreen(self):
        """
        Fill the screen with the background color
        :return:
        """
        self.__screen.fill(self.__bg_color)


    def setColor(self, color):
        self._color = color
        self.__screen.fill(self._color)

    # Accessor Methods
    def getScreen(self):
        return self.__screen

    def getVirtualWidth(self):
        return self.__width

    def getVirtualHeight(self):
        return self.__height


if __name__ == "__main__":
    pygame.init()

    WINDOW = Window("template")
    WINDOW.setColor(Color.BLUE)

    while True:
        # pygame retrieves all inputs
        for event in pygame.event.get():
            # checks if the window is closed
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        WINDOW.getScreen()
        WINDOW.updateFrame()