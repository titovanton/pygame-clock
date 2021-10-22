from models import MyColor, TimeZones, Point, Size


clock_diameter = 450
padding = 14
default_clock = {
    'clock_diameter': clock_diameter,
    'padding': padding,
    'hour_point_radius': 9,
    'min_point_radius': 4,
    'font_family': 'Tahoma',
    'font_size': 17,
    'timezone': TimeZones.UTC,
    'coordinates': Point(0, 0),
    'backgound_color': MyColor.BLACK,
    'color': MyColor.SILVER,
    'hour_thickness': 10,
    'minute_thickness': 4,
}

quarter_clock = {
    **default_clock,
    'clock_diameter': clock_diameter / 2,
    'padding': padding / 2,
    'hour_point_radius': 4,
    'min_point_radius': 1,
    'font_size': 10,
    'hour_thickness': 6,
    'minute_thickness': 3,
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
        },
        {
            **quarter_clock,
            'coordinates': Point(clock_diameter / 2 + padding, 0),
            'timezone': TimeZones.COPENHAGEN,
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
