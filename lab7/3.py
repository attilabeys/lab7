import sys
import pygame
pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
w = 600
h = 500
r = 25
x = (w - r * 2) // 2
y = (h - r * 2) // 2
screen = pygame.display.set_mode((w, h))
clock = pygame.time.Clock()
move = True
while move:
    screen.fill(white)
    pygame.draw.circle(screen, red, (x,y), r)
    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            moving = False
     elif event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            if y - 20 >= 0:
                y -= 20
        elif event.key == pygame.K_DOWN:
            if y + r//2 + 20 <= h:
                y += 20
        elif event.key == pygame.K_LEFT:
            if x - 20 >= 0:
                x -= 20
        elif event.key == pygame.K_RIGHT:
            if x + r//2 + 20 <= w:
                x += 20

    pygame.display.flip()
    clock.tick(30)
    while True:
     for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
