import random
import pygame

class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Resourses/Trash/Bannana.png').convert()
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocity_y = 5

    def update(self):
        self.rect.y += self.velocity_y
        if self.rect.top > 720:
            self.reset()