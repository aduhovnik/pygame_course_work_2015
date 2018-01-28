import pygame
import sys
from scores import*

class Menu:
    def __init__(self, punkts = [400, 140, u'Punkt', (250,250, 30), (250, 30, 250), 0]):

        self.punkts = punkts

    def render(self, poverhnost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhnost.blit(font.render(i[2], 1, i[4]), (i[0], i[1]-30))
            else:
                poverhnost.blit(font.render(i[2], 1, i[3]), (i[0], i[1]-30))

    def menu(self,  screen):
        done = True
        font_menu = pygame.font.Font(None, 50)
        pygame.key.set_repeat(1, 1)
        pygame.mouse.set_visible(True)
        punkt = 0
        while done:
            screen.fill((0, 100, 200))

            mp = pygame.mouse.get_pos()
            for i in self.punkts:
                if i[0]+155 > mp[0] > i[0] and i[1]+70 > mp[1] > i[1]-30:
                    punkt = i[5]
            self.render(screen, font_menu, punkt)

            for ee in pygame.event.get():
                if ee.type == pygame.QUIT:
                    sys.exit()
                if ee.type == pygame.KEYDOWN:
                    if ee.key == pygame.K_ESCAPE:
                        sys.exit()
                    if ee.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if ee.key == pygame.K_DOWN:
                        if punkt < len(self.punkts)-1:
                            punkt += 1
                if ee.type == pygame.MOUSEBUTTONDOWN and ee.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        records = HighScores()
                        records.show(screen)
                        pygame.display.flip()
                        pygame.time.wait(2000)
                    elif punkt == 2:
                        sys.exit()

                if ee.type == pygame.K_KP_ENTER and ee.button == 1:
                    if punkt == 0:
                        done = False
                    elif punkt == 1:
                        sys.exit()

            pygame.display.flip()