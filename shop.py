import pygame, sys
from buttons import Button

class Shop:
    def __init__(self):
        pygame.init()
        self.SCREEN = pygame.display.set_mode((1280, 720))
        pygame.display.set_caption("SHOP")
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

            organic = Button(image=pygame.image.load("Resourses/Trash_shop/Category/Category4.png"), pos=(100, 100),
                             text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            glass = Button(image=pygame.image.load("Resourses/Trash_shop/Category/Category3.png"), pos=(210, 100),
                           text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            metal = Button(image=pygame.image.load("Resourses/Trash_shop/Category/Category2.png"), pos=(320, 100),
                           text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            papel = Button(image=pygame.image.load("Resourses/Trash_shop/Category/Category1.png"), pos=(430, 100),
                           text_input="", font=self.get_font(50), base_color="#ffffff", hovering_color="#efa40f")
            back_button = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(50), base_color="#ffffff",
                                 hovering_color="#590a0a")

            self.SCREEN.blit(MENU_TEXT, MENU_RECT)

            for button in [organic, glass, metal, papel, back_button]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if organic.checkForInput(MENU_MOUSE_POS):
                        self.opc = "organic"
                        return
                    if glass.checkForInput(MENU_MOUSE_POS):
                        self.opc = "glass"
                        return
                    if metal.checkForInput(MENU_MOUSE_POS):
                        self.opc = "metal"
                        return
                    if papel.checkForInput(MENU_MOUSE_POS):
                        self.opc = "papel"
                        return
                    if back_button.checkForInput(MENU_MOUSE_POS):
                        self.opc = "back"
                        return

            pygame.display.update()
if __name__ == "__main__":
    shop = Shop()
    shop.run()