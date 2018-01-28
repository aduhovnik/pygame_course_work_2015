from game import *
# -*- coding: utf-8 -*-
#вафывфывфы
hasname = False

cl = CurrentLevel()
def main():
    #фывфывфывфы
    screen = pygame.display.set_mode(DISPLAY)
    play = True
    name = ''
    post = ''
    clr = False
    name, clr = inputName(screen, clr)
    print("clr = "+str(clr))
    if clr:
        post = "b"
    print("clr = "+str(clr))
    cl.SetName(name)
    while play:
        game(cl, post)
    if CurrentLevel() > 4:
        CurrentLevel.SetNum(1)


if __name__ == "__main__":
    main()
