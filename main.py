import sys

import pygame
import cfg

screen = pygame.display.set_mode(cfg.ScreenInfo, None)

def gameinit():
    pygame.display.init()
    screen.fill(0)

def SnakeMain():
    gameinit()
    gamerunning = True
    clock = pygame.time.Clock()
    image_back = cfg.imageLib['back']

    while gamerunning:
        screen.fill(0)
        screen.blit(image_back)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        clock.tick(cfg.FPS)
        pygame.display.update()


if __name__ == '__main__':
    SnakeMain()