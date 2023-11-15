import pygame.mixer, sys
from buttons import Button

class Menu:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("../EarthCare/Resourses/Backgrounds/Menu/Menu_background.png")
        self.button_pressed = None

    def get_font(self, size):
        return pygame.font.Font("../EarthCare/Resourses/Fonts/font.ttf", size)

    '''def play(self):
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            PLAY_TEXT = self.get_font(45).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460),
                               text_input="BACK", font=self.get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()'''

    '''def options(self):
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            self.SCREEN.fill("white")
            pygame.image.load("../EarthCare/Resourses/Backgrounds/Menu/Menu_background.png")

            OPTIONS_TEXT = self.get_font(45).render("Pantalla de opciones.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            self.SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460),
                                 text_input="BACK", font=self.get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()'''

    def opciones_play(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("DIFFICULT", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            EASY_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Play Rect.png"), pos=(640, 250),
                                 text_input="EASY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            HARD_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Options Rect.png"), pos=(640, 400),
                                 text_input="HARD", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 550),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [EASY_BUTTON, HARD_BUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if EASY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.Menu_easy()
                    if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.Menu_hard()
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def Menu_easy(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("LEVELS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 60))

            LEVEL1_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Green_button.png"), pos=(640, 220),
                                   text_input="Level 1", font=self.get_font(30), base_color="#d7fcd4",
                                   hovering_color="White")
            LEVEL2_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Green_button.png"), pos=(640, 340),
                                   text_input="Level 2", font=self.get_font(30), base_color="#d7fcd4",
                                   hovering_color="White")
            LEVEL3_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Green_button.png"), pos=(640, 460),
                                   text_input="Level 3", font=self.get_font(30), base_color="#d7fcd4",
                                   hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 580),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LEVEL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                        print("Selected level: level1")
                        return "level1"
                        #pygame.quit()
                        #sys.exit()
                    if LEVEL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opciones_play()

            pygame.display.update()

    def Menu_hard(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("LEVELS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 60))

            LEVEL1_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 220),
                                   text_input="Level 1", font=self.get_font(30), base_color="#d7fcd4",
                                   hovering_color="White")
            LEVEL2_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 340),
                                   text_input="Level 2", font=self.get_font(30), base_color="#d7fcd4",
                                   hovering_color="White")
            LEVEL3_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 460),
                                   text_input="Level 3", font=self.get_font(30), base_color="#d7fcd4",
                                   hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 580),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [LEVEL1_BUTTON, LEVEL2_BUTTON, LEVEL3_BUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LEVEL1_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if LEVEL2_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if LEVEL3_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opciones_play()

            pygame.display.update()

    def menu_opciones(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("OPTIONS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            SOUND_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Play Rect.png"), pos=(640, 230),
                                  text_input="SOUND", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            LANGUAGE_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Options Rect.png"), pos=(640, 350),
                                     text_input="LANGUAGE", font=self.get_font(75), base_color="#d7fcd4",
                                     hovering_color="White")
            CHARACTER_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Options Rect.png"), pos=(640, 490),
                                      text_input="CHARACTER", font=self.get_font(75), base_color="#d7fcd4",
                                      hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [SOUND_BUTTON, LANGUAGE_BUTTON, CHARACTER_BUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.SOUND()
                    if LANGUAGE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.LANGUAGE()
                    if CHARACTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.CHARACTER()
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def SOUND(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("SOUND", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            SOUND_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Sound_button.png"), pos=(300, 400),
                                  text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            MUTE_SOUND = Button(image=pygame.image.load("Resourses/Buttons/NoSound_button.png"), pos=(1000, 400),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [SOUND_BUTTON, MUTE_SOUND, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SOUND_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.mixer.music.play(-1)
                        pygame.mixer.music.set_volume(1.0)
                    if MUTE_SOUND.checkForInput(MENU_MOUSE_POS):
                        pygame.mixer.music.stop()
                        pygame.mixer.music.set_volume(0.0)
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_opciones()

            pygame.display.update()

    def LANGUAGE(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("LANGUAGUE", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            MEX_BUTTON = Button(image=pygame.image.load("Resourses/Flags/Mex_flag.png"), pos=(210, 450),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            EUA_BUTTON = Button(image=pygame.image.load("Resourses/Flags/EUA_flag.png"), pos=(500, 450),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            '''FRA_BUTTON = Button(image=pygame.image.load("assets/flag/fraa.png"), pos=(820, 450),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            JAP_BUTTON = Button(image=pygame.image.load("assets/flag/jpp.png"), pos=(1100, 450),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")'''
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [MEX_BUTTON, EUA_BUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MEX_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if EUA_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    '''if FRA_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if JAP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()'''
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_opciones()

            pygame.display.update()

    def CHARACTER(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("CHARACTERS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            MALE_BUTTON = Button(image=pygame.image.load("Resourses/Characters/Male/idle/Plyr_H_idle.png"), pos=(400, 350),
                                 text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            FEMALE_BUTTON = Button(image=pygame.image.load("Resourses/Characters/Male/idle/Plyr_H_idle.png"), pos=(800, 350),
                                   text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Rects/Quit Rect.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [MALE_BUTTON, FEMALE_BUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if MALE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_opciones()
                    if FEMALE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_opciones()
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.menu_opciones()

            pygame.display.update()

    def menu_shop(self):
        while True:
            self.SCREEN.blit(self.BG, (0 ,0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("SHOP", True, "b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            SHOPBUTTON = Button(image=pygame.image.load("assets/button/Play Rect.png"), pos=(640, 230),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("assets/button/Quit Rect.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [SHOPBUTTON, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if SHOPBUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.main_menu()

            pygame.display.update()

    def main_menu(self):
        while True:
            self.SCREEN.blit(self.BG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            PLAY_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Rects/Play Rect.png"), pos=(640, 250),
                                text_input="PLAY", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            OPTIONS_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Rects/Options Rect.png"), pos=(640, 400),
                                    text_input="OPTIONS", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            SHOP_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Rects/Quit Rect.png"), pos=(640, 470),
                                 text_input="SHOP", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Rects/Quit Rect.png"), pos=(640, 550),
                                text_input="QUIT", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, OPTIONS_BUTTON, SHOP_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.button_pressed = "play"
                        return
                        #self.opciones_play()
                        #self.play()
                    if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.button_pressed = "options"
                        return
                        #menu_opcions()
                        #self.menu_opciones()
                    if SHOP_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.button_pressed = "shop"
                        return
                        #self.menu_shop()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def run(self):
        self.main_menu()

if __name__ == "__main__":
    menu = Menu()
    menu.run()