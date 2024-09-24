import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))

rect = pygame.Rect(500,0,200,200)             # assigns the variable "rect" at coordinates (500,0) with a width of 200 and height of 200

surf = pygame.Surface((rect.w,rect.h))        # assigns the surface with the width and height of "rect"
surf.fill(color=(128,128,128))      

screen.blit(surf, (rect.x,rect.y))            # assigns the location of the rect

pygame.display.flip()


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
