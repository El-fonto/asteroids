import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    while True:
        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player
        updatable.update(dt)

        # draw screen
        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # screen

        # limit FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
