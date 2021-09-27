import math
import enum
from collections import namedtuple
from datetime import datetime
from decimal import Decimal

import pygame
import pygame.gfxdraw

from colors import WHITE, SILVER


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


class ArrowType(enum.Enum):
    SECOND = '1'
    MINUTE = '2'
    HOUR = '3'


class ArrowBase:
    len_k = 1
    skin_angles = {
        ArrowType.SECOND: Decimal(math.pi / 2),
        ArrowType.MINUTE: Decimal(math.pi / 6),
        ArrowType.HOUR: Decimal(math.pi / 4),
    }
    color = SILVER

    def __init__(self, surface, radius, center):
        self.surface = surface
        self.radius = radius
        self.center = center
        self.start_point = Point(center.x, center.y - self.len)

    @property
    def skin_angle(self):
        return self.skin_angles[self.type]

    @property
    def len(self):
        return self.radius * self.len_k

    def update(self):
        raise NotImplementedError()

    def calc_arrowhead(self, angle):
        x0 = self.start_point.x
        y0 = self.start_point.y
        x = math.ceil(x0 + Decimal(math.sin(angle)) * self.len)
        y = math.ceil(y0 + self.len * Decimal(1 - math.cos(angle)))
        return Point(x, y)


class MinuteAngleMixin:
    def get_angle(self, minute, second=0, error_text='Must be True: 0 <= minute <= 59'):
        if minute > 59 or minute < 0:
            raise ValueError(error_text)
        if second > 59 or second < 0:
            raise ValueError('Must be True: 0 <= second <= 59')
        return minute * Decimal(math.pi / 30) + second * Decimal(math.pi / 1800)


class MinuteArrow(MinuteAngleMixin, ArrowBase):
    len_k = Decimal(9 / 10)

    def __init__(self, surface, radius, center):
        super().__init__(surface, radius, center)
        self.type = ArrowType.MINUTE

    def update(self, dtime):
        minute = dtime.minute
        second = dtime.second

        # harcoded to make arrows look better
        if minute == 15 and second == 0:
            current_pos = Point(self.center.x + self.len, self.center.y)
        elif minute == 30 and second == 0:
            current_pos = Point(self.center.x, self.center.y + self.len)
        elif minute == 45 and second == 0:
            current_pos = Point(self.center.x - self.len, self.center.y)
        else:
            angle = self.get_angle(minute, second)
            current_pos = self.calc_arrowhead(angle)

        pygame.draw.aaline(
            self.surface,
            self.color,
            self.center,
            current_pos,
        )


class SecondArrow(MinuteAngleMixin, ArrowBase):
    len_k = Decimal(8 / 10)

    def __init__(self, surface, radius, center):
        super().__init__(surface, radius, center)
        self.type = ArrowType.SECOND

    def update(self, dtime):
        second = dtime.second

        # harcoded to make arrows look better
        if second == 15:
            current_pos = Point(self.center.x + self.len, self.center.y)
        elif second == 30:
            current_pos = Point(self.center.x, self.center.y + self.len)
        elif second == 45:
            current_pos = Point(self.center.x - self.len, self.center.y)
        else:
            angle = self.get_angle(second, error_text='Must be True: 0 <= second <= 59')
            current_pos = self.calc_arrowhead(angle)

        pygame.draw.aaline(
            self.surface,
            self.color,
            self.center,
            current_pos,
        )


class HourArrow(MinuteAngleMixin, ArrowBase):
    len_k = Decimal(3 / 5)

    def __init__(self, surface, radius, center):
        super().__init__(surface, radius, center)
        self.type = ArrowType.HOUR

    def update(self, dtime):
        hour = dtime.hour
        minute = dtime.minute

        # harcoded to make arrows look better
        if hour == 3 and minute == 0:
            current_pos = Point(self.center.x + self.len, self.center.y)
        elif hour == 6 and minute == 0:
            current_pos = Point(self.center.x, self.center.y + self.len)
        elif hour == 9 and minute == 0:
            current_pos = Point(self.center.x - self.len, self.center.y)
        else:
            angle = self.get_angle(hour, minute)
            current_pos = self.calc_arrowhead(angle)

        pygame.draw.aaline(
            self.surface,
            self.color,
            self.center,
            current_pos,
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
        self.center = Point(width / 2, height / 2)
        self.start_point = Point(width / 2, self.padding)  # 12:00

        # arrows
        self.second_arrow = SecondArrow(surface, self.radius, self.center)
        self.minute_arrow = MinuteArrow(surface, self.radius, self.center)
        self.hour_arrow = HourArrow(surface, self.radius, self.center)

        # generate face_points for hours and minutes
        self.face_points = [FacePoint(
            self.start_point.x,
            self.start_point.y,
            self.hour_point_radius,
            self.color
        )]
        hour_flag = 0
        for minute in range(60):
            angle = self.minute_arrow.get_angle(minute)
            radius = self.hour_point_radius if not hour_flag else self.min_point_radius
            point = self.calc_point(self.radius, self.start_point, angle)
            self.face_points.append(FacePoint(point.x, point.y, radius, self.color))
            if hour_flag == 4:
                hour_flag = 0
            else:
                hour_flag += 1

    def draw_face(self, points):
        for point in points:
            pygame.gfxdraw.aacircle(
                self.surface,
                int(point.x),
                int(point.y),
                int(point.radius),
                self.color,
            )

    def calc_point(self, radius, start_point, angle):
        x1 = start_point.x
        y1 = start_point.y
        x2 = math.ceil(x1 + Decimal(math.sin(angle)) * radius)
        y2 = math.ceil(y1 + radius * Decimal(1 - math.cos(angle)))
        return Point(x2, y2)

    def update(self):
        self.draw_face(self.face_points)
        now = datetime.now()
        self.second_arrow.update(now)
        self.minute_arrow.update(now)
        self.hour_arrow.update(now)
