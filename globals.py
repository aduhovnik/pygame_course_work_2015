WIN_WIDTH = 1000
WIN_HEIGHT = 600
PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = "#FF6262"
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
BACKGROUND_COLOR = (220, 220, 220)


class Points:
    __points = 0

    def ChangePoints(self, del_p):
        self.__points+=del_p

    def GetPoints(self):
        return self.__points

    def ZeroPoints(self):
        self.__points = 0

POINTS = Points()