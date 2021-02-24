import pygame
class snakeblock(pygame.sprite.Sprite):
    def __init__(self, image, position):


class snakesprite(pygame.sprite.Sprite):
    def __init__(self, image, position):
        self.image = image
        self.position = position
        self.rect = self.image.get_rect()
        self.length = 1

    def snakegrow(self):
        if self.length < 20:
            self.length += 1
        else:
            self.length = 20

    def snakemove(self):



