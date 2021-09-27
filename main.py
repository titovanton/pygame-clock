import pygame

from clock import Clock
from colors import BLACK


BACKGOUND_COLOR = BLACK


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Clock')
    pg_clock = pygame.time.Clock()

    # Main Loop
    clock = Clock(screen)
    going = True
    while going:
        pg_clock.tick(60)  # 60 times a second
        screen.fill(BACKGOUND_COLOR)
        clock.update()
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
