# Course CSE 1321L
# Section: BJK
# Semester: Fall 2024
# Name: Starlan Davis

# Adjustments Made:
    # includes a more detailed background display (both image options were designed, by me, using Canva.com)
    # rather than just a rect, the falling fruit is now an image of cherries
    # includes music
    # the fruit increases speed over time (based on the user's score)

# all images were sourced from Canva.com)

# Fruit Catcher Game

import pygame, sys
from pygame import K_RIGHT
pygame.init()
clock = pygame.time.Clock()
import random

screen = pygame.display.set_mode((700,500)) # the whole screen / display
setting_image = pygame.image.load("Canva-Background0.png")
setting = pygame.transform.scale(setting_image, (700,500))

fruit_rect = pygame.Rect((0,0,10,10))
fruit_image = pygame.image.load("Canva-Cherries.png")
fruit = pygame.transform.scale(fruit_image, (90,90))

basket_rect = pygame.Rect((300,480,80,30))
basket_image = pygame.image.load("Canva-Basket.png")
basket = pygame.transform.scale(basket_image, (365,200))


screen.fill(color=(0,180,255))  # light blue screen / display window

surf = pygame.Surface((fruit_rect.w,fruit_rect.h))
surf.fill(color=(255,0,0))

surf1 = pygame.Surface((basket_rect.w,basket_rect.h))
surf1.fill(color=(255,178,102))

basket_rect_speed = [0,0]

score = 0
font = pygame.font.SysFont("Courier New",36, bold=True)    # initializes font type, size, and special attribute

music = pygame.mixer.Sound("Japanese Garden by Sight of Wonders.mp3")

running = True
while running:
    music.set_volume(0.1)
    music.play(-1)

    # increase the speed of the fruit by 2 for each set if 10 fruits that the player catches
    if score < 10:
        fruit_speed = [0,5]
    elif 20 > score >=10:
        fruit_speed = [0,7]
    elif 30 > score >=20:
        fruit_speed = [0,9]
    elif 40 > score >=30:
        fruit_speed = [0,11]
    elif 50 > score >=40:
        fruit_speed = [0,13] 
    
    # spawn fruit + movement
    if fruit_rect.y > 500:
        fruit_rect.x = random.randint(0, 400)
        fruit_rect.y=0
    fruit_rect = fruit_rect.move(fruit_speed)

    # key controls
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        if basket_rect.x < 500:
            basket_rect.x += 5
    if keys[pygame.K_LEFT]:
        if basket_rect.x > 0:
            basket_rect.x -= 5

    # collision detection / Score/point tracker
    if (basket_rect.colliderect(fruit_rect)):
        score += 1
        print("Score: " + str(score))
        fruit_rect.x = random.randint(0, 480)
        fruit_rect.y = 0

    # score displayed on screen
    score_tracker = font.render("Score: " + str(score), True, (0,0,0))


    screen.fill(color=(0,180,255))
    screen.blit(setting, (0,0))

    screen.blit(surf, (fruit_rect.x,fruit_rect.y))
    screen.blit(fruit, (fruit_rect.x-35,fruit_rect.y-55))

    screen.blit(surf1, (basket_rect.x,basket_rect.y))
    screen.blit(basket, (basket_rect.x-145,348))

    screen.blit(score_tracker, (16,40))
    pygame.display.flip()

    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == pygame.QUIT:
            running = False
