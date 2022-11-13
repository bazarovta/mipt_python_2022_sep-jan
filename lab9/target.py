import pygame
import random

class Target:


    def __init__(self, screen: pygame.Surface, x=0, y=0):
        '''Создает объект класс Target.
        screen - поверхность, где отрисовывается объект
        x,y - координаты цели
        vx, vy - скорости цели
        '''
        self.screen = screen
        self.vx = random.randint(-10,10)
        self.vy = random.randint(5,10)
        self.x = x
        self.y = y

    def move(self):
        '''Изменяет координаты цели.'''
        if self.x < 10 or self.x > 790:
            self.vx = -self.vx
        if self.y < 10 or self.y > 550:
            self.vy = -self.vy
        self.x += self.vx * 0.5
        self.y += self.vy * 0.5

    def get_pos(self):
        '''Возвращает координаты цели.'''
        return (self.x, self.y, self.a)

class Target_circle(Target):


    def __init__(self, screen: pygame.Surface, x, y):
        super().__init__(screen, x, y)
        self.a = 10
        self.color = 0xFF03B8

    def draw(self):
        '''Рисует объект.'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.a
        )

class Target_square(Target):


    def __init__(self, screen: pygame.Surface, x, y):
        super().__init__(screen, x, y)
        self.a = 20
        self.color = 0xFF03B8

    def draw(self):
        '''Рисует объект.'''
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x - self.a, self.y - self.a, self.a, self.a)
        )

class Bomber:


    def __init__(self, screen: pygame.Surface):
        '''Создает объект класса Bomber.'''
        self.screen = screen
        self.x = random.randint(15, 785)
        self.y = 30
        self.v = 5
        
    def draw(self):
        '''Рисует объект.'''
        pygame.draw.circle(
            self.screen,
            0xFFC91F,
            (self.x, self.y),
            5
        )
        pygame.draw.line(
            self.screen,
            0xFFC91F,
            [self.x-10, self.y],
            [self.x+10, self.y]
        )
        pygame.draw.line(
            self.screen,
            0xFFC91F,
            [self.x, self.y+10],
            [self.x, self.y-10]
        )
        pygame.draw.line(
            self.screen,
            0xFFC91F,
            [self.x-10, self.y-10],
            [self.x+10, self.y+10]
        )
        pygame.draw.line(
            self.screen,
            0xFFC91F,
            [self.x-10, self.y+10],
            [self.x+10, self.y-10]
        )

    def move(self):
        '''Изменяет координаты.'''
        if self.x<15 or self.x>785:
            self.v = -self.v
        self.x += self.v*0.5

    def throw_target(self):
        '''Создает новую цель.'''
        t = random.randint(0,1)
        if t == 0:
            return Target_circle(self.screen, self.x, self.y)
        else:
            return Target_square(self.screen, self.x, self.y)



