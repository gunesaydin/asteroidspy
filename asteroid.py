import random

from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.asteroid_kind = 0
        if radius == ASTEROID_MIN_RADIUS * 1:
            self.asteroid_kind = 1
        elif radius == ASTEROID_MIN_RADIUS * 2:
            self.asteroid_kind = 2
        elif radius == ASTEROID_MIN_RADIUS * 3:
            self.asteroid_kind = 3

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        if self.asteroid_kind <= 1:
            self.kill()
        elif self.asteroid_kind <= 3:
            split_angle = random.uniform(20, 50)
            direction_1 = self.velocity.rotate(split_angle)
            direction_2 = self.velocity.rotate(-split_angle)
            asteroid_1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid_1.velocity = direction_1 * 1.2
            asteroid_2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
            asteroid_2.velocity = direction_2 * 1.2
            self.kill()