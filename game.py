
import pygame
from pygame import *
from player import Player
from blocks import *
import sounds
import menu
from camera import *
from enemies import *
from HealthBar import *
from globals import*
from scores import*
from savingcontext import *
from Bonuses import *
import math

pygame.init()

timer = pygame.time.Clock()

def loadLevel(num, level):

    levelFile = open('levels/%s.txt'%num)

    line = levelFile.readline()
    count = int(line)
    for i in range(0, count-1):
        line = str(levelFile.readline())
        level.append(line)

def loadBackGround(num, level_b, background):
    background = image

def camera_configure(camera, target_rect):
        l, t, _, _ = target_rect
        _, _, w, h = camera
        l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

        l = min(0, l)
        l = max(-(camera.width-WIN_WIDTH), l)
        t = max(-(camera.height - WIN_HEIGHT), t)
        t = min(0, t)

        return Rect(l, t, w, h)

class CurrentLevel():
    num = 1
    check = True
    name = ''
    def __init__(self):
        pass

    def SetNum(self, num):
        self.num = num

    def SetName(self, name):
        self.name = name

    def GetNum(self):
        return self.num

    def GetName(self):
        return self.name

def parse_level(level, entities, platforms, enemies, traps, finish, bonuses, spauns):
    x=y=0 
    for row in level:
                for col in row:
                     if col == "-":
                        pf = Platform(x, y)
                        entities.add(pf)
                        platforms.append(pf)
                     if col == "b":
                         pf = BorderBlock(x, y)
                         entities.add(pf)
                         platforms.append(pf)
                     if col == "_":
                         pf = Platform(x, y)
                         entities.add(pf)
                     if col == "r":
                        pf = Angle(x, y, True)
                        entities.add(pf)
                        platforms.append(pf)
                     if col == "l":
                        pf = Angle(x, y, False)
                        entities.add(pf)
                        platforms.append(pf)
                     if col == "g":
                        #mc.set_monster(sm)
                        #mc.create_monster(x, y)
                        p = monster_guarder(x, y-20)
                        pf = Decorator(p)
                        entities.add(pf.obj)
                        enemies.append(pf)
                     if col == "m":
                        #mc.set_monster(sm)
                        #mc.create_monster(x, y)
                         p = stupid_monster(x, y-40)
                         pf = Decorator(p)
                         entities.add(pf.obj)
                         enemies.append(pf)
                     if col == "s":
                         pf = Spaun(x,y)
                         entities.add(pf)
                         spauns.append(pf)
                     if col == "*":
                         pf = Trap(x, y-20)
                         entities.add(pf)
                         traps.append(pf)
                     if col == "f":
                         pf = Finish(x, y)
                         entities.add(pf)
                         finish.rect.x = pf.rect.x
                         finish.rect.y = pf.rect.y
                     if col == "h":
                         pf = Chest(x,y-5, (x+y)%50+time.get_ticks()%30+20)
                         entities.add(pf)
                         bonuses.append(pf)
                     if col == "1":
                         pf = WeaponCrate(x, y - 5, ((x+y)%10+time.get_ticks()%10)*2+10, 1)
                         entities.add(pf)
                         bonuses.append(pf)
                     if col == "0":
                         pf = WeaponCrate(x, y, ((x+y)%10+time.get_ticks()%10)+5, 0)
                         entities.add(pf)
                         bonuses.append(pf)
                     x += PLATFORM_WIDTH
                y += PLATFORM_HEIGHT
                x = 0

def inputName(screen, clr):
    """

    :type screen: object
    """
    do = True
    name = ''
    plus = ''
    inputed_name = False
    info_string = pygame.Surface((300, 150))
    info_string.fill(Color(COLOR))
    inf_font = pygame.font.Font(None, 36)
    small_inf_font = pygame.font.Font(None, 20)
    bgi = image.load('images/load.png')
    bg = image.load('images/background1.jpg')
    high = False
    tm = time.get_ticks()
    while do:
        for e in pygame.event.get():
            if e.type == QUIT:
                go = False
            if e.type == KEYUP and e.key == K_SPACE:
                if name.__len__() > 0 and inputed_name:
                    do = False
                    return name, False
                if name.__len__() > 0 and not inputed_name:
                    inputed_name = True
            if e.type == KEYUP and e.key == 8:
                name = name[0:-1]
            if e.type == KEYUP and e.key == K_CAPSLOCK:
                high = not high
            if e.type == KEYUP and e.key > 96 and e.key < 123:
                if high:
                    name+= chr(e.key-32)
                else:
                    name+=chr(e.key)
            if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
                sys.exit()
            if inputed_name and e.type == KEYUP and e.key == K_KP_PLUS:
                return name, True
        screen.blit(bg, (0, 0))
        screen.blit(bgi, (0, 0))
        draw.ellipse(screen, (155,155,155), ((270, 240),(370, 80)), 0)
        if not inputed_name:
            screen.blit(inf_font.render(u'    Input name: ', 1, (0, 0, 0)), (300, 250))
            screen.blit(small_inf_font.render(u'    %s '%name, 1, (0, 0, 0)), (400-name.__len__()*2.5, 275))
        else:
            screen.blit(small_inf_font.render(u'         ', 1, (0, 0, 0)), (300, 260))
            screen.blit(small_inf_font.render(u"            (name shouldn't be empty) ", 1, (0, 0, 0)), (300, 275))
        if name.__len__() > 0 and time.get_ticks()%1000 < 500:
            screen.blit(small_inf_font.render(u'    press space ', 1, (100, 100, 100)), (340, 290))
        pygame.display.flip()

