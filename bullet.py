from entity import *
from globals import *
from Effects import *
import sounds

class Bullet(entity):
    id = -1
    def __init__(self, x, y, rotation, up, dwn, id):
        super(Bullet, self).__init__(x, y)
        self.used = False
        self.rotation = rotation
        self.damage = 3
        if rotation:
            delta = 20
        else:
            delta = -20
        if id == 0:
            self.rect.height = 28
            self.rect.width = 47
            self.rect = Rect(x+delta, y+10, 47, 27)
            if rotation:
                self.xvel = 20
            else:
                self.xvel = -20

        self.image.fill(Color(COLOR))

        if up:
            self.yvel = 5
        if not id == 0:
            self.rect.height = 26
            self.rect.width = 36
            self.rect = Rect(x+delta, y+10, self.width-60, self.heidht-20)
            if rotation:
                if up:
                    self.yvel = 5
                    self.image = image.load("images/bulru.png")
                elif dwn:
                    self.yvel = -5
                    self.image = image.load("images/bulrd.png")
                else:
                    self.image = image.load("images/bulr.png")
                self.xvel = 10
                self.rect.x += 10
            else:
                if up:
                    self.yvel = 5
                    self.image = image.load("images/bullu.png")
                elif dwn:
                    self.yvel = -5
                    self.image = image.load("images/bulld.png")
                else:
                    self.image = image.load("images/bull.png")
                self.xvel = -10
        self.rect.x += self.xvel

    def SetAnimation(self, anim):
        self.image.fill(Color(COLOR))
        self.animation = anim
        self.animation.blit(self.image, (0, 0))


    def update(self, platforms, effects):
        if self.rect.x != -1000 and self.rect.y != -1000:
            self.rect.x += self.xvel
            self.rect.y -= self.yvel
            self.collide(platforms, effects)
            if self.used:
                if self.id == 0:
                    sounds.Sounds.baz_expls()
                    explsn = Explosion(self.rect.x, self.rect.y-20)
                    effects.append(explsn)
                self.rect.x = -1000
                self.rect.y = -1000


    def collide(self, platforms, effects):
        for pf in platforms:
            if sprite.collide_rect(self, pf):
                if self.id == 0:
                    sounds.Sounds.baz_expls()
                    explsn = Explosion(self.rect.x, self.rect.y-20)
                    effects.append(explsn)
                self.rect.x = -1000
                self.rect.y = -1000

    def can_del(self):
        if self.rect.x == -1000 and self.rect.y == -1000:
            return True
        else:
            return False

    def GetRotation(self):
        return self.rotation