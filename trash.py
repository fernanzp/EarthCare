import random
import pygame

class Trash(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('Resourses/Trash/Apple_pix.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (90, 90))
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.randrange(1280 - self.rect.width)
        self.rect.y = -self.rect.width
        self.velocity_y = random.randrange(2, 4)

    def update(self):
        self.rect.y += self.velocity_y
        if self.rect.top > 720:
            self.reset()