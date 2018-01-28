from pygame import *
import pyganim
import sounds
from entity import*
from bullet import*
from PlayerState import*
from  HealthBar import *
from Weapon import *
from Effects import *
from blocks import *

class Player(entity):

    obj = None
    animation = None
    win = False

    ajr = PlayerStateJump(True)
    ajl = PlayerStateJump(False)
    agr = PlayerStateGo(True)
    agl = PlayerStateGo(False)
    asr = PlayerStateStay(True)
    asl = PlayerStateStay(False)
    ashr = PlayerStateShoot(True)
    ashl = PlayerStateShoot(False)

    rpgr = image.load("images/rpg.png")
    rpgl = image.load("images/rpgl.png")
    pstl = image.load("images/pstl.png")
    pstr = image.load("images/pstr.png")
    bfr = image.load("images/firebreaker.png")
    bfl = image.load("images/firebreakel.png")

    rpg = Weapon(0, 0, 20, 15, 0, rpgr, rpgl)
    pst = Weapon(0, 0, 100, 3, 1, pstr, pstl)
    fbr = Weapon(0, 0, float("Inf"), 3, 2, bfr, bfl)
    weap_list = []
    weap_list.append(rpg)
    weap_list.append(pst)
    weap_list.append(fbr)
    w_num = 1
    w_num_max =3
    xp = 100

    def __init__(self, x, y):
        if self.obj is None:
            super(Player, self).__init__(x, y)
            self.fires = False
            self.obj = object.__init__(x, y)
            self.weapon = self.pst
        return self.obj

    def SetAnimEvery(self, post):
        set_anim_every(post)
        self.ajr = PlayerStateJump(True)
        self.ajl = PlayerStateJump(False)
        self.agr = PlayerStateGo(True)
        self.agl = PlayerStateGo(False)
        self.asr = PlayerStateStay(True)
        self.asl = PlayerStateStay(False)
        self.ashr = PlayerStateShoot(True)
        self.ashl = PlayerStateShoot(False)

    def change_weapon(self):
        sounds.Sounds.change_weapon_sound()
        self.w_num = (self.w_num+1)%self.w_num_max
        self.weapon = self.weap_list[self.w_num]

    def update(self,  left, right, up, shoot, platforms, traps, enemies, bonuses, effects):
        if left:
           self.rotation = False
           self.xvel = -MOVE_SPEED
           if not self.in_air:
               self.agl.SetAnimation(self)
           else:
               self.ajl.SetAnimation(self)

        if right:
            self.rotation = True
            self.xvel = MOVE_SPEED
            if not self.in_air:
                self.agr.SetAnimation(self)
            else:
                self.ajr.SetAnimation(self)

        if up:
            if self.onGround:
                self.yvel = -JUMP_POWER
            if self.rotation:
                self.ajr.SetAnimation(self)
            else:
                self.ajl.SetAnimation(self)

        if not(left or right):
            self.xvel = 0
            if self.rotation:
                self.asr.SetAnimation(self)
            else:
                self.asl.SetAnimation(self)

        if shoot:
            self.weapon.update(self.rect.x, self.rect.y+15, self.rotation)
            if self.rotation:
                 self.ashr.SetAnimation(self)
            else:
                 self.ashl.SetAnimation(self)
            time.Clock().tick(400)
        else:
            self.weapon.update(-1000, -1000,self.rotation)

        if not self.onGround:
            self.yvel += 0.3*GRAVITY

        if self.xp <= 0:
            self.xp = 100
            self.rect.x = 80
            self.rect.y = 100
            POINTS.ChangePoints(-200)

        self.onGround = False
        self.rect.y += self.yvel
        self.collide(0, self.yvel, platforms, traps, enemies, bonuses, effects)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, platforms, traps, enemies, bonuses, effects)

    def collide(self, xvel, yvel, platforms, traps, enemies, bonuses, effects):

        for bnss in bonuses:
            if sprite.collide_rect(self, bnss):
                sounds.Sounds.GetBonus()
                abe = AfterBonus(bnss.rect.x-20, bnss.rect.y-30)
                bnss.GetBonus(self)
                effects.append(abe)

        for e in enemies:
            if sprite.collide_rect(self, e.obj):
                sounds.Sounds.trap_found()
                self.xp -= 50
                if self.rotation:
                    self.rect.x -= 50
                else:
                    self.rect.x += 50
                self.yvel = -JUMP_POWER*0.5

        for t in traps:
            if sprite.collide_rect(self, t):
                sounds.Sounds.trap_found()
                self.xp -= 30
                if self.rotation:
                    self.rect.x -= 50
                else:
                    self.rect.x += 50
                self.yvel = -JUMP_POWER*0.5
        for p in platforms:
            temp = self;
            if sprite.collide_rect(temp, p):

                if xvel > 0:
                    self.rect.right = p.rect.left

                if xvel < 0:
                    self.rect.left = p.rect.right

                if yvel > 0:
                    self.rect.bottom = p.rect.bottom-15
                    self.onGround = True
                    self.in_air = False
                    self.yvel = 0

                if yvel < 0:
                    self.rect.top = p.rect.bottom
                    self.yvel = 0

    def fire(self, bullets, f_up, f_dwn):
        if self.weapon.bls > 0:
            self.weapon.play_shoot_sound()
            if self.weapon.id == 0:
                b = Bullet(self.rect.x, self.rect.y, self.rotation, False, False, self.weapon.id)
                b.damage = self.weapon.dmg
                b.id = self.weapon.id
                baz_bul(self.rotation, b)
            if self.weapon.id == 1:
                if self.weapon.id == 1:
                    b = Bullet(self.rect.x, self.rect.y, self.rotation, f_up, f_dwn, self.weapon.id)
            if self.weapon.id == 2:
                pass
            self.weapon.bls -= 1
            if self.weapon.id != 2:
                bullets.append(b)
            print(self.weapon.id)

    def GetWin(self):
        return self.win


