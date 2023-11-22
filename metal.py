import pygame, sys
from buttons import Button

class Metal:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("Menu")
        self.BG = pygame.image.load("../EarthCare/Resourses/Backgrounds/Menu/Menu_background.png")
        self.BGG = pygame.image.load("../EarthCare/Resourses/Backgrounds/Win_lose/Victory.png")
        self.opc = None

    def get_font(self, size):
        return pygame.font.Font("../EarthCare/Resourses/Fonts/font.ttf", size)

    def run(self):
        while True:
            self.SCREEN.blit(self.BGG, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            MENU_TEXT = self.get_font(100).render("", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            catmetal = Button(image=pygame.image.load("Resourses/Trash_shop/Can/BluecanButton.png"), pos=(150, 380),
                              text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            catmetal2 = Button(image=pygame.image.load("Resourses/Trash_shop/Can/RedCanbutton.png"),
                               pos=(600, 380),
                               text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            catmetal3 = Button(image=pygame.image.load("Resourses/Trash_shop/Can/PurpleCanButton.png"),
                               pos=(1150, 380),
                               text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(50), base_color="#ffffff",
                                 hovering_color="#590a0a")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [catmetal, catmetal2, catmetal3, BACK_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "back"
                        return
                    if catmetal.checkForInput(MENU_MOUSE_POS):
                        print("jiji")
                        return
                    if catmetal2.checkForInput(MENU_MOUSE_POS):
                        print("jij")
                        return
                    if catmetal3.checkForInput(MENU_MOUSE_POS):
                        print("ji")
                        return

            pygame.display.update()

if __name__ == "__main__":
    metal = Metal()
    metal.run()