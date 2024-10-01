import pygame
pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((1000,500))

rect1 = pygame.Rect(0,0,100,100)
rect2 = pygame.Rect(0,400,100,100)

rect_speed = [5,0]
rect_speed1 = [10,0]

surf1 = pygame.Surface((rect1.w,rect1.h))
surf1.fill(color=(0,255,0))

surf2 = pygame.Surface((rect2.w,rect2.h))
surf2.fill(color=(0,0,255))


run = True
while run:
    if (rect1.x<0 or rect1.x>900):
        rect_speed[0] = -rect_speed[0]
    rect1 = rect1.move(rect_speed)

    if (rect2.x<0 or rect2.x>900):
        rect_speed1[0] = -rect_speed1[0]
    rect2 = rect2.move(rect_speed1)

    screen.fill(color=(0,0,0))
    screen.blit(surf1, (rect1.x,rect1.y))
    screen.blit(surf2, (rect2.x, rect2.y))
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                run = False
