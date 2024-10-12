# Course CSE 1321L
# Section: BJK
# Semester: Fall 2024
# Name: Starlan Davis

# Fruit Catcher Game

import pygame, sys
from pygame import K_RIGHT
pygame.init()
clock = pygame.time.Clock()
import random

screen = pygame.display.set_mode((800,600)) # the whole screen / display
fruit = pygame.Rect((0,0,20,20))
basket = pygame.Rect((300,580,100,20))

screen.fill(color=(0,180,255))  # light blue screen / display window

surf = pygame.Surface((fruit.w,fruit.h))
surf.fill(color=(255,0,0))

surf1 = pygame.Surface((basket.w,basket.h))
surf1.fill(color=(255,255,255))

fruit_speed = [0,3]
basket_speed = [0,0]

font = pygame.font.SysFont("Courier New",36, bold=True)    # initializes font type, size, and special attribute

score = 0

running = True
while running:
    # spawn fruit + movement
    if fruit.y > 600:
        fruit.x = random.randint(0, 780)
        fruit.y=0
    fruit = fruit.move(fruit_speed)

    # key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if basket.x < 700:
            basket.x += 5
    if keys[pygame.K_LEFT]:
        if basket.x > 0:
            basket.x -= 5

    # collision detection / Score/point tracker
    if (basket.colliderect(fruit)):
        score += 1
        print("Score: " + str(score))
        fruit.x = random.randint(0, 780)
        fruit.y = 0

    # score displayed on screen
    score_tracker = font.render("Score: " + str(score), True, (255,255,0))


    screen.fill(color=(0,180,255))
    screen.blit(surf, (fruit.x,fruit.y))
    screen.blit(surf1, (basket.x,basket.y))
    screen.blit(score_tracker, (20,20))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
