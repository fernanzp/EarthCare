import pygame.mixer, sys
from settings import *
from forest_easy import Level_f_1
from forest_hard import Level_f_2
from city_easy import Level_c_1
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((weight, height))
pygame.display.set_caption('EarthCare')
clock = pygame.time.Clock()
menu = Menu()
forest_easy_ = Level_f_1(forest_map, screen)
forest_hard_ = Level_f_2(forest_map_hard, screen)
city_easy_ = Level_c_1(city_map, screen)

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
        if menu.play_button_pressed:
            current_screen = "level"
            menu_sound.stop()
            forest_sound.play(-1)
            forest_sound.set_volume(0.5)
    if current_screen == "level":
        forest_easy_.run()

    pygame.display.update()
    clock.tick(60)