import pygame
import random
import math
import cannon
import ammo
import target

def score(points, screen, score_font):
    '''
    отрисовывает кол-во очков, полученных игроком
    points - кол-во очков
    screen - объект типа pygame.Surface, где происходит отрисовка
    score_font - объект типа pygame.font.SysFont, на котором отрисовается кол-во очков
    '''
    value = score_font.render("Your score: " + str(points), True, (255, 0, 0))
    background = pygame.Surface((150,30))
    background.fill((255,255,255))
    screen.blit(background, (0,0))
    screen.blit(value, (0,0))

FPS = 30
pygame.init()
screen = pygame.display.set_mode((800,600))
score_font = pygame.font.SysFont("comicsansms", 35)
balls = []
targets = []
bomber = target.Bomber(screen)
targets.append(bomber.throw_target())
targets.append(bomber.throw_target())
targets.append(bomber.throw_target())
clock = pygame.time.Clock()
gun = cannon.Cannon(screen)
finished = False
points = 0

while not finished:
    screen.fill((255, 255, 255))
    gun.draw()
    score(points, screen, score_font)
    bomber.draw()
    bomber.move()
    pygame.draw.rect(screen, (150, 75, 0), (0, 550, 800, 600))
    cord = []
    for t in targets:
        t.draw()
        t.move()
        cord.append(t.get_pos())
    for ball in balls:
        if ball.live != 0:
            ball.draw()
            ball.move()
        for i in range (0, len(cord)):
            b = ball.get_pos()
            c = cord[i]
            if ((b[0]-c[0])**2 + (b[1]-c[1])**2 < (c[2]+b[2])**2) and ball.live == 1:
                points += 1
                ball.live = -1
                ball.y = 585
                ball.x = 15 * (points+1)
                targets[i] = bomber.throw_target()
    pygame.display.update()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire_start()
        elif event.type == pygame.MOUSEBUTTONUP:
            balls.append(gun.fire_end())
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event.pos, 0)
    gun.move()

