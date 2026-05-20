import pygame
from circleshape import CircleShape
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, EXPLOSION_INITIAL_RADIUS, LINE_WIDTH, ASTEROID_MIN_RADIUS, EXPLOSION_LINE_WIDTH

class ExplosionParticle(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, EXPLOSION_INITIAL_RADIUS)
        self.line_width = EXPLOSION_LINE_WIDTH

    def draw(self, screen):
        pygame.draw.circle(screen, "red", self.position, self.radius, self.line_width)

    def update(self, dt):
        self.radius *= (1 + 2*dt)
        if self.radius >= ASTEROID_MIN_RADIUS * 0.8:
            self.kill()
        elif self.radius < ASTEROID_MIN_RADIUS * 0.6:
            self.line_width = 0
        elif self.radius > ASTEROID_MIN_RADIUS * 0.6:
            self.line_width = EXPLOSION_LINE_WIDTH