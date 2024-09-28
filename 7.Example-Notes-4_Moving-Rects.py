# Several rects are created and resemble an arrow traveling across the display.

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((700,700))

rect = pygame.Rect(0,0,200,200)

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(128,128,128))

running = True

while running:
    rect = rect.move(5,5)                  # moves the rect 5 units along the x- and y-axis
    screen.blit(surf, (rect.x,rect.y))     # a streak of the previous rects remain because this blit is only updating the coordinates given to it.
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
