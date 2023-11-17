import pygame.mixer, sys
from settings import *
from forest_easy import Level_f_1
from forest_hard import Level_f_2
from city_easy import Level_c_1
from city_hard import Level_c_2
from beach_easy import Level_b_1
from beach_hard import Level_b_2

from menu import Menu
from opciones_play import OpcionesPlay
from options import Options
from menu_easy import Menu_easy
from menu_hard import Menu_hard
from sound import Sound
from language import Language
from chng_character import Chng_character

pygame.init()

screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('EarthCare')
clock = pygame.time.Clock()
forest_easy_ = Level_f_1(forest_map, screen)
forest_hard_ = Level_f_2(forest_map_hard, screen)
city_easy_ = Level_c_1(city_map, screen)
city_hard_ = Level_c_2(city_map_hard, screen)
beach_easy_ = Level_b_1(beach_map, screen)
beach_hard_ = Level_b_2(beach_map_hard, screen)

menu = Menu()
opciones_play = OpcionesPlay()
options = Options()
menu_easy = Menu_easy()
menu_hard = Menu_hard()
sound = Sound()
language = Language()
chng_character = Chng_character()



run = True
current_screen = "menu"

pygame.mixer.init()
menu_sound = pygame.mixer.Sound('Resourses/sfx/inicio.mpeg')
forest_sound = pygame.mixer.Sound('Resourses/sfx/forest_level_sound.wav')
city_sound = pygame.mixer.Sound('Resourses/sfx/city_level_sound.wav')
beach_sound = pygame.mixer.Sound('Resourses/sfx/beach_level_sound.wav')

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

        elif menu.button_pressed == "options":
            current_screen = "options"

        elif menu.button_pressed == "shop":
            pygame.quit()
            sys.exit()

    elif current_screen == "opciones_play":
        opciones_play.run()

        if opciones_play.opc == "easy":
            menu_easy.run()

            if menu_easy.opc == "level1":
                menu_sound.stop()
                forest_sound.play(-1)
                forest_sound.set_volume(0.5)
                current_screen = "level1_easy"

            elif menu_easy.opc == "level2":
                menu_sound.stop()
                beach_sound.play(-1)
                beach_sound.set_volume(0.5)
                current_screen = "level2_easy"

            elif menu_easy.opc == "level3":
                menu_sound.stop()
                city_sound.play(-1)
                city_sound.set_volume(0.5)
                current_screen = "level3_easy"

            elif menu_easy.opc == "back":
                current_screen = "opciones_play"

        elif opciones_play.opc == "hard":
            menu_hard.run()

            if menu_hard.opc == "level1":
                menu_sound.stop()
                forest_sound.play(-1)
                forest_sound.set_volume(0.5)
                current_screen = "level1_hard"

            elif menu_hard.opc == "level2":
                menu_sound.stop()
                beach_sound.play(-1)
                beach_sound.set_volume(0.5)
                current_screen = "level2_hard"

            elif menu_hard.opc == "level3":
                menu_sound.stop()
                city_sound.play(-1)
                city_sound.set_volume(0.5)
                current_screen = "level3_hard"

            elif menu_hard.opc == "back":
                current_screen = "opciones_play"

        elif opciones_play.opc == "back":
            menu_sound.stop()
            current_screen = "menu"

    elif menu.button_pressed == "options":
        options.run()

        if options.opc == "sound":
            sound.run()
            if sound.opc == "back":
                current_screen = "options"
        elif options.opc == "language":
            language.run()
            if language.opc == "back":
                current_screen = "options"
        elif options.opc == "character":
            chng_character.run()
        elif options.opc == "back":
            menu_sound.stop()
            current_screen = "menu"

    elif current_screen == "level1_easy":
        forest_easy_.run()
        if forest_easy_.opc == "menu":
            forest_easy_.opc = None
            forest_sound.stop()
            current_screen = "menu"
        elif forest_easy_.opc == "retry":
            forest_easy_.opc = None
            current_screen = "level1_easy"
        elif forest_easy_.opc == "next":
            current_screen = "level2_easy"

    elif current_screen == "level2_easy":
        beach_easy_.run()
        if beach_easy_.opc == "menu":
            beach_easy_.opc = None
            beach_sound.stop()
            current_screen = "menu"
        elif beach_easy_.opc == "retry":
            beach_easy_.opc = None
            current_screen = "level2_easy"
        elif beach_easy_.opc == "next":
            beach_sound.stop()
            current_screen = "level3_easy"

    elif current_screen == "level3_easy":
        city_easy_.run()
        if city_easy_.opc == "menu":
            city_easy_.opc = None
            city_sound.stop()
            current_screen = "menu"
        elif city_easy_.opc == "retry":
            city_easy_.opc = None
            current_screen = "level3_easy"

    elif current_screen == "level1_hard":
        forest_hard_.run()
        if forest_hard_.opc == "menu":
            forest_hard_.opc = None
            forest_sound.stop()
            current_screen = "menu"
        elif forest_hard_.opc == "retry":
            forest_hard_.opc = None
            current_screen = "level1_hard"
        elif forest_hard_.opc == "next":
            forest_sound.stop()
            current_screen = "level2_hard"
    elif current_screen == "level2_hard":
        beach_hard_.run()
        if beach_hard_.opc == "menu":
            beach_hard_.opc = None
            beach_sound.stop()
            current_screen = "menu"
        elif beach_hard_.opc == "retry":
            beach_hard_.opc = None
            current_screen = "level2_hard"
        elif beach_hard_.opc == "next":
            beach_sound.stop()
            current_screen = "level3_hard"
    elif current_screen == "level3_hard":
        city_hard_.run()
        if city_hard_.opc == "menu":
            city_hard_.opc = None
            city_sound.stop()
            current_screen = "menu"
        elif city_hard_.opc == "retry":
            city_hard_.opc = None
            current_screen = "level3_hard"

    pygame.display.update()
    clock.tick(60)