import pygame, sys
from settings import *
from levels import Level

pygame.init()

screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('EarthCare')
clock = pygame.time.Clock()
level = Level(forest_map, screen)
run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()

    #Exit the game with escape
    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        run = False

    #screen.fill('black')   "Fondo negro" eliminar despues
    level.run()

    pygame.display.update()
    clock.tick(60)