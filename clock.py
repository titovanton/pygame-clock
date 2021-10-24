import math
from collections import namedtuple
from datetime import datetime
from decimal import Decimal

import numpy as np
import pygame
import pygame.gfxdraw
from pytz import timezone

from models import MyColor, Point, TimeZones


FacePoint = namedtuple(
    'FacePoint',
    ['x', 'y', 'radius', 'color'],
    defaults=[0, 0, 0, MyColor.WHITE]
)


class ArrowBase:
    """
    Rotation we gonna implement via coordinate system transformation, to use one formula x = f(x0,y0) for any x.
    We declare 3 coordinate systems: XOY, X1O1Y1, X2O2Y2 == S, S1, S2
    S - is the regular graphic system, where O at the left top corner, X goes to the right, Y goes to the bottom.
    S1 - rotated and shifted system, so O in the center of the clock, Y goes the same direction(always) as the given
    arrow, X goes to the 3:00 on the clock.
    S2 - everything the same as in S1, but X and Y are rotated on angle alpha with the arrow on relation to S1(and S).
    So, when alpha == 0 -> S2 == S1.
    This way we alwyas have same coordinates for arrows in S2, so we need transofm coordinates from S2 -> S1 -> S
    """

    # arrow_len = radius * len_k
    len_k = 1

    def __init__(self, surface, radius, center, color, thickness=1):
        self.color = color
        self.surface = surface
        self.radius = radius
        self.thickness = thickness
        self.center = center  # in S
        self.start_point = Point(0, self.len)  # in S2

    def get_matrix_s2_to_s1(self, angle):
        return np.float32([
            [np.cos(-angle), -np.sin(-angle), 0],
            [np.sin(-angle), np.cos(-angle), 0]
        ])

    def get_matrix_s1_to_s(self):
        return np.float32([
            [1, 0, self.center.x],
            [0, -1, self.center.y]
        ])

    def transform_point(self, point, angle):
        point_vector = np.float32([point.x, point.y, 1])
        point_vector = self.get_matrix_s2_to_s1(angle).dot(point_vector)
        point_vector = np.append(point_vector, np.float32([1]))
        point_vector = self.get_matrix_s1_to_s().dot(point_vector)
        return Point(math.ceil(point_vector[0]), math.ceil(point_vector[1]))

    @property
    def len(self):
        return self.radius * self.len_k

    def update(self):
        raise NotImplementedError()

    def _update(self, angle):
        current_pos = self.transform_point(self.start_point, angle)
        pygame.draw.aaline(
            self.surface,
            self.color,
            self.center,
            current_pos,
        )


class MinuteAngleMixin:
    def get_angle(self, minute, second=0, error_text='Must be True: 0 <= minute <= 59'):
        if minute > 59 or minute < 0:
            raise ValueError(error_text)
        if second > 59 or second < 0:
            raise ValueError('Must be True: 0 <= second <= 59')
        return minute * np.radians(360 / 60) + second * np.radians(360 / (60 * 60))


class MinuteArrow(MinuteAngleMixin, ArrowBase):
    len_k = Decimal(93 / 100)

    def update(self, dtime):
        minute = dtime.minute
        second = dtime.second
        angle = self.get_angle(minute, second)
        self._update(angle)


class SecondArrow(MinuteAngleMixin, ArrowBase):
    len_k = Decimal(9 / 10)

    def update(self, dtime):
        second = dtime.second
        angle = self.get_angle(second, error_text='Must be True: 0 <= second <= 59')
        self._update(angle)


class HourArrow(ArrowBase):
    len_k = Decimal(3 / 5)

    def update(self, dtime):
        hour = dtime.hour
        minute = dtime.minute
        angle = self.get_angle(hour, minute)
        self._update(angle)

    def get_angle(self, hour, minute=0):
        if minute > 59 or minute < 0:
            raise ValueError('Must be True: 0 <= minute <= 59')
        if hour > 23 or hour < 0:
            raise ValueError('Must be True: 0 <= second <= 23')
        if hour > 11:
            hour = hour - 12
        return hour * np.radians(360 / 12) + minute * np.radians(360 / (60 * 12))


class PolygonArrowMixin:
    thickness = 3

    def __init__(self, surface, radius, center, color, thickness):
        super().__init__(surface, radius, center, color, thickness)

        # all coordinates are in S2
        self.start_left_top = Point(int(-self.thickness / 2), self.len)
        self.start_right_top = Point(int(self.thickness / 2), self.len)
        self.start_right_bottom = Point(int(self.thickness / 2), 0)
        self.start_left_bottom = Point(int(-self.thickness / 2), 0)

    def _update(self, angle):
        cur_left_top = self.transform_point(self.start_left_top, angle)
        cur_right_top = self.transform_point(self.start_right_top, angle)
        cur_right_bottom = self.transform_point(self.start_right_bottom, angle)
        cur_left_bottom = self.transform_point(self.start_left_bottom, angle)

        pygame.gfxdraw.filled_polygon(
            self.surface,
            [cur_left_top, cur_right_top, cur_right_bottom, cur_left_bottom],
            self.color,
        )

        pygame.gfxdraw.aapolygon(
            self.surface,
            [cur_left_top, cur_right_top, cur_right_bottom, cur_left_bottom],
            self.color,
        )


