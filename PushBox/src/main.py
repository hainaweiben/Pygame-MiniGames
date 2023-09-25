import pygame
import sys
from pygame.locals import *
from game import *
import const

pygame.init()
DISPLAYSURF = pygame.display.set_mode((const.GAME_WIDTH_SIZE, const.GAME_HEIGHT_SIZE))
gameRen = Game(DISPLAYSURF, (100, 100), const.ControlType.REN)
gameJi = Game(DISPLAYSURF, (100, 600), const.ControlType.JI)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    gameRen.update()
    gameJi.update()
    DISPLAYSURF.fill((0, 0, 0))
    gameRen.draw()
    gameJi.draw()
    if gameJi.level.level > gameRen.level.level:
        image = pygame.image.load("res/lose.png")
        image_rect = image.get_rect(center=(const.GAME_WIDTH_SIZE // 2, const.GAME_HEIGHT_SIZE // 2))
        DISPLAYSURF.blit(image, image_rect)
    pygame.display.update()
