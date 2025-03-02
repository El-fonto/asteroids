import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        black_screen = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        black_screen.fill(color="black")

        pygame.display.flip()  # refresh screen


if __name__ == "__main__":
    main()
