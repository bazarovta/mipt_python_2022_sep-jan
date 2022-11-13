import pygame
from pygame.draw import *
from random import randint

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

class Ball:
    '''
    класс Ball
    переменные:
        -x,y - координаты центра шара
        -vx,vy - скорость шара
        -r - радиус шара
        -color - цвет шара
    методы:
        -__init__
        -draw
    '''
    def __init__(self):
        '''
        создает представителя класс
        '''
        self.x = randint(100, 1100)
        self.y = randint(100, 800)
        self.vx = randint(-40,40)
        self.vy = randint(-30,30)
        self.r = randint(20,50)
        self.color = COLORS[randint(0, len(COLORS)-1)]

    def draw(self, screen, erase=False):
        '''
        рисует или стирает объект
        screen - объект pygame.Surface, где происходит отрисовка
        erase - объект типа bool, который указывает на действие: 
        нарисовать или удалить
        '''
        if erase == True:
            circle(screen, (255,255,255), (self.x, self.y), self.r)
        else:
            circle(screen, self.color, (self.x, self.y), self.r) 

def click(cord, balls):
    '''
    проверяет попадание мышки в один из шаров
    cord - координаты мышки, при её нажатии
    balls - массив объектов типа Ball
    '''
    x = cord[0]
    y = cord[1]
    for i in balls:
        if (x-i.x)**2 + (y-i.y)**2 < i.r**2:
            return True
    return False

def score(points, screen, score_font):
    '''
    отрисовывает кол-во очков, полученных игроком
    points - кол-во очков
    screen - объект типа pygame.Surface, где происходит отрисовка
    score_font - объект типа pygame.font.SysFont, на котором отрисовается кол-во очков
    '''
    value = score_font.render("Your score: " + str(points), True, RED)
    background = pygame.Surface((150,30))
    screen.blit(background, (0,0))
    screen.blit(value, (0,0))

def main():
    
    pygame.init()

    FPS = 30
    screen = pygame.display.set_mode((1200,900))
    score_font = pygame.font.SysFont("comicsansms", 35)
    screen.fill((255,255,255))
    pygame.display.set_caption("GAME")

    clock = pygame.time.Clock()
    finished = False
    points = 0
    
    score(points, screen, score_font)
    balls = [Ball() for i in range (0,10)]
    pygame.display.update()

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if click(event.pos, balls) == True:
                        points += 1
                        score(points, screen, score_font)
        for ball in balls:
            dt = 0.5
            if (ball.x-ball.r < 200 and ball.y-ball.r < 50):
                ball.vx = randint(5,40)
                ball.vy = randint(5,30)
            else:
                if ball.x - ball.r < 0:
                    ball.vx = randint(5, 40)
                elif ball.x+ball.r > 1200:
                    ball.vx = randint(-40, -5)
                if ball.y-ball.r < 0:
                    ball.vy = randint(5, 30)
                elif ball.y+ball.r > 900:
                    ball.vy = randint(-30, -5)
            ball.draw(screen, True)
            ball.x = ball.x + int(ball.vx*dt)
            ball.y = ball.y + int(ball.vy*dt)
            ball.draw(screen)
        pygame.display.update()
    return points

print("enter your name")
name = input()
print("the game starts")
points = main()
file = open('best_players.txt', 'r')
arr_players = []
for line in file:
    if len(line) != 0:
        arr_players.append(line.rstrip())
file.close()
file = open('best_players.txt', 'w')
file.write(arr_players[0] + '\n')
t = 0
if (len(arr_players) == 1):
    file.write('1 ' + name + ' ' + str(points))
else:
    for i in range (1, len(arr_players)):
        inform = arr_players[i].split()
        if int(inform[2]) < points and t==0:
            file.write(inform[0] + ' ' + name + ' ' + str(points) + '\n')
            t = 1
        file.write(str(int(inform[0])+t) + ' ' + inform[1] + ' ' + inform[2] + '\n')
    inform = arr_players[len(arr_players)-1].split()
    if t == 0:
        file.write(str(int(inform[0])+1) + ' ' + name + ' ' +str(points) + '\n')
file.close()
    

