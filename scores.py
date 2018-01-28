import  pygame
# -*- coding: utf-8 -*-
def SortByScore(inputStr):
    start = inputStr.find(':')
    end = inputStr.find('\n')
    num = inputStr[start+3:end]
    return int(num)

class HighScores:
    records = []
    r = {}
    inf_font = pygame.font.Font(None, 24)
    b_font = pygame.font.Font(None, 45)
    count = 1
    MinScore = 0

    def __init__(self):
        ScoreFile = open('Records.txt', 'r')
        for line in ScoreFile:
            self.records.append(line)
        self.records.sort(key = SortByScore, reverse=True)
        ScoreFile.close()

    def show(self, screen):
        screen.fill((0, 100, 200))
        screen.blit(self.b_font.render((u'Таблица рекордов ( top 10 )'), 1, (255, 0, 0)), (100, 50))
        i = 1
        self.records.sort(key = SortByScore, reverse=True)
        for line in self.records:
            if i < 11:
                end = line.find('\n')
                screen.blit(self.inf_font.render((u'%s'%line[0:end]), 1, (255, 0, 0)), (300, 30*i+100))
            i+=1
        self.records.clear()

    def save(self):
        ScoreFile = open('Records.txt', 'w')
        for line in self.records:
            ScoreFile.write(str(line))
        ScoreFile.write(str('\n'))
        ScoreFile.close()

    def AddRecord(self, name, score):
        self.records.append(name+':  '+str(score))
        self.save()
        self.records.clear()


