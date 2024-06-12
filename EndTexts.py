from my_sprite import MySprite
import pygame

class ImageSprite(MySprite):
    def __init__(self, width=200, height=200, x=500, y=500, speed=5, file="media/you-lose-text-with-neon.png"):
        MySprite.__init__(self, width, height, x, y, speed, file)
        self.file_location = file
        self.surface = pygame.Surface
        self.surface = pygame.image.load(self.file_location).convert_alpha()
        self.__health = 0
        self.takeDamageTime = 0
        self.x = x
        self.y = y
    '''
    def __init__(self, image_file_location):
        super().__init__()
        self._file_location = image_file_location
        self._surface = pygame.image.load(self._file_location).convert_alpha()
        self._image_dir_x = True

    def getSurface(self):
        return self._surface

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