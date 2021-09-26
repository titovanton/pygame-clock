import pygame as pg

from clock import Clock
from colors import BLACK


BACKGOUND_COLOR = BLACK


def main():
    pg.init()
    screen = pg.display.set_mode((600, 600))
    pg.display.set_caption('Clock')
    pg_clock = pg.time.Clock()

    # Main Loop
    clock = Clock(screen)
    going = True
    while going:
        pg_clock.tick(60)  # 60 times a second
        screen.fill(BACKGOUND_COLOR)
        clock.update()
        pg.display.flip()

        # Handle Input Events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                going = False
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                going = False

    pg.quit()


if __name__ == '__main__':
    main()
