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
}

default_settings = {
    'screen_size': Size(
        int(default_surface_size.width + quarter_surface_size.width * 6),
        int(default_surface_size.height + quarter_surface_size.height * 2)
    ),
    'title': 'World Wide Time',
}

SETTINGS = {
    **default_settings,
    'clocks': [

        # the big one
        {
            **default_clock,
            'timezone': TimeZones.YEKATERINBURG,
            'coordinates': Point(quarter_surface_size.width * 6, 0),
        },

        # 1t row
        {
            **quarter_clock,
            'timezone': TimeZones.LOS_ANGELES,
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.NEW_YORK,
            'coordinates': Point(quarter_surface_size.width, 0),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.LONDON,
            'coordinates': Point(quarter_surface_size.width * 2, 0),
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.MADRID,
            'coordinates': Point(quarter_surface_size.width * 3, 0),
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.PARIS,
            'coordinates': Point(quarter_surface_size.width * 4, 0),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.COPENHAGEN,
            'coordinates': Point(quarter_surface_size.width * 5, 0),
            'second_color': BootstrapColor.RED,
        },

        # 2nd row
        {
            **quarter_clock,
            'timezone': TimeZones.BERLIN,
            'second_color': BootstrapColor.YELLOW,
            'coordinates': Point(0, quarter_surface_size.height),
        },
        {
            **quarter_clock,
            'timezone': TimeZones.ROME,
            'coordinates': Point(quarter_surface_size.width,
                                 quarter_surface_size.height),
            'second_color': BootstrapColor.GREEN,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.WARSAW,
            'coordinates': Point(quarter_surface_size.width * 2,
                                 quarter_surface_size.height),
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.ATHENS,
            'coordinates': Point(quarter_surface_size.width * 3,
                                 quarter_surface_size.height),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.MOSCOW,
            'coordinates': Point(quarter_surface_size.width * 4,
                                 quarter_surface_size.height),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.DUBAI,
            'coordinates': Point(quarter_surface_size.width * 5,
                                 quarter_surface_size.height),
            'second_color': BootstrapColor.GREEN,
        },

        # 3d row
        {
            **quarter_clock,
            'timezone': TimeZones.MALDIVES,
            'coordinates': Point(0, quarter_surface_size.height * 2),
            'second_color': BootstrapColor.ORANGE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.BANGKOK,
            'coordinates': Point(quarter_surface_size.width,
                                 quarter_surface_size.height * 2),
            'second_color': BootstrapColor.PURPLE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.SINGAPORE,
            'second_color': BootstrapColor.RED,
            'coordinates': Point(quarter_surface_size.width * 2,
                                 quarter_surface_size.height * 2),
        },
        {
            **quarter_clock,
            'timezone': TimeZones.HONGKONG,
            'coordinates': Point(quarter_surface_size.width * 3,
                                 quarter_surface_size.height * 2),
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.TAIPEI,
            'coordinates': Point(quarter_surface_size.width * 4,
                                 quarter_surface_size.height * 2),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.TOKYO,
            'coordinates': Point(quarter_surface_size.width * 5,
                                 quarter_surface_size.height * 2),
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.VLADIVOSTOK,
            'coordinates': Point(quarter_surface_size.width * 6,
                                 quarter_surface_size.height * 2),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.CANBERRA,
            'coordinates': Point(quarter_surface_size.width * 7,
                                 quarter_surface_size.height * 2),
            'second_color': BootstrapColor.BLUE,
        },

        # 4th row
        {
            **quarter_clock,
            'timezone': TimeZones.NEW_ZEALAND,
            'coordinates': Point(0, quarter_surface_size.height * 3),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.PDT,
            'coordinates': Point(quarter_surface_size.width,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.MDT,
            'coordinates': Point(quarter_surface_size.width * 2,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.CDT,
            'coordinates': Point(quarter_surface_size.width * 3,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.EDT,
            'coordinates': Point(quarter_surface_size.width * 4,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.GMT,
            'coordinates': Point(quarter_surface_size.width * 5,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.RED,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.CET,
            'coordinates': Point(quarter_surface_size.width * 6,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.BLUE,
        },
        {
            **quarter_clock,
            'timezone': TimeZones.IST,
            'coordinates': Point(quarter_surface_size.width * 7,
                                 quarter_surface_size.height * 3),
            'second_color': BootstrapColor.ORANGE,
        },

    ],
    # 'weather': [
    #     {
    #         TimeZones.YEKATERINBURG,
    #     }
    # ]
}
