import math
from decimal import Decimal

from collections import namedtuple

import pygame as pg

from colors import WHITE


CLOCK_COLOR = WHITE
Point = namedtuple('Point', ['x', 'y'])


class Clock:
    padding = Decimal(10)
    division_rect = (5, 25)
    angle = Decimal(0)

    def __init__(self, surface):
        self.surface = surface
        width = Decimal(surface.get_width())
        height = Decimal(surface.get_height())
        self.radius = (width - self.padding * 2) / 2
        print(self.radius)
        self.middle = Point(width / 2, height / 2)
        self.start_point = Point(width / 2, self.padding)

    def _draw(self, point):
        pg.draw.circle(self.surface, CLOCK_COLOR, (float(point.x), float(point.y)), 5)

    def _calc_point(self):
        x1 = self.start_point.x
        y1 = self.start_point.y
        x2 = x1 + Decimal(math.sin(self.angle)) * self.radius
        y2 = y1 + self.radius * Decimal(1 - math.cos(self.angle))
        return Point(x2, y2)

    def _inc_angle(self):
        self.angle = self.angle - Decimal(360 / 60)

    def update(self):
        point = self._calc_point()
        self._draw(point)
        self._inc_angle()
