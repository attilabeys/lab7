import pygame
import math
import sys
from time import localtime
height = 300
width = 300
pygame.init()
screen = pygame.display.set_mode((width, height))
m_img = pygame.image.load("mickeyclock.png")
m_img = pygame.transform.scale(m_img, (300, 300))
minute_img = pygame.image.load("minute.png")
minute_img = pygame.transform.scale(minute_img, (140, 60))
second_img = pygame.image.load("second.png")
second_img = pygame.transform.scale(second_img, (140, 60))

   
def d_clock(m, s):
    screen.fill((255, 255, 255))
    screen.blit(m_img, (width//2 - m_img.get_width()//2, height//2 - m_img.get_height()//2))

    rotated_minute_hand = pygame.transform.rotate(minute_img, -(m * 6))
    screen.blit(rotated_minute_hand, (width//2 - rotated_minute_hand.get_width()//2, height//2 - rotated_minute_hand.get_height()//2))

    rotated_second_hand = pygame.transform.rotate(second_img, -(s * 6))
    screen.blit(rotated_second_hand, (width//2 - rotated_second_hand.get_width()//2, height//2 - rotated_second_hand.get_height()//2))

    pygame.display.flip()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    current_time = localtime()
    minute, second = current_time.tm_min, current_time.tm_sec


    d_clock(minute, second)


    clock.tick(60)