from models import MyColor, TimeZones, Point, Size, BootstrapColor


clock_diameter = 430
padding = 24
default_clock = {
    'clock_diameter': clock_diameter,
    'padding': padding,
    'hour_point_radius': 8,
    'min_point_radius': 4,
    'font_family': 'Tahoma',
    'font_size': 25,
    'font_color': BootstrapColor.GRAY500,
    'timezone': TimeZones.UTC,
    'coordinates': Point(0, 0),
    'backgound_color': MyColor.BLACK,
    'color': BootstrapColor.WHITE,
    'hour_thickness': 10,
    'minute_thickness': 4,
    'second_color': BootstrapColor.WHITE,
}

quarter_clock = {
    **default_clock,
    'clock_diameter': clock_diameter / 2,
    'padding': padding / 2,
    'hour_point_radius': 4,
    'min_point_radius': 1,
    'font_size': 17,
    'hour_thickness': 6,
    'minute_thickness': 3,
    'second_color': BootstrapColor.BLUE,
}

default_settings = {
    'screen_size': Size(clock_diameter * 2 + padding * 4,
                        clock_diameter + padding * 2),
}

SETTINGS = {
    **default_settings,
    'clocks': [
        {
            **quarter_clock,
            'second_color': BootstrapColor.GREEN,
        },
        {
            **quarter_clock,
            'coordinates': Point(clock_diameter / 2 + padding, 0),
            'timezone': TimeZones.COPENHAGEN,
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'coordinates': Point(0, clock_diameter / 2 + padding),
            'timezone': TimeZones.LOS_ANGELES,
        },
        {
            **quarter_clock,
            'coordinates': Point(clock_diameter / 2 + padding,
                                 clock_diameter / 2 + padding),
            'timezone': TimeZones.NEW_YORK,
            'second_color': BootstrapColor.YELLOW,
        },
        {
            **default_clock,
            'coordinates': Point(clock_diameter + 2 * padding, 0),
            'timezone': TimeZones.YEKATERINBURG,
        },

    ],
    # 'weather': [
    #     {
    #         TimeZones.YEKATERINBURG,
    #     }
    # ]
}
