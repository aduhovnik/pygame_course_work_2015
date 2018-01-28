from PlayerConfig import*
import pyganim
from entity import *

class State(sprite.Sprite):
    animation = None
    def __init__(self, Anim, Anim_Delay):
        boltAnim = []
        for anim in Anim:
            boltAnim.append((anim, Anim_Delay))
            self.animation = pyganim.PygAnimation(boltAnim)
            self.animation.play()

    def SetAnimation(self, player):
        player.image.fill(Color(COLOR))
        player.animation = self.animation
        player.animation.blit(player.image, (0, 0))


class PlayerStateStay(State):
    def __init__(self, rotation):
        if rotation:
            super(PlayerStateStay, self).__init__(ANIMATION_STAYR, ANIMATION_DELAY)
        else:
            super(PlayerStateStay, self).__init__(ANIMATION_STAYL, ANIMATION_DELAY)

class PlayerStateGo(State):
    def __init__(self, rotation):
        if rotation:
            super(PlayerStateGo, self).__init__(ANIMATION_RIGHT, ANIMATION_DELAY)
        else:
            super(PlayerStateGo, self).__init__(ANIMATION_LEFT, ANIMATION_DELAY)

class PlayerStateJump(State):
    def __init__(self, rotation):
        if rotation:
            super(PlayerStateJump, self).__init__(ANIMATION_JUMP_RIGHT, ANIMATION_DELAY)
        else:
            super(PlayerStateJump, self).__init__(ANIMATION_JUMP_LEFT, ANIMATION_DELAY)

class PlayerStateShoot(State):
    def __init__(self, rotation):
        if rotation:
            super(PlayerStateShoot, self).__init__(ANIMATION_SHOOT_RIGHT, ANIMATION_DELAY)
        else:
            super(PlayerStateShoot, self).__init__(ANIMATION_SHOOT_LEFT, ANIMATION_DELAY)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def baz_bul(rotation, bul):
    if rotation:
        s = State(ANIM_BAZ_BUL_RIGHT, ANIMATION_DELAY*10)
    else:
        s = State(ANIM_BAZ_BUL_LEFT, ANIMATION_DELAY*10)
    bul.SetAnimation(s.animation)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class WaterState(State):
    def __init__(self, rotation):
        if rotation:
            super(WaterState, self).__init__(ANIM_WR, ANIMATION_DELAY)
        else:
            super(WaterState, self).__init__(ANIM_WL, ANIMATION_DELAY)

class Water(entity):
    s = None
    sr =  WaterState(True)
    sl = WaterState(False)
    rotation = False

    def __init__(self, x, y, rotation):
        entity.__init__(self, x, y)
        self.rotation = rotation

    def update(self, x, y, rotation):
        if rotation:
            self.sr.SetAnimation(self)
            self.rect.x = x+70
        else:
            self.sl.SetAnimation(self)
            self.rect.x = x-70
        self.rect.y = y
