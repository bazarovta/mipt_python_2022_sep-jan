import pygame

CYAN = 0x00FFCC

class Ammo:

    
    def __init__(self, screen: pygame.Surface, x=0, y=0, vx=15, vy=10):
        '''Создает объект класса Ammo.
        screen - поверхность, где отрисовывается объект
        x,y - координаты объекта на поверхности
        vx, vy - скорости объекта
        a - параметр, отвечающий за размер объекта
        live - параметр, показывающий состояние объекта
        colot - цвет объекта
        self.screen = screen
        '''
        self.screen = screen
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.a = 0
        self.live = 1
        self.color = CYAN
        
    def move(self, k):
        '''Изменяет координаты объекта.
        k - коэффициент сопротивления в среде.
        '''
        dt = 0.3 #промежуток времени
        g = 5 #ускорение свободного падения
        if self.live == 1:
            if self.x < 5:
                self.vx = -self.vx
            elif self.x > 795:
                self.vx = -self.vx
            if self.y > 550:
                self.y = 550
                self.live = 0
            else:
                self.x += self.vx*dt
                self.y += self.vy*dt
                self.vx -= k*self.vx*dt
                self.vy += g*dt - k*self.vy*dt

    def get_pos(self):
        '''Возвращает координаты объекта'''
        return (self.x, self.y, self.a)

class Ammo_circle(Ammo):


    def __init__(self, screen: pygame.Surface, x=0, y=0, vx=10, vy=10):
        '''Создает объект класса Ammo_circle.'''
        super().__init__(screen, x, y, vx, vy)
        self.a = 5

    def move(self):
        k = 0.01
        super().move(k)

    def draw(self):
        '''Отрисовывает объект.'''
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.a
        )

class Ammo_square(Ammo):


    def __init__(self, screen: pygame.Surface, x=0, y=0, vx=10, vy=10):
        '''Создает объект класса Ammo_square.'''
        super().__init__(screen, x, y, vx, vy)
        self.a = 10

    def move(self):
        k = 0.05
        super().move(k)

    def draw(self):
        '''Отрисовывет объект.'''
        pygame.draw.rect(
            self.screen,
            self.color,
            (self.x + 5 - self.a, self.y -self.a + 5, self.a, self.a)
        )

