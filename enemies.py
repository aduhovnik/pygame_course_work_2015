from entity import*
from pygame import *
from EnemyStrategy import*
from globals import *
from PlayerState import *
from EnemyStates import *
from Effects import *


class Mutator(entity):
    def collide(self, bullets, effects, platforms):
        if self.rect.x != -1000 and self.rect.y != -1000:
            for b in bullets:
                if sprite.collide_rect(self, b):
                    self.xp -= b.damage
                    if b.GetRotation():
                        self.rect.x +=30
                    else:
                        self.rect.x -= 30
                    self.rotation = not self.rotation
                    b.used = True
            for ef in effects:
                if ef.id == 0:
                    if sprite.collide_rect(self, ef):
                        self.xp -= 15
            """or p in platforms:
                temp = self;
                if sprite.collide_rect(temp, p):
                    if self.yvel > 0:
                        self.rect.bottom = p.rect.bottom-15
                        self.yvel = 0

                    if self.yvel < 0:
                        self.rect.top = p.rect.bottom
                        self.yvel = 0"""
        if self.xp <= 0:
            abe = EnemyDie(self.rect.x-20, self.rect.y-30)
            effects.append(abe)
            self.rect.x = -1000
            self.rect.y = -1000
            POINTS.ChangePoints(100)


class monster_guarder(Mutator):
    go_l = GlState()
    go_r= GrState()
    def __init__(self, x, y):
        entity.__init__(self, x, y)
        self.width = 90
        self.height = 60
        self.xp = 20
        self.xvel = 1
        self.strategy = SmartEnemyStrategy(1, 20, 0, self.rect.x, self.rect.y, 20)

    def update(self, bullets, x, y, effects, platforms):
        if self.rect.x != -1000 and self.rect.y != -1000:
            if self.rotation:
                self.go_r.SetAnimation(self)
            else:
                self.go_l.SetAnimation(self)
            self.strategy.update(x, y, self)
            self.collide(bullets, effects, platforms)

class Decorator(Mutator):
    def __init__(self, obj):
        self.obj = obj

    def update(self, bullets, x, y, platforms, enemies):
        self.obj.update(bullets, x, y, platforms, enemies)
        draw.line(self.obj.image, (255, 0, 0), (0, 0), (3*self.obj.xp, 0), 5)



class stupid_monster(Mutator):
    anim = None
    st = mState()
    def __init__(self, x, y):
        entity.__init__(self, x, y)
        self.width = 90
        self.height = 60
        self.xp = 10
        self.xvel = 1
        self.strategy = SmartEnemyStrategy(1, 20, 230, self.rect.x, self.rect.y, 20)

    def update(self, bullets, x, y, platforms, enemies):
        self.st.SetAnimation(self)
        if self.rect.x != -1000 and self.rect.y != -1000:
            self.strategy.update(x, y, self)
            self.collide(bullets, platforms, enemies)
        draw.line(self.image, (255, 0, 0), (0, 0), (5*self.xp, 0), 5)