import sys
import gameclass
import pygame
import cfg

screen = pygame.display.set_mode((cfg.ScreenInfo[0], cfg.ScreenInfo[1]))

def gameinit():
    pygame.display.init()
    screen.fill(0)

def SnakeMain(img_snake=None):
    gameinit()
    gamerunning = True
    clock = pygame.time.Clock()
    img_back = pygame.image.load(cfg.imageLib['back'])
    img_apple = pygame.image.load(cfg.imageLib['apple'])
    img_snake = pygame.image.load(cfg.imageLib['snake'])
    img_win = pygame.image.load(cfg.imageLib['youwin'])
    img_over = pygame.image.load(cfg.imageLib['gameover'])

    while gamerunning:
        screen.fill(0)
        for i in range(0, cfg.ScreenInfo[0], img_back.get_width()):
            for k in range(0, cfg.ScreenInfo[1], img_back.get_height()):
                screen.blit(img_back, (i, k))

        snake = gameclass.snakesprite(img_snake, (cfg.ScreenInfo[0]/2, cfg.ScreenInfo[1]/2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_a] or keypressed[pygame.K_LEFT]:
            snake.snakemove('left')
        elif keypressed[pygame.K_d] or keypressed[pygame.K_RIGHT]:
            snake.snakemove('right')
        elif keypressed[pygame.K_w] or keypressed[pygame.K_UP]:
            snake.snakemove('up')
        elif keypressed[pygame.K_s] or keypressed[pygame.K_DOWN]:
            snake.snakemove('down')

        snake.foodcheck()

        snake.snakeupdate()

        clock.tick(cfg.FPS)
        pygame.display.update()


if __name__ == '__main__':
    SnakeMain()