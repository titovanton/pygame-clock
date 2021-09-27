import math
from collections import namedtuple
from datetime import datetime
from decimal import Decimal

import pygame as pg

from colors import WHITE, BLUE, SILVER


CLOCK_COLOR = WHITE
Point = namedtuple(
    'Point',
    ['x', 'y'],
    defaults=[0, 0]
)


FacePoint = namedtuple(
    'FacePoint',
    ['x', 'y', 'radius', 'color'],
    defaults=[0, 0, 0, WHITE]
)


class Clock:
    padding = 20
    division_rect = (5, 25)
    face_points = []
    hour_point_radius = 8
    min_point_radius = 4
    color = SILVER

    def __init__(self, surface):
        self.surface = surface
        width = Decimal(surface.get_width())
        height = Decimal(surface.get_height())
        self.radius = (width - self.padding * 2) / 2
        self.middle = Point(width / 2, height / 2)
        self.start_point = Point(width / 2, self.padding)  # 12:00

        # generate face_points for hours and minutes
        self.face_points = [FacePoint(
            self.start_point.x,
            self.start_point.y,
            self.hour_point_radius,
            self.color
        )]
        hour_flag = 0
        for minute in range(60):
            angle = self._get_min_angle(minute)
            radius = self.hour_point_radius if not hour_flag else self.min_point_radius
            point = self._calc_point(self.radius, self.start_point, angle)
            self.face_points.append(FacePoint(point.x, point.y, radius, self.color))
            if hour_flag == 4:
                hour_flag = 0
            else:
                hour_flag += 1

    def _get_min_angle(self, minute, second=0):
        if minute > 59 or minute < 0:
            raise ValueError('Must be True: 0 <= minute <= 59')
        if second > 59 or second < 0:
            raise ValueError('Must be True: 0 <= second <= 59')
        return minute * Decimal(math.pi / 30) + second * Decimal(math.pi / 1800)

    def _get_hour_angle(self, hour, minute=0):
        if hour > 11 or hour < 0:
            raise ValueError('Must be True: 0 <= hour <= 11')
        if minute > 59 or minute < 0:
            raise ValueError('Must be True: 0 <= minute <= 59')
        return hour * Decimal(math.pi / 6) + minute * Decimal(math.pi / 360)

    def _draw_face(self, points):
        for point in points:
            pg.draw.circle(
                self.surface,
                point.color,
                (float(point.x), float(point.y)),
                point.radius
            )

    def _calc_point(self, radius, start_point, angle):
        x1 = start_point.x
        y1 = start_point.y
        x2 = math.ceil(x1 + Decimal(math.sin(angle)) * radius)
        y2 = math.ceil(y1 + radius * Decimal(1 - math.cos(angle)))
        return Point(x2, y2)

    def _draw_min_arrow(self, now):
        min_arrow = self.radius * 9 / 10
        min_start_point = Point(
            Decimal(self.surface.get_width()) / 2,
            self.padding + self.radius / 10
        )
        minute = now.minute

        # harcoded to make arrows look better
        if minute == 15:
            end_pos = Point(self.middle.x + min_arrow, self.middle.y)
        elif minute == 30:
            end_pos = Point(self.middle.x, self.middle.y + min_arrow)
        elif minute == 45:
            end_pos = Point(self.middle.x - min_arrow, self.middle.y)
        else:
            angle = self._get_min_angle(minute, now.second)
            end_pos = self._calc_point(min_arrow, min_start_point, angle)

        pg.draw.line(
            self.surface,
            self.color,
            self.middle,
            end_pos,
            4
        )

    def _draw_hour_arrow(self, now):
        hour_arrow = self.radius * 3 / 5
        hour_start_point = Point(
            Decimal(self.surface.get_width()) / 2,
            self.padding + 2 * self.radius / 5
        )
        hour = now.hour

        # harcoded to make arrows look better
        if hour == 3:
            end_pos = Point(self.middle.x + hour_arrow, self.middle.y)
        elif hour == 6:
            end_pos = Point(self.middle.x, self.middle.y + hour_arrow)
        elif hour == 9:
            end_pos = Point(self.middle.x - hour_arrow, self.middle.y)
        else:
            angle = self._get_hour_angle(hour, now.minute)
            end_pos = self._calc_point(hour_arrow, hour_start_point, angle)

        pg.draw.line(
            self.surface,
            self.color,
            self.middle,
            end_pos,
            16
        )

    def _draw_sec_arrow(self, now):
        sec_arrow = self.radius * 8 / 10
        sec_start_point = Point(
            Decimal(self.surface.get_width()) / 2,
            self.padding + 2 * self.radius / 10
        )
        second = now.second

        # harcoded to make arrows look better
        if second == 15:
            end_pos = Point(self.middle.x + sec_arrow, self.middle.y)
        elif second == 30:
            end_pos = Point(self.middle.x, self.middle.y + sec_arrow)
        elif second == 45:
            end_pos = Point(self.middle.x - sec_arrow, self.middle.y)
        else:
            angle = self._get_min_angle(second)
            end_pos = self._calc_point(sec_arrow, sec_start_point, angle)

        pg.draw.line(
            self.surface,
            self.color,
            self.middle,
            end_pos,
            1
        )

    def update(self):
        self._draw_face(self.face_points)
        now = datetime.now()
        self._draw_sec_arrow(now)
        self._draw_min_arrow(now)
        self._draw_hour_arrow(now)
