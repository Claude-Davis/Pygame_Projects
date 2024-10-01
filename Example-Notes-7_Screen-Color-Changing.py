# Loop: Gradually changes the color of the screen from black to white, and then back to black

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((400,400))

color_value = 0
increasing = True  # determines if the color value is increasing or decreasing

run = True
while run:
    # fills the screen with the current color
    screen.fill((color_value,color_value,color_value))

    if increasing:
        color_value += 1
        if color_value >=255:
            increasing = False
    else:
        color_value -= 1
        if color_value <= 0:
            increasing = True

    pygame.display.flip()
    clock.tick(85)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
