import pygame, sys
from pygame.locals import *

#Iniciación de pygame
pygame.init()

#Creamos la pantalla
weight, hight = 1280,720
screen = pygame.display.set_mode((weight,hight))
pygame.display.set_caption('EarthCare')

#Background
background = pygame.image.load("Backgrounds/Forest/Background_forest.png").convert()
x=0

#Bucle game
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    x_relativa = x % background.get_rect().width
    screen.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa < weight:
        screen.blit(background,(x_relativa,0))

    x -= 1
    pygame.display.update()
