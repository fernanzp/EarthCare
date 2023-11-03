import random
import pygame
import os

class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        trash_images = {
            'Apple.png': (33, 40.5),
            'Bannana.png': (43, 22),
            'Bottle1.png': (22.4, 46.2),
            'Bottle2.png': (40.6, 43.4),
            'Box.png': (43.5, 25.5),
            'Can1.png': (45.9, 27.9),
            'Can2.png': (38.7, 47.7),
            'News.png': (40, 21)
        }
        self.image_file = random.choice(list(trash_images.keys()))
        self.image = pygame.image.load(os.path.join('Resourses/Trash', self.image_file)).convert_alpha()
        self.image = pygame.transform.scale(self.image, trash_images[self.image_file])
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