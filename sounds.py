import pygame
pygame.init()

class Sounds:
    def __init__(self):

        pass
    @staticmethod
    def main_theme():
         sound = pygame.mixer.music
         sound.load("sounds/main.mp3")
         sound.set_volume(1)
         sound.play(6)

    @staticmethod
    def trap_found():
        sound = pygame.mixer.Sound("sounds/trap.wav")
        sound.set_volume(0.2)
        sound.play()


    @staticmethod
    def shoot_sound():
        sound = pygame.mixer.Sound("sounds/shoot.wav")
        sound.set_volume(0.3)
        sound.play()

    @staticmethod
    def change_weapon_sound():
        sound = pygame.mixer.Sound("sounds/change_weapon.wav")
        sound.set_volume(0.2)
        sound.play()

    @staticmethod
    def baz_bul_start():
        sound = pygame.mixer.Sound("sounds/rocket_start.ogg")
        sound.set_volume(0.2)
        sound.play()

    @staticmethod
    def baz_expls():
        sound = pygame.mixer.Sound("sounds/explosion1.wav")
        sound.set_volume(0.4)
        sound.play()

    @staticmethod
    def GetBonus():
        sound = pygame.mixer.Sound("sounds/GetBonus.wav")
        sound.set_volume(0.3)
        sound.play()