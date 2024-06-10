from my_sprite import MySprite
import pygame

class ImageSprite(MySprite):

    def __init__(self, image_file_location):
        MySprite.__init__(self)
        self.__file_location = image_file_location
        self.__surface = pygame.image.load(self.__file_location).convert_alpha()
        self.__image_dir_x = True

    # modifier methods

    def setScale(self, scale_x, scale_y=None):
        """
        changes the scale of the image, making it bigger or smaller
        :param scale_x: float
        :param scale_y: float
        :return: None
        """
        if scale_y is None:
            scale_y = scale_x
        self._surface = pygame.transform.scale(self.__surface, (self.getWidth()*scale_x, self.getHeight()*scale_y))

'''
if __name__ == "__main__":

    from Window import Window
    import pygame

    LOSE = ImageSprite("media/you-lose-text-with-neon.png")
    pygame.init()

    Window = Window("template")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        Window.getScreen().blit(LOSE.getSurface(), LOSE.getPosition())
        Window.updateFrame()

'''