hasname = False

def ShowIfDie(screen, hero, score):
    go = True
    r = 0
    while(go):
        draw.circle(screen, (0,0,0), (500, 300), r, 0)
        r+=10
        time.wait(10)
        pygame.display.flip()
        if r >= 710:
            go = False
    go = True
    start_time = time.get_ticks()
    big_inf_font = pygame.font.Font(None, 60)
    small_inf_font = pygame.font.Font(None, 30)
    Effects = []
    for i in range(0, 150):
        pf = Explosion((i*i*300)%1000, (i*200)%500)
        pf.end_time = 3000
        Effects.append(pf)
    for i in range(0, 150):
        pf = AfterBonus((i*i*270)%1000, (i*160)%500)
        pf.end_time = 3000
        Effects.append(pf)
    for i in range(0, 150):
        pf = EnemyDie((i*i*i*330)%1000, (i*240)%500)
        pf.end_time = 3000
        Effects.append(pf)
    while(go):
        tm = (time.get_ticks() - start_time)
        print(str(tm))
        if tm > 2300:
            go = False
        time.wait(10)
        draw.circle(screen, (0,0,0), (500, 300), r, 0)
        if time.get_ticks()%1000 < 200:
            sounds.Sounds.baz_expls()
        for pf in Effects:
            pf.update()
            screen.blit(pf.image, (pf.rect.x, pf.rect.y))
        screen.blit(big_inf_font.render(u'Game over! ', 1, (255, 255, 255)), (380, 200))
        screen.blit(small_inf_font.render(u'Your score: '+str(score), 1, (150, 150, 150)), (400, 250))
        pygame.display.flip()
    hero.weap_list[0].bls = 20
    hero.weap_list[1].bls = 100

clr = False

