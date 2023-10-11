import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/Tile_0.png').convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size,size))
        #self.image.fill('brown')   Color solido para los tiles
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift