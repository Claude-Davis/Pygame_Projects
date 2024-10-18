# Meteor Evader Game

import pygame, sys
pygame.init()
clock = pygame.time.Clock()
from pygame import K_RIGHT
from pygame.locals import *
import random

screen = pygame.display.set_mode((800,800))

ship = pygame.Rect((0,0,40,40))
meteor = pygame.Rect((0,0,40,40)) # this meteor travels down

screen.fill(color=(0,0,153))

surf_ship = pygame.Surface((ship.w, ship.h))
surf_ship.fill(color=(255,255,255))

surf_meteor = pygame.Surface((meteor.w,meteor.h))
surf_meteor.fill(color=(128,128,128))

ship_speed = [0,0]
meteor_speed = [0,3.5]

run = True
while run:
    # key movement controls
    keys = pygame.key.get_pressed()
    if keys[K_w]:
        if ship.top > 0:
            ship.y -= 5
    if keys[K_s]:
        if ship.bottom < 800:
            ship.y += 5
    if keys[K_d]:
        if ship.right < 800:
            ship.x += 5
    if keys[K_a]:
        if ship.left > 0:
            ship.x -= 5
    ship = ship.move(ship_speed)

    screen.blit(surf_ship, (ship.x,ship.y))
    screen.blit(surf_meteor, (meteor.x,meteor.y))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
        elif event.type == pygame.QUIT:
            run = False
