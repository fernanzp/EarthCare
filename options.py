import pygame, sys
from buttons import Button

class Options:
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

            MENU_TEXT = self.get_font(100).render("OPTIONS", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            SOUND_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Green_button.png"), pos=(640, 230),
                                  text_input="SOUND", font=self.get_font(50), base_color="#ffffff", hovering_color="#0f4302")
            LANGUAGE_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Buttons/Red_button_big.png"), pos=(640, 350),
                                     text_input="LANGUAGE", font=self.get_font(50), base_color="#ffffff",
                                     hovering_color="#590a0a")
            CHARACTER_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Buttons/Yellow_button_big.png"), pos=(640, 490),
                                      text_input="CHARACTER", font=self.get_font(50), base_color="#efa40f",
                                      hovering_color="#b57b08")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(50), base_color="#ffffff", hovering_color="#590a0a")

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
                        self.opc = "sound"
                        return
                    if LANGUAGE_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "language"
                        return
                    if CHARACTER_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "character"
                        return
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "back"
                        return

            pygame.display.update()

if __name__ == "__main__":
    options = Options()
    options.run()