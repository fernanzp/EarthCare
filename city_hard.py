import pygame.mixer, sys, random

import defeat
from tiles import City_tile, City_tile_1
from settings import tile_size, weight, height
from players import Players
from trash import Trash
from victory import VictoryScreen
from defeat import DefeatScreen

class Level_c_2:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.setup_level(level_data)
        self.world_shift = 0
        self.current_x = 0
        self.trash_collected = 0 #Contador
        self.victory = False
        self.opc = None

        #Counters by type
        self.organic = 0
        self.glass = 0
        self.metal = 0
        self.paper = 0

        #Temporizador para la generación de basura
        self.last_trash_time = 0
        self.trash_spawn_inverval_min = 2000
        self.trash_spawn_inverval_max = 3000

        #Background
        self.background = pygame.image.load('Resourses/Backgrounds/City/city_bg.jpg').convert()
        self.background = pygame.transform.scale(self.background, (weight, height))

        #Counters
        self.green_counter_backgound = pygame.image.load('Resourses/Backgrounds/Counters/green_counter_background.png').convert_alpha()
        self.red_counter_backgound = pygame.image.load('Resourses/Backgrounds/Counters/red_counter_background.png').convert_alpha()

        #Sprite group for Trash
        self.trash_group = pygame.sprite.Group()
        for x in range(12):
            trash = Trash()
            self.trash_group.add(trash)

        #Sounds
        self.victory_sound = pygame.mixer.Sound('Resourses/sfx/Victory_defeat/victory.wav')
        self.defeat_sound = pygame.mixer.Sound('Resourses/sfx/Victory_defeat/defeat.wav')

    def get_font(self, size):
        return pygame.font.Font("../EarthCare/Resourses/Fonts/font.ttf", size)

    def setup_level(self, layout):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

        for row_index, row in enumerate(layout):
            for col_index, cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size

                if cell == 'X':
                    city_tile = City_tile((x, y), tile_size)
                    self.tiles.add(city_tile)
                if cell == 'P':
                    player_sprite = Players((x, y))
                    self.player.add(player_sprite)
                if cell == 'Y':
                    city_tile_1 = City_tile_1((x, y), tile_size)
                    self.tiles.add(city_tile_1)

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
        for _ in range(8):
            trash = Trash()
            self.trash_group.add(trash)

    def reset(self):
        player_sprite = Players((625, 670))
        self.player.empty()
        self.player.add(player_sprite)

        self.trash_collected = 0
        self.trash_group.empty()

        #self.organic = 0
        #self.glass = 0
        #self.metal = 0
        #self.paper = 0
        #self.last_trash_time = 0

    def run(self):
        #Background
        self.display_surface.blit(self.background, (0,0))

        #Counter backgrounds
        self.display_surface.blit(self.green_counter_backgound, (10, 10))
        self.display_surface.blit(self.red_counter_backgound, (1154, 10))

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
            self.trash_collected += 1 #Sumar 1 al contador

            if trash.image_file in ['Apple.png', 'Bannana.png']:
                self.organic += 1
            elif trash.image_file in ['Bottle1.png', 'Bottle2.png']:
                self.glass += 1
            elif trash.image_file in ['Can1.png', 'Can2.png']:
                self.metal += 1
            elif trash.image_file in ['Box.png', 'News.png']:
                self.paper += 1

        #Verify if the counter reaches 120
        if self.trash_collected >= 120:
            self.victory_sound.play()
            self.reset()
            victory_screen = VictoryScreen(self.display_surface, weight, height, self.organic, self.glass, self.metal, self.paper)
            victory_screen.run()

            self.opc = victory_screen.button_pressed
            return

        #Verify the collision between trash and tiles
        trash_tile_collisions = pygame.sprite.groupcollide(self.trash_group, self.tiles, False, False)

        #Count the trashes that are on the ground
        trash_on_floor = 0
        for trash, tile_list in trash_tile_collisions.items():
            if any(tile.rect.colliderect(trash.rect) for tile in tile_list):
                trash_on_floor += 1

        #If there are at least 100 trash on the ground, close the game
        if trash_on_floor >= 100:
            self.defeat_sound.play()
            self.reset()
            defeat_screen = DefeatScreen(self.display_surface, weight, height)
            defeat_screen.run()

            self.opc = defeat_screen.button_pressed
            return

        #Trash collected counter
        text_trash_collected = self.get_font(18).render(f"{self.trash_collected}/120",True, (255,255,255))
        #Trash on the ground counter
        text_trash_on_ground = self.get_font(18).render(f"{trash_on_floor}/100", True, (255,255,255))

        self.display_surface.blit(text_trash_collected, (15, 21))
        self.display_surface.blit(text_trash_on_ground, (1175, 21))