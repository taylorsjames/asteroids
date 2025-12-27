from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from circleshape import CircleShape
import pygame
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    

    def update(self, dt):
        self.position += (self.velocity * dt)

    def split(self):
        
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        new_radius = (self.radius - ASTEROID_MIN_RADIUS)
        log_event("asteroid_split")
        
        rand_angle = random.uniform(20, 50)
        
        new_vector_1 = self.velocity.rotate(rand_angle)
        new_vector_2 = self.velocity.rotate(-rand_angle)
        
        smaller_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid1.velocity = (new_vector_1 * 1.2)

        smaller_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        smaller_asteroid2.velocity = (new_vector_2 * 1.2)