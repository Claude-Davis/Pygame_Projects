# A rect circles the display

import pygame

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((200,200))

rect = pygame.Rect(0,0,50,50)           

surf = pygame.Surface((rect.w,rect.h))
surf.fill(color=(255,255,255))

running = True

while running:  # lines 16-25 dictate the changes in diretion 
    if (rect.x==0):
        if (rect.y==0):
            rect_speed = [5,0]
        elif (rect.y==150):
            rect_speed = [0,-5]
    elif (rect.x==150):
        if (rect.y==0):
            rect_speed = [0,5]
        elif (rect.y==150):
            rect_speed = [-5,0]
    rect = rect.move(rect_speed)    # Causes the illusion of movement (the rect would not 'move' w/o this command)



    screen.fill(color=(0,0,0))
    screen.blit(surf, (rect.x,rect.y))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
