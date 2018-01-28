# -*- coding: utf-8 -*-
__author__ = 'Андрей'

from pygame import *
from PlayerState import *
from entity import*
from blocks import *

class Bonus(entity):
    x0 = 0
    y0 = 0
    up = False
    stop = True
    vy = 0
    vy_max = 0
    def __init__(self, x, y, rand):
        super(Bonus, self).__init__(x,y)
        self.y0 = y
        self.vy_max = rand/30+1

    def GetBonus(self, player):
        pass

    def update(self):
        if self.stop:
            self.vy = -self.vy_max
            self.stop = False
            self.up = True

        if self.up:
            self.vy += 0.1
            self.rect.y += self.vy
            if self.vy > 0:
                self.up = False
        else:
            self.vy += 0.1
            self.rect.y += self.vy
            if self.rect.y > self.y0:
                self.stop = True


xp_image = image.load('images/xp_bar.png')

class Chest(Bonus):
    inc_hp = 0
    def __init__(self, x, y, inc):
        super(Chest, self).__init__(x,y, inc)
        self.inc_hp = inc
        self.image = xp_image

    def GetBonus(self, player):
        delta = 200 - player.xp
        if player.xp + self.inc_hp < 200:
            player.xp += self.inc_hp
        else:
            player.xp = 200
        self.rect.x = -1000
        self.rect.y = -1000

class WeaponCrate(Bonus):
    inc_bullets = 0
    weapon_id = -1
    def __init__(self, x, y, inc, id):
        super(WeaponCrate,self).__init__(x,y, inc)
        self.inc_bullets = inc
        self.weapon_id = id
        self.image = image.load('images/WeaponCrate'+str(id)+'.png')

    def GetBonus(self, player):
        player.weap_list[self.weapon_id].bls += self.inc_bullets;
        self.rect.x = -1000
        self.rect.y = -1000

