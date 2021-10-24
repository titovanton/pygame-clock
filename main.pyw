import asyncio

import pygame

from clock import Clock
from models import Dict2Obj
from settings import SETTINGS


going = True
pg_clock = pygame.time.Clock()
tick_times = 100  # 100 times a second


async def handle_quit_event():
    global going

    while going:
        pg_clock.tick(tick_times)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False

        # unblock loop
        await asyncio.sleep(0)


async def game_loop(obj):
    global going

    while going:
        pg_clock.tick(tick_times)
        obj.update()
        pygame.display.flip()

        # unblock loop
        await asyncio.sleep(0)


async def main():
    pygame.init()
    pygame.font.init()
    settings = Dict2Obj(SETTINGS)
    screen = pygame.display.set_mode(settings.screen_size)
    pygame.display.set_caption(settings.title)

    clocks = [
        Clock(screen, Dict2Obj(cl_setngs))
        for cl_setngs in settings.clocks
    ]

    # runs them concurrently and waits till each get done
    await asyncio.gather(
        *[game_loop(clock) for clock in clocks],
        handle_quit_event()
    )

    pygame.quit()


if __name__ == '__main__':
    asyncio.run(main())
