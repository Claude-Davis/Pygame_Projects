# the user controls a blue rect with the keys 'w,' 's,' 'd,' and 'a.' the user is not able to move the rect off of the screen.
  # w = up
  # s = down
  # d = right 
  # a = left

import pygame, sys
from pygame.locals import *
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((500,500))

blue = pygame.Rect(225,225,50,50)
rect_speed = [0,0]

surf = pygame.Surface((blue.w,blue.h))
surf.fill(color=(0,0,255))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    # the keys
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        if blue.top > 0: # prevent rect from moving off the top
            blue.y -= 5 # move up 5 if key 'w' is pressed
    if keys[K_s]:
        if blue.bottom < 500:  # prevent rect from moving off the bottom
            blue.y += 5  # move down 5 if key 's' is pressed
    if keys[K_d]:
        if blue.right < 500:  # prevent rect from moving off the right side
            blue.x += 5 # move right 5 if key 'd' is pressed
    if keys[K_a]:
        if blue.left > 0: # prevent rect from moving off the left side
            blue.x -= 5 # move left 5 if key 'a' is pressed
    if keys[K_r]:
        blue.x = 225
        blue.y = 225
    blue = blue.move(rect_speed)


    screen.fill(color=(0,0,0))
    screen.blit(surf, (blue.x,blue.y))
    pygame.display.flip()
    clock.tick(60)
