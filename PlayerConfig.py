from pygame import *
import game
MOVE_SPEED = 4
JUMP_POWER = 9
GRAVITY = 0.70
WIDTH = 63
HEIGHT = 61
COLOR =  "#888888"
ANIMATION_DELAY = 0.10
xlen = 61
ylen = 61
ANIMATION_LEFT = []
ANIMATION_JUMP_LEFT = []
ANIMATION_JUMP_RIGHT= []
ANIMATION_RIGHT=[]
ANIMATION_STAYR = []
ANIMATION_STAYL = []
ANIMATION_SHOOT_RIGHT = []
ANIMATION_SHOOT_LEFT = []
def set_anim_every(post):
    print(post)
    r = image.load('images/player/move_r'+post+'.png')
    l = image.load('images/player/move_l'+post+'.png')
    shr = image.load('images/shootr'+post+'.png')
    shl = image.load('images/shootl'+post+'.png')
    sr = image.load('images/player/stayr'+post+'.png')
    sl = image.load('images/player/stayl'+post+'.png')
    jl = image.load('images/player/jump_l'+post+'.png')
    jr = image.load('images/player/jump_r'+post+'.png')
    ANIMATION_JUMP_LEFT.append(jl)
    ANIMATION_JUMP_RIGHT.append(jr)
    for i in range(0, 3):
        ANIMATION_LEFT.append(l.subsurface(xlen*(3-i), 0, xlen, ylen))
    for i in range(0, 3):
        ANIMATION_RIGHT.append(r.subsurface(xlen*i, 0, xlen, ylen))
    ANIMATION_STAYR.append(sr)
    ANIMATION_STAYL.append(sl)
    for i in range(1, 2):
        ANIMATION_SHOOT_RIGHT.append(shr.subsurface(i*65, 0, 65, 65))
    for i in range(1, 2):
        ANIMATION_SHOOT_LEFT.append(shl.subsurface((2-i)*65, 0, 65, 65))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
bbl  = image.load('images/baz_bul.png')
ANIM_BAZ_BUL_LEFT = []
for i in range(0,2):
    ANIM_BAZ_BUL_LEFT.append(bbl.subsurface(i*47, 0, 47, 27))

bbr = image.load('images/baz_bur.png')
ANIM_BAZ_BUL_RIGHT = []
for i in range(0,2):
    ANIM_BAZ_BUL_RIGHT.append(bbr.subsurface(i*47, 0, 47, 27))

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
xp_image = image.load('images/xp_bar.png')

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
explsn = image.load('images/expln.png')
EXPL_ANIM = []
for i in range(0,12):
    EXPL_ANIM.append(explsn.subsurface(i*39, 0, 39, 40))

abe = image.load('images/abe.png')
ABE_ANIM = []
for i in range(0,9):
    ABE_ANIM.append(abe.subsurface(i*64, 0, 64, 63))

eda = image.load('images/enemy_die.png')
ENEMY_DIE_ANIM = []
for i in range(0,8):
    ENEMY_DIE_ANIM.append(eda.subsurface(i*64, 0, 64, 63))

spaun = image.load('images/spaun.png')
SPAUN_ANIM = []
for i in range(0, 3):
    SPAUN_ANIM.append(spaun.subsurface(i*50, 0, 50, 105))
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
wl  = image.load('images/wodal.png')
ANIM_WL = []
for i in range(0,5):
    ANIM_WL.append(wl.subsurface(i*60, 0, 60, 35))

wr = image.load('images/wodar.png')
ANIM_WR = []
for i in range(0,5):
    ANIM_WR.append(wr.subsurface((5-i)*60, 0, 60, 35))