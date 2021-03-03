import pygame
class snakeblock(pygame.sprite.Sprite):
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.left = self.rect.left
        self.top = self.rect.top


class snakesprite(pygame.sprite.Sprite):
    snakearray = {}

    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.length = 1
        self.snakearray = {1:snakeblock(image,position)}

    def snakegrow(self):
        if self.length < 20:
            self.length += 1
        else:
            self.length = 20

    def snakemove(self, keystring):
        if keystring == 'left':
            self.snakearray[1].left -= self.image.get_width()
        elif keystring == 'right':
            self.snakearray[1].left += self.image.get_width()
        elif keystring == 'up':
            self.snakearray[1].top -= self.image.get_height()
        elif keystring == 'down':
            self.snakearray[1].top += self.image.get_height()

    def foodcheck(self):


    def snakeupdate(self):


class foodsprite(pygame.sprite.Sprite):
    def __init__(self,image,position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()

    def foodgenarate(self):

    def foodupdate(self):


