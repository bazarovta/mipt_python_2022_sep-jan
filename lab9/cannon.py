import pygame
import random
import math
import ammo

RED = 0xFF0000
GREEN = 0x00FF00
BLACK = (0, 0, 0)

class Cannon:
    

    def __init__(self, screen: pygame.Surface):
        '''Создает объект класса Cannon.
        screen - поверхность, где отрисовывается объект
        power - коээфициент, который показывает потенциал снаряда в пушке
        on - переменная, показывающая состояние пушки
        angle - угол, под которым целится дуло пушки
        v - скорость пушки
        x,y - координаты центра пушки
        mouse_x, mouse_y - координаты мышки
        '''
        self.screen = screen
        self.power = 25.
        self.on = 0
        self.angle = 1.
        self.v = 10
        self.x = random.randint(50, 750)
        self.y = 550
        self.mouse_x = 0
        self.mouse_y = 0

    def fire_start(self):
        '''Начинает заряд пушки.'''
        self.on = 1

    def fire_end(self):
        '''Описывает действие выстрела. Возвращает объект класса Ammo_circle
        или Ammo_square. Возвращает состояние пушки в исходное положение.
        '''
        if random.randint(0,1) == 0:
            ammo_ = ammo.Ammo_circle(
                self.screen, self.x, self.y-25,
                (self.power+25)*math.cos(self.angle),
                -(self.power+25)*math.sin(self.angle)
            )
        else:
            ammo_ = ammo.Ammo_square(
                self.screen, self.x, self.y-25,
                (self.power+25)*math.cos(self.angle),
                -(self.power+25)*math.sin(self.angle)
        )
        self.power = 25
        self.on = 0
        return ammo_

    def targetting(self, pos, check):
        '''Изменяет угол, под которым смотрит пушка.
        pos - tupple(int,int), координаты мышки
        check -
        '''
        self.mouse_x = pos[0]
        self.mouse_y = pos[1]
        if self.power <= 75 and self.on == 1 and check == 1:
            self.power += 0.5
        if pos[0] == self.x:
            self.angle = math.pi/2
        else:
            self.angle = math.atan((self.y - pos[1]) / (pos[0] - self.x))
            if self.angle < 0:
                self.angle += math.pi

    def move(self):
        '''Изменяет координаты пушки.'''
        if self.x < 50:
            self.v = 10
        elif self.x > 750:
           self.v = -10
        self.x += int(self.v*0.25)

    def draw(self):
        '''Отрисовывет пушку.'''
        self.targetting((self.mouse_x, self.mouse_y), 1)
        pygame.draw.polygon(
            self.screen,
            GREEN,
            [(self.x-50, self.y), (self.x+50, self.y),
            (self.x+50, self.y-25), (self.x-50, self.y-25)]
        )
        if self.on == 1:
            pygame.draw.polygon(
                self.screen,
                RED,
                [[self.x-4, self.y-25],
                 [self.x+4, self.y-25],
                 [self.x+4 + math.cos(self.angle)*self.power,
                    self.y-25 - math.sin(self.angle)*self.power],
                 [self.x-4 + math.cos(self.angle)*self.power,
                    self.y-25 - math.sin(self.angle)*self.power]]
            )
        else:
            pygame.draw.polygon(
                self.screen,
                BLACK,
                [[self.x-4, self.y-25],
                 [self.x+4, self.y-25],
                 [self.x+4 + math.cos(self.angle)*25,
                    self.y-25 - math.sin(self.angle)*25],
                 [self.x-4 + math.cos(self.angle)*25,
                    self.y-25 - math.sin(self.angle)*25]]
                 )



        
