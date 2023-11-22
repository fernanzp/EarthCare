import pygame, sys
from buttons import Button

class Sound:
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

            MENU_TEXT = self.get_font(100).render("SOUND", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

            SOUND_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Sound_button.png"), pos=(300, 400),
                                  text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            MUTE_SOUND = Button(image=pygame.image.load("Resourses/Buttons/NoSound_button.png"), pos=(1000, 400),
                                text_input="", font=self.get_font(75), base_color="#d7fcd4", hovering_color="White")
            BACK_BUTTON = Button(image=pygame.image.load("Resourses/Buttons/Red_button.png"), pos=(640, 650),
                                 text_input="BACK", font=self.get_font(50), base_color="#ffffff", hovering_color="#590a0a")

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
                        self.opc = "sound"
                        return
                    if MUTE_SOUND.checkForInput(MENU_MOUSE_POS):
                        self.opc = "mute"
                        return
                    if BACK_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.opc = "back"
                        return

            pygame.display.update()

if __name__ == "__main__":
    sound = Sound()
    sound.run()