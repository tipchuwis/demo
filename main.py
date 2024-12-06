import pygame
from sprites import *
import config as c
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 32)
        self.running = True
        
        self.character_spritesheet = Spritesheet('img/mel_spritesheet.png')
        self.terrain_spritesheet = Spritesheet('img/terrain.png')

    def createTilemap(self):
        for i, row in enumerate(c.TILEMAP):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "B":
                    Block(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def new(self):
        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.createTilemap()
        self.playing = True
        self.createTilemap()
        
        

    def events(self):
        # game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        # game loop updates
        self.all_sprites.update()
        
    def draw(self):
        # game loop draw
        self.screen.fill(c.BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(c.FPS)
        pygame.display.update()

    def main(self): # basically all the game happening.
        # game loop
        while self.playing:
            self.events()
            self.update()
            self.draw()
        self.running = False

    def game_over(self):
        pass
    def intro_screen(self):
        pass

g = Game()
g.intro_screen()
g.new()

while g.running:
    g.main()
    g.game_over()

pygame.quit()
sys.exit()