import pygame

class VictoryScreen:
    def __init__(self, display_surface, weight, height):
        self.display_surface = display_surface
        self.background = pygame.image.load('Resourses/Backgrounds/Win_lose/Win.png').convert()
        self.background = pygame.transform.scale(self.background, (weight, height))

        #Titles
        self.victory_title = pygame.image.load('Resourses/Titles/Victory_title.png').convert_alpha()

        #Buttons
        self.menu_button = pygame.image.load('Resourses/Buttons/Menu_button.png').convert_alpha()

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            #Background
            self.display_surface.blit(self.background, (0, 0))

            #Titles
            self.display_surface.blit(self.victory_title, (55, 282))

            #Buttons
            self.display_surface.blit(self.menu_button, (800, 540))


            pygame.display.flip()

        pygame.quit()