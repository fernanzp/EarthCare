import pygame

class VictoryScreen:
    def __init__(self, display_surface, weight, height, organic, glass, metal, paper):
        self.display_surface = display_surface
        self.background = pygame.image.load('Resourses/Backgrounds/Win_lose/Win.png').convert()
        self.background = pygame.transform.scale(self.background, (weight, height))
        self.organic = organic
        self.glass = glass
        self.metal = metal
        self.paper = paper
        center_x = weight // 2
        center_y = height // 2


        #Titles
        self.victory_title = pygame.image.load('Resourses/Titles/Victory_title.png').convert_alpha()

        #Buttons
        self.menu_button = pygame.image.load('Resourses/Buttons/Menu_button.png').convert_alpha()

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

            #Titles
            self.display_surface.blit(self.victory_title, (55, 201))

            #Buttons
            self.display_surface.blit(self.menu_button, (800, 572))

            font = pygame.font.Font(None, 46)
            ancho_del_contador, alto_del_contador = font.size("Organic: 10")
            x_counter = 640 - (ancho_del_contador / 2)
            text_organic = self.get_font(18).render(f"Organic:{self.organic}", True, (0, 255, 0))
            text_glass = self.get_font(18).render(f"Glass:{self.glass}", True, (0, 187, 255))
            text_metal = self.get_font(18).render(f"Metal:{self.metal}", True, (255, 0, 0))
            text_paper = self.get_font(18).render(f"Paper:{self.paper}", True, (255, 255, 0))

            self.display_surface.blit(text_organic, (x_counter, 370))
            self.display_surface.blit(text_glass, (x_counter, 420))
            self.display_surface.blit(text_metal, (x_counter, 470))
            self.display_surface.blit(text_paper, (x_counter, 520))

            pygame.display.flip()

        pygame.quit()