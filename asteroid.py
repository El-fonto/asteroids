import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, SHOT_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            radius=self.radius,
            width=2,
            center=(self.position.x, self.position.y),
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        # generate new trajectories
        random_angle = random.uniform(20, 50)
        a = self.velocity.rotate(random_angle)
        b = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        ast_1 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_1.velocity = a * (1.2)

        ast_2 = Asteroid(self.position.x, self.position.y, new_radius)
        ast_2.velocity = b * (1.2)
