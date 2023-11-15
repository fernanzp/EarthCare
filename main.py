import pygame.mixer, sys
from settings import *
from forest_easy import Level_f_1
from forest_hard import Level_f_2
from city_easy import Level_c_1

from menu import Menu
from opciones_play import OpcionesPlay
from options import Options
from menu_easy import Menu_easy
from menu_hard import Menu_hard

pygame.init()

screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('EarthCare')
clock = pygame.time.Clock()
forest_easy_ = Level_f_1(forest_map, screen)
forest_hard_ = Level_f_2(forest_map_hard, screen)
city_easy_ = Level_c_1(city_map, screen)

menu = Menu()
opciones_play = OpcionesPlay()
options = Options()
menu_easy = Menu_easy()
menu_hard = Menu_hard()

run = True
current_screen = "menu"

pygame.mixer.init()
menu_sound = pygame.mixer.Sound('Resourses/sfx/inicio.mpeg')
forest_sound = pygame.mixer.Sound('Resourses/sfx/forest_level_sound.wav')

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

    if current_screen == "menu":
        menu_sound.play(-1)
        menu_sound.set_volume(0.5)
        menu.run()

        if menu.button_pressed == "play":
            current_screen = "opciones_play"
            opciones_play.run()
            if opciones_play.opc == "easy":
                menu_easy.run()
                if menu_easy.opc == "level1":
                    menu_sound.stop()
                    forest_sound.play(-1)
                    forest_sound.set_volume(0.5)
                    current_screen = "level1"
            elif opciones_play.opc == "hard":
                menu_hard.run()
            elif opciones_play.opc == "back":
                menu_sound.stop()
                current_screen = "menu"

        elif menu.button_pressed == "options":
            options.run()

        elif menu.button_pressed == "shop":
            pygame.quit()
            sys.exit()

    if current_screen == "level1":
        forest_easy_.run()

    pygame.display.update()
    clock.tick(60)