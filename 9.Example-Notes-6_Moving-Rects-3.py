# A single rect moves back and forth, diagonally, across the display

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

rect = pygame.Rect(0,0,10,10)
rect_speed = [2,2]               # Determines the speed of the rect

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(255,255,255))

running = True

while running:
    if (rect.x<0 or rect.x>499) and (rect.y<0 or rect.y>499):      #This creates the boundary for the rect/regulates how far the rect can travel
                                #The max values above (in this case 500) when added to the width and height of the rect should equal the display size if you only want the rect to travel as far the display
        rect_speed[0] = -rect_speed[0]
            # The negative sign (-) inverts the speed and send the rect in the opposite direction
        rect_speed[1] = -rect_speed[1]
    rect = rect.move(rect_speed)   # Causes the illusion of movement


    screen.fill(color=(0,0,0))
    screen.blit(surf, (rect.x,rect.y))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
