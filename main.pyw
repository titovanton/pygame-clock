import pygame

from clock import Clock
from settings import SETTINGS
from utils import get_clock_size, get_clocks_coordinates


def main():
    pygame.init()
    pygame.font.init()
    clock_size = get_clock_size()
    screen_width = clock_size
    screen_height = clock_size * 2
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Clock')
    # pygame.Surface()
    pg_clock = pygame.time.Clock()

    clocks = []
    for tz in SETTINGS['clocks']:
        surf = pygame.Surface((clock_size, clock_size))
        clocks.append(Clock(surf, tz))

    # Main Loop
    going = True
    while going:
        pg_clock.tick(60)  # 60 times a second

        for clock, coordinates in zip(clocks, get_clocks_coordinates()):
            clock.update()
            screen.blit(clock.surface, coordinates)

        pygame.display.flip()

        # Handle Input Events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                going = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                going = False

    pygame.quit()


if __name__ == '__main__':
    main()
