import pygame

class Strategy(object):
    speed = 2
    damage = 0
    def __init__(self, speed, damage):
        self.speed = speed
        self.damage = damage

class RestStrategy(Strategy):
    y = None
    x = None
    x_max = None
    def __init__(self, s, d, c_x, c_y, x_max):
        super(RestStrategy, self).__init__(s, d)
        self.x = c_x
        self.y = c_y
        self.x_max = x_max

    def update(self, e):
        if e.rect.y >= self.y:
            e.yvel = -self.speed
        if e.rect.y < self.y:
            e.yvel = self.speed
        if e.rect.y == self.y:
            e.yvel = 0
        e.rect.y += e.yvel

        if self.x - self.x_max < e.rect.x < self.x + self.x_max:
            e.rect.x += e.xvel
        else:
            if e.rect.x > self.x+self.x_max:
                e.xvel = -self.speed
                e.rotation = False
            if e.rect.x  < self.x-self.x_max:
                e.xvel = self.speed
                e.rotation = True
            e.rect.x += e.xvel

class AggressiveStrategy(Strategy):
    def __init__(self, r, s):
        super(AggressiveStrategy, self).__init__(r, s+1)
        #Strategy.__init__(r, s+1)

    def update(self, e, hx, hy):
        if hx <= e.rect.x and hy <= e.rect.y:
             e.rect.x += -self.speed
             e.rect.y += -self.speed
        if hx <= e.rect.x and hy >= e.rect.y:
             e.rect.x += -self.speed
             e.rect.y += +self.speed
        if hx >= e.rect.x and hy <= e.rect.y:
             e.rect.x += +self.speed
             e.rect.y += -self.speed
        if hx >= e.rect.x and hy >= e.rect.y:
             e.rect.x += self.speed
             e.rect.y += self.speed

class SmartEnemyStrategy():
    Agr = None
    Pat = None
    def __init__(self, s, d, r, c_x, c_y, x_max):
        self.s = s
        self.d = d
        self.r = r
        self.Agr = AggressiveStrategy(s, d)
        self.Pat = RestStrategy(s, d, c_x, c_y, x_max)
        self.str = self.Pat

    def update(self, x, y, e):
        if abs(e.rect.x - x) < self.r and abs(e.rect.y - y) < self.r:
            self.str = self.Agr
            self.str.update(e, x, y)
        else:
            self.str = self.Pat
            self.str.update(e)



