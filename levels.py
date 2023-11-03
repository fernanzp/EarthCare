import pygame.mixer, sys, random
from tiles import Tile, Tile_1
from settings import tile_size, weight, height
from players import Players
from trash import Trash
from victory import VictoryScreen
from defeat import DefeatScreen

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        self.trash_collected = 0 #Contador
        #Temporizador para la generación de basura
        self.last_trash_time = 0
        self.trash_spawn_inverval_min = 2000
        self.trash_spawn_inverval_max = 3000

        #Background
        self.background = pygame.image.load('Resourses/Backgrounds/Forest/Background_forest.png').convert() 
        self.background = pygame.transform.scale(self.background, (weight, height))

        #Music
        pygame.mixer.init()
        pygame.mixer.music.load('Resourses/sfx/forest_level_sound.wav')
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.5)

        #Sprite group for Trash
        self.trash_group = pygame.sprite.Group()
        for x in range(5):
            trash = Trash()
            self.trash_group.add(trash)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    tile = Tile((x,y),tile_size)
                    self.tiles.add(tile)
                if cell == 'P':
                    player_sprite = Players((x, y))
                    self.player.add(player_sprite)
                if cell == 'Y':
                    tile_1 = Tile_1((x,y),tile_size)
                    self.tiles.add(tile_1)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < weight/4 and direction_x < 0:
            self.world_shift = 3
            player.speed = 0
            for trash in self.trash_group:
                trash.rect.x += 3

        elif player_x > weight - (weight/4) and direction_x > 0:
            self.world_shift = -3
            player.speed = 0
            for trash in self.trash_group:
                trash.rect.x += -3

        else:
            self.world_shift = 0
            player.speed = 3

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    def generate_new_trash(self):
        for _ in range(5):
            trash = Trash()
            self.trash_group.add(trash)

    def run(self):
        #Background
        self.display_surface.blit(self.background, (0,0))

        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.scroll_x()

        #player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        #Time
        current_time = pygame.time.get_ticks()
        random_interval = random.randint(self.trash_spawn_inverval_min, self.trash_spawn_inverval_max)
        if current_time - self.last_trash_time >= random_interval:
            self.generate_new_trash()
            self.last_trash_time = current_time

        #Trash
        trash_collisions = pygame.sprite.groupcollide(self.trash_group, self.tiles, False, False)
        for trash, tile_list in trash_collisions.items():
            for tile in tile_list:
                trash.velocity_y = 0

        self.trash_group.update()
        self.trash_group.draw(self.display_surface)

        #Trash collide with Player
        trash_collisions = pygame.sprite.groupcollide(self.trash_group, self.player, True, False)
        for trash, player_list in trash_collisions.items():
            trash.kill()
            self.trash_collected += 1 #Sumamos 1 al contador

        #Verificamos si el contador llega a 20
        if self.trash_collected >= 20:
            victory_screen = VictoryScreen(self.display_surface, weight, height)
            victory_screen.run()
            pygame.quit()
            sys.exit()

        #Verify the collision between trash and tiles
        trash_tile_collisions = pygame.sprite.groupcollide(self.trash_group, self.tiles, False, False)

        #Count the trashes that are on the ground
        trash_on_floor = 0
        for trash, tile_list in trash_tile_collisions.items():
            if any(tile.rect.colliderect(trash.rect) for tile in tile_list):
                trash_on_floor += 1

        #If there are at least 30 trash on the ground, close the game
        if trash_on_floor >= 40:
            defeat_screen = DefeatScreen(self.display_surface, weight, height)
            defeat_screen.run()
            pygame.quit()
            sys.exit()

        #Contador
        font = pygame.font.Font(None, 36)
        text = font.render(f"{self.trash_collected}/20",True, (255,255,255))

        self.display_surface.blit(text, (190, 10))
        #self.trash_group.update()
        #self.trash_group.draw(self.display_surface)