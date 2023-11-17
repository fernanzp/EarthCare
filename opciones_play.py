import pygame, sys
from buttons import Button

class OpcionesPlay:
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

            MENU_TEXT = self.get_font(100).render("DIFFICULT", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            EASY_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Green_button.png"), pos=(640, 250),
                                 text_input="EASY", font=self.get_font(50), base_color="#ffffff",
                                 hovering_color="#0f4302")
            HARD_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 400),
                                 text_input="HARD", font=self.get_font(50), base_color="#ffffff",
                                 hovering_color="#590a0a")
            BACK_BUTTON = Button(image=pygame.image.load("../EarthCare/Resourses/Buttons/Yellow_button.png"), pos=(640, 550),
                                 text_input="BACK", font=self.get_font(50), base_color="#efa40f",
                                 hovering_color="#b57b08")

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
                        self.opc = "easy"
                        return
                    if HARD_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "hard"
                        return
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "back"
                        return

            pygame.display.update()

if __name__ == "__main__":
    opciones_play = OpcionesPlay()
    opciones_play.run()