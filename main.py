import pygame, sys
from pygame.locals import *

#Iniciación de pygame
pygame.init()

#Creamos la pantalla
weight, hight = 1280,720 #Variables para definir el ancho y el alto de la pantalla
screen = pygame.display.set_mode((weight,hight))
pygame.display.set_caption('EarthCare') #Nombre del juego
run = True

#set framerate
clock = pygame.time.Clock()
fps = 60

#Background
background = pygame.image.load('Resourses/Backgrounds/Forest/Background_forest.png').convert() #Creamos el fondo
x=0

#Datos personajes
class players(pygame.sprite.Sprite):
    def __init__(self, x, y, velocidad):
        pygame.sprite.Sprite.__init__(self)
        self.velocidad = velocidad
        self.direction = 1
        self.flip = False
        quieto = pygame.image.load('Resourses/Characters/Personaje_H.png')
        self.scale = pygame.transform.scale(quieto, (int(quieto.get_width()), int(quieto.get_height())))
        self.rect = quieto.get_rect()
        self.rect.center = (x, y)

    def move(self, izquierda, derecha):
        #Reset movement variables
        dx = 0
        dy = 0

        #Assign movement variables if moving left or right
        if izquierda:
            dx = -self.velocidad
            self.flip = True
            self.direction = -1
        if derecha:
            dx = self.velocidad
            self.flip = False
            self.direction = 1

        #Update rectangle position
        self.rect.x += dx
        self.rect.y += dy
    def draw(self):
        screen.blit(pygame.transform.flip(self.scale, self.flip, False), self.rect)

player_h = players(200,650,4)

#Definimos las variables de accion de los player
izquierda = False
derecha = False

#Bucle game
while run:
    clock.tick(fps)
    for event in pygame.event.get():
        #Quit game
        if event.type == QUIT:
            run = False
            pygame.quit()
            sys.exit()

        #Keyboard presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                izquierda =True
            if event.key == pygame.K_d:
                derecha = True
            if event.key == pygame.K_LEFT:
                izquierda = True
            if event.key == pygame.K_RIGHT:
                derecha = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #Keyboard button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                izquierda = False
            if event.key == pygame.K_d:
                derecha = False
            if event.key == pygame.K_LEFT:
                izquierda = False
            if event.key == pygame.K_RIGHT:
                derecha = False

    #Fondo movimiento
    x_relativa = x % background.get_rect().width
    screen.blit(background, (x_relativa - background.get_rect().width, 0))
    if x_relativa < weight:
        screen.blit(background,(x_relativa,0))
    x -= 1

    player_h.draw()
    player_h.move(izquierda, derecha)

    pygame.display.update()