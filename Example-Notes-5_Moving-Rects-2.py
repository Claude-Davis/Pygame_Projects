# Single rect moves, diagonally, across the display

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((700,700))

rect = pygame.Rect(0,0,200,200)

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(128,128,128))

running = True

while running:
    rect = rect.move(5,5)   # moves the rect 5 units along the x- and y-axis
    screen.fill(color=(0,0,0)) # overwrites the previous rects with black rects
    screen.blit(surf, (rect.x,rect.y))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
