from pygame import *
from PlayerState import*
m = image.load('images/fly_monster.png')
ANIMATION = []
for i in range(0, 5):
    ANIMATION.append(m.subsurface(32*i, 0, 32, 32))

gr = image.load('images/guarder.png')
G_R_ANIMATION = []
for i in range(0, 5):
    G_R_ANIMATION.append(gr.subsurface(32*i, 0, 32, 32))

gl = image.load('images/guardel.png')
G_l_ANIMATION = []
for i in range(0, 5):
    G_l_ANIMATION.append(gl.subsurface(32*i, 0, 32, 32))

class GrState(State):
    def __init__(self):
        super(GrState, self).__init__(G_R_ANIMATION, 0.1)

class GlState(State):
    def __init__(self):
        super(GlState, self).__init__(G_l_ANIMATION, 0.1)

class mState(State):
    def __init__(self):
        super(mState, self).__init__(ANIMATION, 0.1)
