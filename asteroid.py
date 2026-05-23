from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
from logger import log_event
import random



class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.is_seen = False
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt):
        if self.is_seen == False:
            self.is_asteroid_seen()
        self.position += self.velocity * dt

    def is_asteroid_seen(self):
        if self.position.x > 0 and self.position.x < SCREEN_WIDTH:
            if self.position.y > 0 and self.position.y < SCREEN_HEIGHT:
                self.is_seen = True
            

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            asteroid_split_angle = random.uniform(20,50)
            asteroid_one_velocity = self.velocity.rotate(asteroid_split_angle)
            asteroid_two_velocity = self.velocity.rotate(-asteroid_split_angle)
            asteroid_one = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid_two = Asteroid(self.position.x, self.position.y, self.radius-ASTEROID_MIN_RADIUS)
            asteroid_one.velocity = asteroid_one_velocity * 1.2
            asteroid_two.velocity = asteroid_two_velocity * 1.2

            
        