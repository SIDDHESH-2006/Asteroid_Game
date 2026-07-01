import pygame
import random
from logger import log_event
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)
    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if(self.radius<=ASTEROID_MIN_RADIUS):
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        self.velocity1 = self.velocity.rotate(random_angle)
        self.velocity2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius-ASTEROID_MIN_RADIUS
        offset=new_radius+self.radius
        pos1=self.position+self.velocity1.normalize()*offset
        pos2=self.position+self.velocity2.normalize()*offset
        asteroid1 = Asteroid(pos1.x, pos1.y, new_radius)
        asteroid2 = Asteroid(pos2.x, pos2.y, new_radius)
        asteroid1.velocity = self.velocity1
        asteroid2.velocity = self.velocity2
    def bounce(self, other: "Asteroid") -> None:
        # Calculate the normal vector between the two asteroids
        normal = (self.position - other.position).normalize()
        # Calculate the relative velocity along the normal
        relative_velocity = self.velocity - other.velocity
        velocity_along_normal = relative_velocity.dot(normal)
        # If the asteroids are moving away from each other, do nothing
        if velocity_along_normal > 0:
            return
        # Calculate the impulse scalar
        impulse_scalar = -2 * velocity_along_normal / 2  # Assuming equal mass
        # Apply the impulse to both asteroids
        self.velocity += impulse_scalar * normal
        other.velocity -= impulse_scalar * normal
