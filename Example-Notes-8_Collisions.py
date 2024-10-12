# This program consists of 2 rects. 1 travels horizontally across the screen, repetitively. The other is motionless and stretches vertically across the screen. As the moving rect collides with the stationary rect, the stationary rect changes color, it then reverts to its original collor when te moving rect is no longer colliding with it.

import pygame
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((400,400))

rect = pygame.Rect(175,0,50,400)   # This rect will be the visual display that changes colors when another rect collides with it.
rect1 = pygame.Rect(175,175,50,50)  # rect1 will be moving across the screen and colliding with "rect"

rect_speed = [5,0]   # assigns the speed as 5 units

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(255,0,0))

surf1 = pygame.Surface((rect1.w,rect1.h))
surf1.fill(color=(0,0,255))


running = True
while running:
  # uses colliderect() to detect a collision
    if (rect.colliderect(rect1)):   # if a collision is detected, the color of "rect" changes to Green
        surf.fill(color=(0,255,0))
    else:                           # when a collision is not detected, the color of "rect" is Red
        surf.fill(color=(255,0,0))

  # "rect1" is made to move back and forth across the screen
    if (rect1.x<0 or rect1.x>350): 
        rect_speed[0] = -rect_speed[0]   # determines when to change "rect1's" travelling direction
    rect1 = rect1.move(rect_speed)   # initializes the rect's movement

    screen.fill(color=(0, 0, 0))

    screen.blit(surf, (rect.x,rect.y))
    screen.blit(surf1, (rect1.x,rect1.y))
    pygame.display.flip()                 # updates the Display
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
