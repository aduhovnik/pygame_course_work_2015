from pygame import *
from PlayerState import *
from entity import*

class ExplsnState(State):
    def __init__(self):
        super(ExplsnState, self).__init__(EXPL_ANIM, ANIMATION_DELAY)

class AfterBonusEffect(State):
    def __init__(self):
        super(AfterBonusEffect, self).__init__(ABE_ANIM, ANIMATION_DELAY/2)

class EnemyDieEffect(State):
    def __init__(self):
        super(EnemyDieEffect, self).__init__(ENEMY_DIE_ANIM, ANIMATION_DELAY*2)
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

class Effect(entity):
    id = -1
    start_time = 0
    end_time = 0
    s = None
    def __init__(self, x, y):
        super(Effect, self).__init__(x,y)
        self.start_time = time.get_ticks()

    def update(self):
        pass

    def update(self):
        self.s.SetAnimation(self)
        s = time.get_ticks()-self.start_time
        if s > self.end_time:
            self.rect.x = -1000
            self.rect.y = -1000

class Explosion(Effect):
    id = 0
    end_time = 900
    s = ExplsnState()

class AfterBonus(Effect):
    s = AfterBonusEffect()
    end_time = 350

class EnemyDie(Effect):
    s = EnemyDieEffect()
    end_time = 600