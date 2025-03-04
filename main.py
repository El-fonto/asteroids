import pygame
import sys
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)
    field = AsteroidField()

    while True:
        # quit game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # updates
        updatable.update(dt)

        # draw screen
        screen.fill(color="black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()  # screen

        # limit FPS
        dt = clock.tick(60) / 1000

        for asteroid in asteroids:
            if player.collision(asteroid):
                sys.exit("Game over!")

            for shot in shots:
                if shot.collision(asteroid):
                    shot.kill()
                    asteroid.split()


if __name__ == "__main__":
    main()
