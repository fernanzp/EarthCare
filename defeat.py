import pygame
from buttons import Button

class DefeatScreen:
    def __init__(self, display_surface, weight, height):
        self.display_surface = display_surface
        self.SCREEN = pygame.display.set_mode((1280, 720))
        self.background = pygame.image.load('Resourses/Backgrounds/Win_lose/Defeat.png').convert()
        self.background = pygame.transform.scale(self.background, (weight, height))
        self.button_pressed = None

        #Titles
        self.defeat_title = pygame.image.load('Resourses/Titles/Defeat_title.png').convert_alpha()

    def get_font(self, size):
        return pygame.font.Font("../EarthCare/Resourses/Fonts/font.ttf", size)

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #Background
            self.display_surface.blit(self.background, (0, 0))

            MENU_MOUSE_POS = pygame.mouse.get_pos()

            #Titles
            self.display_surface.blit(self.defeat_title, (72, 226))

            #Buttons
            retry_button = Button(image=pygame.image.load('Resourses/Buttons/Yellow_button.png'), pos=(240, 634), text_input="RETRY", font=self.get_font(40), base_color="#efa40f", hovering_color="#b57b08")#.blit(self.retry_button, (40, 540))
            menu_button = Button(image=pygame.image.load('Resourses/Buttons/Yellow_button.png'), pos=(1030, 634), text_input="MENU", font=self.get_font(40), base_color="#efa40f", hovering_color="#b57b08")#.blit(self.menu_button, (830, 540))

            for button in [retry_button, menu_button]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(self.SCREEN)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.checkForInput(MENU_MOUSE_POS):
                    self.button_pressed = "retry"
                    return
                if menu_button.checkForInput(MENU_MOUSE_POS):
                    self.button_pressed = "menu"
                    return

            pygame.display.flip()

        pygame.quit()
