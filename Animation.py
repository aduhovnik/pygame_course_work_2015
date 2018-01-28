__author__ = 'Андрей'
import pygame

class Animation:
    def __init__(self, sprites=None, time=100):
        self.sprites = sprites
        self.time = time
        self.workTime = 0
        self.skipFrame = 0
        self.frame = 0

    def update(self, dt):
        self.workTime += dt
        self.skipFrame = self.workTime / self.time
        if self.skipFrame > 0:
            self.workTime = self.workTime % self.time
            self.frame += int(self.skipFrame)
            if self.frame >= len(self.sprites):
                self.frame = 0

    def get_sprite(self):
        return self.sprites[self.frame]