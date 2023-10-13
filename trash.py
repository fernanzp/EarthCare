import random
import pygame

class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Resourses/Trash/Apple.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.reset()
        #self.tiles = tiles

    def reset(self):
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocity_y = random.randrange(2, 4)

    def update(self):
        self.rect.y += self.velocity_y
        if self.rect.top > 720:
            self.reset()

        #Collisions
        '''collisions = pygame.sprite.spritecollide(self, self.tiles, False)
        for tile in collisions:
            self.velocity_y = 0'''