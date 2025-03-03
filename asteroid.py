import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius) -> None:
        self.radius = radius
        self.x = x
        self.y = y

    super().__init__()

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            radius=self.radius,
            width=2,
            center=(self.x, self.y),
        )

    def update(self, dt):
        self.position += super().self.velocity() * dt
