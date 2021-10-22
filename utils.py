import requests
from datetime import datetime

from models import Size


def get_clock_size(settings):
    return Size(
        settings.clock_diameter + settings.padding * 2,
        settings.clock_diameter + settings.padding * 2,
    )


def less_often_than(seconds):
    """
    Decorator, which does not allow to call a function more often than
    specified number of seconds via argument.
    """

    def decorator(func):
        def _inner(*args, **kwargs):
            if _inner.last_call:
                tdelta = datetime.now() - _inner.last_call
                if tdelta.seconds < seconds:
                    return _inner.else_return

            _inner.last_call = datetime.now()
            result = _inner.else_return = func(*args, **kwargs)
            print(_inner.last_call)
            print(result)
            return result
        _inner.last_call = None
        _inner.else_return = None

        return _inner
    return decorator


@less_often_than(60 * 30)
def get_weather(city=None):
    url = 'https://community-open-weather-map.p.rapidapi.com/weather'

    querystring = {
        'q': 'London,uk',
        'lat': '0',
        'lon': '0',
        'callback': 'test',
        'id': '2172797',
        'lang': 'null',
        'units': 'imperial',
        'mode': 'xml'
    }

    headers = {
        'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com',
        'x-rapidapi-key': '338f08b14dmsh9663290e8945698p161783jsn27b0abb41a31'
    }

    response = requests.request('GET', url, headers=headers, params=querystring)
    return response.text
