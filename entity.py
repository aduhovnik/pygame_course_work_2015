from pygame import *
from abc import ABCMeta, abstractmethod, abstractproperty


WIDTH = 63
HEIGHT = 61
COLOR =  "#888888"

class entity(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.width = WIDTH
        self.heidht = HEIGHT
        self.xvel = 0
        self.yvel = 0
        self.onGround = False
        self.startX = x
        self.startY = y
        self.image = Surface((self.width, self.heidht))
        self.rect = Rect(x+20, y+20, self.width-30, self.heidht)
        self.image.set_colorkey(Color(COLOR))
        if x > y:
            self.rotation = True
        else:
            self.rotation = False
        self.in_air = True
        self.xp = 100


