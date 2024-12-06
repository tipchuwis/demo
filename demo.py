import pygame, sys
import config as c
from players import Players

# Pygame Initialization
pygame.init()
pygame.font.init()

# Display Setup
display = pygame.display.set_mode((c.DISPLAY_WIDTH, c.DISPLAY_HEIGHT))
fps = 60
clock = pygame.time.Clock()
pygame.display.set_caption("La Llave de Atrás - Menú Principal")

# Object Setup
player = Players()

running = True
while running:
    # Tick Clock
    clock.tick(fps)
    # Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Player Movement

    # Update all the objects

    # Check collisions and dialogues
    
    # Render the display
    display.fill(c.BLACK)
    player.draw(display)
    pygame.display.update()