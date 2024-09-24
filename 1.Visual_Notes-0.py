# This file displays the basics/foundation of creating a game
# 09/24/2024

import pygame

pygame.init()        # initializes Pygame

screen = pygame.display.set_mode((500,500))     # initializes the Display(def. what will be shown on the screen) and its resolution (in this case 500x500), and stores it in a variable

surf = pygame.Surface((200,200))        # establishes the size of the surface ((width, height))
surf.fill(color=(255,0,255))      # COLORING; creates a purple square in the top left corner of the 

screen.blit(surf, (0,0))          # BLITTING; copies the pixels/information from variable 'surf' to variable 'screen' onto the (0,0) coordinates
pygame.display.flip()            # tells the computer to update the whole screen


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
