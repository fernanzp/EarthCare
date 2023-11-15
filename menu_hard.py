import pygame, sys
from buttons import Button

class Menu_hard:
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

if __name__ == "__main__":
    menu_hard = Menu_hard()
    menu_hard.run()