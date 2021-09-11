import math
from decimal import Decimal
from itertools import cycle

from collections import namedtuple

import pygame as pg

from colors import WHITE, BLUE, GREEN, RED


CLOCK_COLOR = WHITE
Point = namedtuple('Point', ['x', 'y'])


class Clock:
    padding = 10
    division_rect = (5, 25)
    angle = 0

    def __init__(self, surface):
        self.surface = surface
        width = Decimal(surface.get_width())
        height = Decimal(surface.get_height())
        self.radius = (width - self.padding * 2) / 2
        print(self.radius)
        self.middle = Point(width / 2, height / 2)
        self.start_point = Point(width / 2, self.padding)
        self._color_generator = cycle([WHITE, GREEN, RED, BLUE, RED, WHITE, BLUE, GREEN])

    def _get_color(self):
        return self._color_generator.__next__()

    def _draw(self, point):
        pg.draw.circle(self.surface, self._get_color(), (float(point.x), float(point.y)), 5)

    def _calc_point(self):
        x1 = self.start_point.x
        y1 = self.start_point.y
        x2 = math.ceil(x1 + Decimal(math.sin(self.angle)) * self.radius)
        y2 = math.ceil(y1 + self.radius * Decimal(1 - math.cos(self.angle)))
        return Point(x2, y2)

    def _inc_angle(self):
        self.angle = self.angle + Decimal(math.pi / 30)

    def update(self):
        point = self._calc_point()
        self._draw(point)
        self._inc_angle()
