# -*- coding: utf-8 -*-
__author__ = 'Андрей'
import pygame
class SavingContext:
    saves = []
    inf_font = pygame.font.Font(None, 24)
    b_font = pygame.font.Font(None, 45)
    count = 1

    def __init__(self):
        SFile = open('saves.txt', 'r')
        for line in SFile:
            self.saves.append(line)
        SFile.close()

    def save(self):
        SFile = open('saves.txt', 'w')
        for line in self.saves:
            SFile.write(str(line))
        SFile.write(str('\n'))
        SFile.close()

    def Add(self, name, cLevel, Points, xp, bullets):
        for line in self.saves:
            if line[0:line.find(' ')] == name:
                self.saves.remove(line)
        self.saves.append(name+' '+cLevel+' '+Points+' '+xp+' '+bullets)
        self.save()
        self.saves.clear()


