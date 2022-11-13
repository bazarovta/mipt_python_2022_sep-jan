import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

screen.fill((220,220,200))

circle(screen, (255, 255,0), (200,200), 100)
circle(screen, (255,0,0), (250, 170), 20)
circle(screen, (255,0,0), (150,170), 20)
circle(screen, (0,0,0), (250,170), 10)
circle(screen, (0,0,0), (150,170), 10)

polygon(screen, (0,0,0), [(150,230),(250,230),(250,250),(150,250)])
line(screen, (0,0,0), (215,160), (300,130), 15)
line(screen, (0,0,0), (185,160), (100,130), 15)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
