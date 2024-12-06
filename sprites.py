import pygame
import pygame.surface
import config as c
import math
import random

class Spritesheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0, 0), (x, y, width, height))
        sprite.set_colorkey(c.BLACK)
        return sprite

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = c.PLAYER_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * c.TILESIZE
        self.y = y * c.TILESIZE
        self.width = c.PLAYER_WIDTH
        self.height = c.PLAYER_HEIGHT

        self.facing = 'down'
        self.animation_loop = 0

        self.x_change = 0
        self.y_change = 0

        self.image = self.game.character_spritesheet.get_sprite(0, 0, c.PLAYER_WIDTH, c.PLAYER_HEIGHT)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animation()

        self.rect.x += self.x_change
        self.collide_blocks('x')
        self.rect.y += self.y_change
        self.collide_blocks('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= c.PLAYER_SPEED
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += c.PLAYER_SPEED
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= c.PLAYER_SPEED
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += c.PLAYER_SPEED
            self.facing = 'down'

    def collide_blocks(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.x_change > 0:
                   self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                   self.rect.x = hits[0].rect.right

        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.blocks, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom

    def animation(self):
        down_animations = [
            self.game.character_spritesheet.get_sprite(0, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 0, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 0, self.width, self.height)
        ]

        up_animations = [
            self.game.character_spritesheet.get_sprite(0, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 30, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 30, self.width, self.height)

        ]

        left_animations = [
            self.game.character_spritesheet.get_sprite(0, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 60, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 60, self.width, self.height)

        ]

        right_animations = [
            self.game.character_spritesheet.get_sprite(0, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(21, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 90, self.width, self.height),
            self.game.character_spritesheet.get_sprite(42, 90, self.width, self.height)
        ]

        if self.facing == 'down':
            if self.y_change == 0:
                self.image = down_animations[0]
            else:
                self.image = down_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(down_animations):
                    self.animation_loop = 1

        elif self.facing == 'up':
            if self.y_change == 0:
                self.image = up_animations[0]
            else:
                self.image = up_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(up_animations):
                    self.animation_loop = 1

        elif self.facing == 'left':
            if self.x_change == 0:
                self.image = left_animations[0]
            else:
                self.image = left_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(left_animations):
                    self.animation_loop = 1

        elif self.facing == 'right':
            if self.x_change == 0:
                self.image = right_animations[0]
            else:
                self.image = right_animations[math.floor(self.animation_loop)]
                self.animation_loop += 0.1
                if self.animation_loop >= len(right_animations):
                    self.animation_loop = 1


class Block(pygame.sprite.Sprite):
    def  __init__(self, game, x, y):

        self.game = game
        self._layer = c.BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * c.TILESIZE
        self.y = y * c.TILESIZE
        self.width = c.TILESIZE
        self.height = c.TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(961, 448, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = c.GROUND_LAYER
        self.groups = self.game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * c.TILESIZE
        self.y = y * c.TILESIZE
        self.width = c.TILESIZE
        self.height = c.TILESIZE

        self.image = self.game.terrain_spritesheet.get_sprite(64, 352, self.width, self.height)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y