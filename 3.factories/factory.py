
from enum import Enum
import math
import json


class CoordinateSystem(Enum):
    DECART = 1
    POLAR = 2


class Point:

    __slots__ = ('x', 'y')

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return json.dumps({atr: self.__getattribute__(atr) for atr in self.__slots__})

    # Внутренний класс как альтернатива
    # class PointFactory:
    #     def new_decart_point(self, x, y):
    #         p = Point(x, y)
    #         p.x = x
    #         p.y = y
    #         return p
    #
    #     def new_polar_point(self, rho, theta):
    #         return Point(rho * math.sin(theta),
    #                      rho * math.cos(theta))


class PointFactory:
    @staticmethod
    def new_decart_point(x, y):
        p = Point(x, y)
        p.x = x
        p.y = y
        return p

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * math.sin(theta),
                     rho * math.cos(theta))


if __name__ == '__main__':
    p1 = PointFactory.new_decart_point(1, 1)
    p2 = PointFactory.new_polar_point(1, 1)

    print(p1, p2)