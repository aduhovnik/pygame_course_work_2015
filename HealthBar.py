from pygame import *
from entity import *

rect_1_color = (255, 0, 0)
rect_2_color = (0, 0, 255)

class HealthBar(entity):
    x = 0
    y = 0
    rect_1 = ((0, 0),(100, 30))
    rect_2 = rect_1
    width_1 = 0
    width_2 = 3

    def __init__(self, x, y):
        super(HealthBar, self).__init__(x, y)
        self.height = 5
        self.width = 50
        self.rect = Rect(x, y, self.width, self.heidht)
        self.image = Surface((self.width, self.height))
        self.image.fill((255, 255, 255))
        draw.line(self.image, rect_1_color, (0, 0), (50, 0), 20)

    def update(self,x, y, health):
        self.width = abs(health/2)
        self.image = Surface((self.width, self.height))
        self.rect.width = health/2
        self.rect.x = x
        self.rect.y = y
        self.image.fill((255, 255, 255))
        draw.line(self.image, rect_1_color, (0, 0), (health/2, 0), 20)


