from settings import SETTINGS


def get_clock_size():
    return SETTINGS['clock_radius'] + SETTINGS['padding'] * 2


def get_clocks_coordinates():
    # TODO: now it's hardcoded, make it dynamic
    return [
        (0, 0),
        (0, get_clock_size())
    ]
