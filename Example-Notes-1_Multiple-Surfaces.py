import pygame

pygame.init()        # initializes Pygame

screen = pygame.display.set_mode((600,450))     # initializes the Display(def. what will be shown on the screen) and its resolution (in this case 600x450), and stores it in a variable

surf = pygame.Surface((200,200))        # establishes the size of the surface ((width, height))
surf.fill(color=(255,0,255))      # COLORING; creates a purple square 

surf1 = pygame.Surface((60,85))        # establishes the size of the surface ((width, height))
surf1.fill(color=(0,255,0))      # COLORING; creates a green square

surf2 = pygame.Surface((200,200))        # establishes the size of the surface ((width, height))
surf2.fill(color=(255,0,0))      # COLORING; creates a red square

screen.blit(surf, (27,67))          # BLITTING; copies the pixels/information from variable 'surf' to variable 'screen' onto coordinates (27,67)
screen.blit(surf1, (0,0))         # BLITTING; copies the pixels/information from variable 'surf1' to variable 'screen' onto the origin
screen.blit(surf2, (300,60))         # BLITTING; copies the pixels/information from variable 'surf2' to variable 'screen' onto the coordinates (300,60)

pygame.display.flip()            # tells the computer to update the whole screen


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
