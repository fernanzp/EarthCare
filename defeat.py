import pygame

class DefeatScreen:
    def __init__(self, display_surface, weight, height):
        self.display_surface = display_surface
        self.background = pygame.image.load('Resourses/Backgrounds/Win_lose/Defeat.png').convert()
        self.background = pygame.transform.scale(self.background, (weight, height))

        #Titles
        self.defeat_title = pygame.image.load('Resourses/Titles/Defeat_title.png').convert_alpha()

        #Buttons
        self.retry_button = pygame.image.load('Resourses/Buttons/Retry_button.png').convert_alpha()
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
            self.display_surface.blit(self.defeat_title, (72, 272))

            #Buttons
            self.display_surface.blit(self.retry_button, (40, 540))
            self.display_surface.blit(self.menu_button, (830, 540))

            pygame.display.flip()

        pygame.quit()
