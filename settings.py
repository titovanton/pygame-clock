from models import MyColor, TimeZones, Point, Size, BootstrapColor


clock_diameter = 430
padding = 24  # deprecated for settings
default_surface_size = Size(clock_diameter + padding * 2,
                            clock_diameter + padding * 2)
default_clock = {
    'clock_diameter': clock_diameter,
    'surface_size': default_surface_size,
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

quarter_surface_size = Size(int(default_surface_size.width / 2),
                            int(default_surface_size.height / 2))
quarter_clock = {
    **default_clock,
    'clock_diameter': clock_diameter / 2,
    'surface_size': quarter_surface_size,
    'hour_point_radius': 4,
    'min_point_radius': 1,
    'font_size': 17,
    'hour_thickness': 6,
    'minute_thickness': 3,
    'second_color': BootstrapColor.BLUE,
}

default_settings = {
    'screen_size': Size(
        int(default_surface_size.width + quarter_surface_size.width * 2),
        int(default_surface_size.height + quarter_surface_size.height * 2)
    ),
}

SETTINGS = {
    **default_settings,
    'clocks': [

        # 1t quarter
        {
            **quarter_clock,
            'timezone': TimeZones.LONDON,
            'second_color': BootstrapColor.GREEN,
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width, 0),
            'timezone': TimeZones.COPENHAGEN,
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'coordinates': Point(0, quarter_surface_size.height),
            'timezone': TimeZones.LOS_ANGELES,
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width,
                                 quarter_surface_size.height),
            'timezone': TimeZones.NEW_YORK,
            'second_color': BootstrapColor.YELLOW,
        },

        # 2nd quarter
        {
            **default_clock,
            'coordinates': Point(quarter_surface_size.width * 2, 0),
            'timezone': TimeZones.YEKATERINBURG,
        },

        # 2nd row
        {
            **quarter_clock,
            'timezone': TimeZones.TOKYO,
            'coordinates': Point(0, quarter_surface_size.height * 2),
            'second_color': BootstrapColor.GREEN,
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width,
                                 quarter_surface_size.height * 2),
            'timezone': 'Europe/Simferopol',
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': 'GMT',
            'coordinates': Point(quarter_surface_size.width * 2,
                                 quarter_surface_size.height * 2),
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width * 3,
                                 quarter_surface_size.height * 2),
            'timezone': TimeZones.CET,
            'second_color': BootstrapColor.YELLOW,
        },

        # 3d row
        {
            **quarter_clock,
            'timezone': TimeZones.PST,
            'coordinates': Point(0, quarter_surface_size.height * 3),
            'second_color': BootstrapColor.GREEN,
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width,
                                 quarter_surface_size.height * 3),
            'timezone': TimeZones.MST,
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width * 2,
                                 quarter_surface_size.height * 3),
            'timezone': TimeZones.CST,
        },
        {
            **quarter_clock,
            'coordinates': Point(quarter_surface_size.width * 3,
                                 quarter_surface_size.height * 3),
            'timezone': TimeZones.EST,
            'second_color': BootstrapColor.YELLOW,
        },

    ],
    # 'weather': [
    #     {
    #         TimeZones.YEKATERINBURG,
    #     }
    # ]
}
