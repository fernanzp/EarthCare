import pygame, sys
from settings import *
from levels import Level

pygame.init()
screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('EarthCare')
clock = pygame.time.Clock()
level = Level(forest_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)