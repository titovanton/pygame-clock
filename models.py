import enum
from collections import namedtuple

from pygame import Color


Point = namedtuple(
    'Point',
    ['x', 'y'],
    defaults=[0, 0]
)
Size = namedtuple(
    'Size',
    ['width', 'height'],
    defaults=[0, 0]
)


class Dict2Obj:
    def __init__(self, entries):
        self.__dict__.update(entries)


class MyColor(enum.Enum):
    BLACK = Color(35, 35, 35)
    WHITE = Color(255, 255, 255)
    SILVER = Color(245, 245, 245)


class BootstrapColor(enum.Enum):
    """Twitter Bootstrap colors"""

    BLUE = Color('#0d6efd')
    INDIGO = Color('#6610f2')
    PURPLE = Color('#6f42c1')
    PINK = Color('#d63384')
    RED = Color('#dc3545')
    ORANGE = Color('#fd7e14')
    YELLOW = Color('#ffc107')
    GREEN = Color('#198754')
    TEAL = Color('#20c997')
    CYAN = Color('#0dcaf0')
    GRAY500 = Color('#adb5bd')
    BLACK = Color('#000000')
    WHITE = Color('#ffffff')


class TimeZones(enum.Enum):
    """pytz timezones for easy use"""

    LOS_ANGELES = 'America/Los_Angeles'
    NEW_YORK = 'America/New_York'
    LONDON = 'Europe/London'
    MADRID = 'Europe/Madrid'
    PARIS = 'Europe/Paris'
    COPENHAGEN = 'Europe/Copenhagen'
    BERLIN = 'Europe/Berlin'
    ROME = 'Europe/Rome'
    WARSAW = 'Europe/Warsaw'
    ATHENS = 'Europe/Athens'
    MOSCOW = 'Europe/Moscow'
    KIEV = 'Europe/Kiev'
    DUBAI = 'Asia/Dubai'
    MALDIVES = 'Indian/Maldives'
    YEKATERINBURG = 'Asia/Yekaterinburg'
    NOVOSIBIRSK = 'Asia/Novosibirsk'
    BANGKOK = 'Asia/Bangkok'
    SINGAPORE = 'Singapore'
    HONGKONG = 'Hongkong'
    TAIPEI = 'Asia/Taipei'
    TOKYO = 'Asia/Tokyo'
    VLADIVOSTOK = 'Asia/Vladivostok'
    CANBERRA = 'Australia/Canberra'

    PDT = 'PST8PDT'  # USA Pacific Time Zone
    MDT = 'MST7MDT'  # USA Mountain Time Zone
    CDT = 'CST6CDT'  # USA Central Time Zone
    EDT = 'EST5EDT'  # USA Eastern Time Zone

    UTC = 'UTC'
    GMT = 'GMT'
    CET = 'CET'  # Central Europe Time

    IST = 'Asia/Kolkata'  # Indian Standard Time Zone

    NEW_ZEALAND = 'NZ'  # New Zealand