class PolygonHourArrow(PolygonArrowMixin, HourArrow):
    thickness = 10


class PolygonMinuteArrow(PolygonArrowMixin, MinuteArrow):
    thickness = 4


class Clock:
    surface = None
    screen = None
    radius = None
    face_points = []
    hour_point_radius = None
    min_point_radius = None

    def __init__(self, screen, settings):
        self.screen = screen
        self.radius = Decimal(settings.clock_diameter / 2)
        self.surface_size = settings.surface_size
        self.hour_point_radius = Decimal(settings.hour_point_radius)
        self.min_point_radius = Decimal(settings.min_point_radius)
        self.font_family = settings.font_family
        self.font_size = settings.font_size
        self.timezone = settings.timezone
        self.coordinates = settings.coordinates
        self.backgound_color = settings.backgound_color.value
        self.color = settings.color.value
        self.font_color = settings.font_color.value

        surface = pygame.Surface(self.surface_size)
        self.surface = surface
        width = Decimal(surface.get_width())
        height = Decimal(surface.get_height())
        self.center = Point(width / 2, height / 2)
        self.start_point = Point(self.center.x,
                                 self.center.y - self.radius)  # 12:00

        # arrows
        self.second_arrow = SecondArrow(
            surface, self.radius, self.center, settings.second_color.value
        )
        self.minute_arrow = PolygonMinuteArrow(
            surface, self.radius, self.center, self.color,
            settings.minute_thickness
        )
        self.hour_arrow = PolygonHourArrow(
            surface, self.radius, self.center, self.color,
            settings.hour_thickness
        )

        # generate face_points for hours and minutes
        self.face_points = [FacePoint(
            *self.start_point,
            self.hour_point_radius,
            self.color
        )]
        hour_flag = 0
        for minute in range(60):
            angle = self.minute_arrow.get_angle(minute)
            radius = self.hour_point_radius if not hour_flag else self.min_point_radius
            point = self.calc_point(self.radius, self.start_point, angle)
            self.face_points.append(FacePoint(*point, radius, self.color))
            if hour_flag == 4:
                hour_flag = 0
            else:
                hour_flag += 1

    def draw_face(self, now):
        for point in self.face_points:
            pygame.gfxdraw.filled_circle(
                self.surface,
                int(point.x),
                int(point.y),
                int(point.radius),
                self.color
            )
            pygame.gfxdraw.aacircle(
                self.surface,
                int(point.x),
                int(point.y),
                int(point.radius),
                self.color
            )

        # text timezone
        city = self.timezone.name
        if len(city) > 3:
            city = city.replace('_', ' ').lower().title()
        myfont = pygame.font.SysFont(self.font_family, self.font_size)
        textsurface = myfont.render(city, True, self.font_color)
        width = Decimal(textsurface.get_width())
        position = Point(
            int(self.center.x - width / 2),
            int(self.center.y - self.radius * 2 / 3)
        )
        self.surface.blit(textsurface, position)

        # AM or PM
        textsurface = myfont.render(
            'PM' if now.hour > 11 else 'AM',
            True,
            self.font_color
        )
        width = Decimal(textsurface.get_width())
        position = Point(
            int(self.center.x - width / 2),
            int(self.center.y + self.radius / 3)
        )
        self.surface.blit(textsurface, position)
        pm_height = Decimal(textsurface.get_height())

        # date.month
        myfont = pygame.font.SysFont(self.font_family, int(self.font_size * 3 / 4))
        textsurface = myfont.render(
            f'{now:%d.%m %a}',
            True,
            self.font_color
        )
        width = Decimal(textsurface.get_width())
        position = Point(
            int(self.center.x - width / 2),
            int(self.center.y + self.radius / 3 + pm_height)
        )
        self.surface.blit(textsurface, position)

    def calc_point(self, radius, start_point, angle):
        x1 = start_point.x
        y1 = start_point.y
        x2 = math.ceil(x1 + Decimal(math.sin(angle)) * radius)
        y2 = math.ceil(y1 + radius * Decimal(1 - math.cos(angle)))
        return Point(x2, y2)

    def update(self):
        self.surface.fill(self.backgound_color)
        now = datetime.now(self.get_pytz(self.timezone))
        self.draw_face(now)
        self.second_arrow.update(now)
        self.minute_arrow.update(now)
        self.hour_arrow.update(now)
        self.screen.blit(self.surface, self.coordinates)

    def get_pytz(self, tz):
        if isinstance(tz, TimeZones):
            return timezone(tz.value)
        return timezone(tz)
