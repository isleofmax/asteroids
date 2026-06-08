import pygame
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)

    def draw(self, screen: pygame.Surface) -> None:
        pass

    def update(self, dt: float) -> None:
        pass
