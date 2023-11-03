import pygame

class VictoryScreen:
    def __init__(self, display_surface, weight, height):
        self.display_surface = display_surface
        self.background = pygame.image.load('Resourses/Backgrounds/Win_lose/Win.png').convert()
        self.background = pygame.transform.scale(self.background, (weight, height))

    def run(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            self.display_surface.blit(self.background, (0, 0))
            pygame.display.flip()

        pygame.quit()