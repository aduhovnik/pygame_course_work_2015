
from entity import*
import sounds

class Weapon(entity):
    id = 0
    bullets = 0
    damage = 0
    imagel = None
    imager = None
    image = None
    def __init__(self, x, y, bls, dmg, id, imagel, imager):
        entity.__init__(self, x, y)
        self.id = id
        self.bls = bls
        self.dmg = dmg
        self.imager = imager
        self.imagel = imagel

    def update(self, x, y, rotation):
        if rotation:
            self.image = self.imagel
            if self.id == 0:
                self.rect.x = x+15
                self.rect.y = y
            if self.id == 1:
                self.rect.x = x+35
                self.rect.y = y - 5
            if self.id == 2:
                self.rect.x = x+35
                self.rect.y = y - 5
        else:
            self.image = self.imager
            if self.id == 0:
                self.rect.x = x
                self.rect.y = y
            if self.id == 1:
                self.rect.x = x-10
                self.rect.y = y - 5
            if self.id == 2:
                self.rect.x = x-10
                self.rect.y = y - 5

    def play_shoot_sound(self):
        if self.id == 1:
            sounds.Sounds.shoot_sound()
        if self.id == 0:
            sounds.Sounds.baz_bul_start()
    '''def SetWeapon(self, x, y, w):
        self.bullets = w.bullets
        self.image = w.image
        self.damage = w.damage'''
