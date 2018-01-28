
from pygame import *
from PlayerState import *
from entity import*
from enemies import*
import math

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = (107, 142, 35)

im = image.load('images/Fire.png')
ANIMATION = []
for i in range(0, 3):
    ANIMATION.append(im.subsurface(32*(3-i), 0, 32, 32))


class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("images/block.jpg")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT-17)

class Angle(sprite.Sprite):
    def __init__(self, x, y, is_right):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        if is_right:
           self.image = image.load("images/angler.jpg")
        else:
            self.image = image.load("images/anglel.jpg")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class BorderBlock(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = Surface((PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.image = image.load("images/stop.png")
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

class TrapState(State):
    def __init__(self):
        super(TrapState, self).__init__(ANIMATION, 0.1)


class Trap(entity):
    hp = 50
    s = TrapState()
    def __init__(self, x, y):
        entity.__init__(self, x, y)

    def update(self):
        self.s.SetAnimation(self)
        if self.hp <= 0:
            self.rect.x = -1000
            self.rect.y = -1000

    def try_water(self, water):
        if sprite.collide_rect(self, water):
            self.hp -= 1

class SpaunState(State):
    def __init__(self):
        super(SpaunState, self).__init__(SPAUN_ANIM, 0.2)

class Spaun(entity):
    hp = 200
    s = SpaunState()
    last_time_mutate = 0
    def __init__(self, x, y):
        super(Spaun, self).__init__(x,y-50)
        self.rect = Rect(x, y-50, 50, 105)
        self.image = Surface((50, 105))
        self.image.set_colorkey(Color(COLOR))
        self.angle = 0

    def update(self, enemies, entities, rand):
        self.s.SetAnimation(self)
        if self.hp <= 0:
            self.rect.x = -1000
            self.rect.y = -1000
        #print(pygame.time.get_ticks() - self.last_time_mutate)
        if pygame.time.get_ticks() - self.last_time_mutate > 2000:
            self.last_time_mutate = pygame.time.get_ticks()
            id = rand%2
            if id == 1:
                y = 30
            else:
                y = 100*math.sin(self.angle)
            x = 100*math.cos(self.angle)
            self.angle += 20*314/100/180
            n_m = self.mutate(id ,self.rect.x+x, self.rect.y+y)
            n_m.obj.rect.x = self.rect.x
            n_m.obj.rect.y = self.rect.y
            enemies.append(n_m)
            entities.add(n_m.obj)

    def try_water(self, water):
        if sprite.collide_rect(self, water):
            self.hp -= 1

    def mutate(self, id, x, y):
        if id == 0:
            new_monst = stupid_monster(x,y)
        if id == 1:
            new_monst = monster_guarder(x,y)
        pf = Decorator(new_monst)
        return pf


class Finish(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y)
        self.image = image.load("images/finish.jpg")