def game(CURRENT_LEVEL, post):
    global hasname
    hero = Player(55,55)
    entities = pygame.sprite.Group()
    platforms = []
    traps = []
    enemies = []
    bullets = []
    effects = []
    bonuses = []
    spauns = []
    entities.add(hero)
    is_w = False
    level = []
    finish = Finish(0, 0)
    loadLevel(str(CURRENT_LEVEL.GetNum()), level)
    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption("GAME!!!")

    info_string = pygame.Surface((1000, 50))
    info_string.fill((204, 204, 255))
    inf_font = pygame.font.Font(None, 24)
    big_inf_font = pygame.font.Font(None, 40)
    bgi = image.load('images/background'+str(CURRENT_LEVEL.GetNum())+'.jpg')
    bg = pygame.Surface((4000, 800))
    heroBar = HealthBar(hero.rect.x, hero.rect.y)
    bg.blit(bgi, (0, 0))
    punkts = [(370, 200, u'Play (%s level)'%CURRENT_LEVEL.GetNum(), (250, 250, 30), (250, 30, 250), 0),
            (370, 300, u'Records', (250, 250, 30), (250, 30, 250), 1   ),
            (370, 400, u'Exit', (250, 250, 30), (250, 30, 250), 2   )]
    game = menu.Menu((punkts))
    game.menu(screen)
    total_level_width = len(level[0])*PLATFORM_WIDTH
    total_level_height = len(level)*PLATFORM_HEIGHT

    camera = Camera(camera_configure, total_level_width, total_level_height)
    left = right = up = f_up = f_dwn = shoot = ch_w = False
    go = True
    parse_level(level, entities, platforms, enemies, traps, finish, bonuses, spauns)
    hero.SetAnimEvery(post)
    while go:
        for e in pygame.event.get():
            if e.type == QUIT:
                go = False
            if e.type == KEYDOWN and e.key == K_LEFT:
                left = True
            if e.type == KEYDOWN and e.key == K_RIGHT:
                right = True
            if e.type == KEYUP and e.key == K_RIGHT:
                right = False
            if e.type == KEYUP and e.key == K_LEFT:
                left = False
            if e.type == KEYDOWN and e.key == K_SPACE:
                up = True
            if e.type == KEYUP and e.key == K_SPACE:
                up = False
            if e.type == KEYUP and e.key == K_ESCAPE:
                game.menu(screen)
            if e.type == KEYDOWN and e.key == K_UP:
                f_up = True
            if e.type == KEYUP and e.key == K_UP:
                f_up = False
            if e.type == KEYDOWN and e.key == K_DOWN:
                f_dwn = True
            if e.type == KEYUP and e.key == K_DOWN:
                f_dwn = False
            if e.type == KEYDOWN and e.key == K_f:
                shoot = True
            if e.type == KEYUP and e.key == K_f:
                shoot = False
                hero.fire(bullets, f_up, f_dwn)
            if e.type == KEYUP and e.key == K_r:
                hero.change_weapon()
            if e.type == KEYUP and e.key == K_CAPSLOCK:
                ch_w = True

        dh = 0
        if (hero.rect.y)/5 > 100:
            dh = -100
        else:
            dh = -hero.rect.y/5
        screen.blit(bg, (-hero.rect.x/8, dh+50))
        camera.update(hero)
        for en in enemies:
            en.update(bullets, hero.rect.x, hero.rect.y, effects, platforms)
            if en.obj.rect.x == -1000:
                enemies.remove(en)
                del en
        for e in entities:
            screen.blit(e.image, camera.apply(e))
        screen.blit(heroBar.image, camera.apply(heroBar))
        screen.blit(hero.weapon.image, camera.apply(hero.weapon))
        hero.update(left, right, up, shoot, platforms, traps, enemies, bonuses, effects)

        for b in bullets:
            b.update(platforms, effects)
            screen.blit(b.image, camera.apply(b))
            if b.rect.x == -1000:
                bullets.remove(b)
                del b
        for b in bonuses:
            b.update()
        for s in spauns:
            s.update(enemies, entities, (s.rect.x*s.rect.y)%(time.get_ticks()))
            screen.blit(s.image, camera.apply(s))
            if s.rect.x == -1000:
                spauns.remove(s)
                del s

        for eff in effects:
            eff.update()
            screen.blit(eff.image, camera.apply(eff))
            if eff.rect.x == -1000:
                effects.remove(eff)
                del eff
        for t in traps:
            t.update()
            if t.rect.x == -1000:
                traps.remove(t)
                del t

        heroBar.update(hero.rect.x, hero.rect.y, hero.xp)
        if(shoot and hero.weapon.id == 2 and not is_w):
            water_sprite = Water(hero.rect.x, hero.rect.y, hero.rotation)
            is_w = True
        if(shoot and hero.weapon.id == 2 and is_w):
            water_sprite.update(hero.rect.x, hero.rect.y, hero.rotation)
            screen.blit(water_sprite.image, camera.apply(water_sprite))
            for t in traps:
                t.try_water(water_sprite)
            for s in spauns:
                s.try_water(water_sprite)

        if(not shoot and hero.weapon.id == 2 and is_w):
            is_w = False

        info_string.fill((204, 204, 255))
        info_string.blit(xp_image, (10, 5))
        info_string.blit(inf_font.render(str(hero.xp), 1, (255, 0, 0)), (40, 5))
        info_string.blit(inf_font.render(u'bullets: '+str(hero.weapon.bls), 1, (255, 0, 0)), (10, 30))
        info_string.blit(hero.weapon.imager, (80, 20))
        info_string.blit(inf_font.render(u'Leverl '+str(CURRENT_LEVEL.GetName()), 1, (0, 0, 0)), (300, 0))
        info_string.blit(big_inf_font.render(u'HP: '+str(POINTS.GetPoints()), 1, (255, 100, 0)), (300, 15))
        screen.blit(info_string, (0, 0))
        pygame.display.update()
        timer.tick(80)
        #print(timer.get_fps())

        if sprite.collide_rect(hero, finish) or hero.xp <= 0 or ch_w:
            if CURRENT_LEVEL.GetNum() == 4 or hero.xp <= 0:
                if CURRENT_LEVEL.GetNum() == 4:
                    screen.blit(big_inf_font.render(u'Level! ', 1, (255, 100, 0)), (300, 200))
                    pygame.display.update()
                    time.wait(2000)
                else:
                    ShowIfDie(screen, hero,POINTS.GetPoints())
                records = HighScores()
                records.AddRecord(CURRENT_LEVEL.GetName(), POINTS.GetPoints())
                CURRENT_LEVEL.SetNum(CURRENT_LEVEL.GetNum()-CURRENT_LEVEL.GetNum()+1)
            else:
                screen.blit(big_inf_font.render(u'You have %s levels! '%CURRENT_LEVEL.GetNum(), 1, (255, 100, 0)), (300, 200))
                POINTS.ChangePoints(10000)
                pygame.display.update()
                time.wait(2000)
                CURRENT_LEVEL.SetNum(CURRENT_LEVEL.GetNum()+1)
            pygame.display.update()
            go = False