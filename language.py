import pygame, sys
from buttons import Button

class Language:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("../EarthCare/Resourses/Backgrounds/Menu/Menu_background.png")
        self.opc = None

    def get_font(self, size):
        return pygame.font.Font("../EarthCare/Resourses/Fonts/font.ttf", size)

    def run(self):
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
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(50), base_color="#ffffff", hovering_color="#590a0a")

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
                        self.opc = "back"
                        return

            pygame.display.update()

if __name__ == "__main__":
    language = Language()
    language.run()