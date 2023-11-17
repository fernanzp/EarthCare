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

class Tile_1(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/Tile_1.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size,size))
        #self.image.fill('brown')   Color solido para los tiles
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Sand_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/Sand_tile0.png').convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size,size))
        #self.image.fill('brown')   Color solido para los tiles
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class Sand_tile_1(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/Sand_tile1.png').convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size,size))
        #self.image.fill('brown')   Color solido para los tiles
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class City_tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/City_tile0.png').convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size,size))
        #self.image.fill('brown')   Color solido para los tiles
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

class City_tile_1(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/City_tile1.png').convert()
        self.image = pygame.transform.scale(self.image, (size, size))
        #self.image = pygame.Surface((size,size))
        #self.image.fill('brown')   Color solido para los tiles
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift

'''class Flower_0(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('Resourses/Tiles/flower_0.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (size, size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, x_shift):
        self.rect.x += x_shift'''