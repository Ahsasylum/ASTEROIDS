from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and keys[pygame.K_w]:
            if self.rotation >= 0:
                self.rotation -= 90*dt % 360
            else:
                self.rotation += 90*dt % 360
            self.move(dt)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            if self.rotation >= 0:
                self.rotation += 90*dt % 360
            else:
                self.rotation -= 90*dt % 360
            self.move(dt)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            if self.rotation >= 0:
                self.rotation += 90*dt % 360
            else:
                self.rotation -= 90*dt % 360
            self.move(-dt)
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            if self.rotation >= 0:
                self.rotation -= 90*dt % 360
            else:
                self.rotation += 90*dt % 360
            self.move(-dt)
        elif keys[pygame.K_a]:
            if self.rotation >= 0:
                self.rotation -= 90*dt % 360
            else:
                self.rotation += 90*dt % 360
        elif keys[pygame.K_d]:
            if self.rotation >= 0:
                self.rotation += 90*dt % 360
            else:
                self.rotation -= 90*dt % 360
        elif keys[pygame.K_w]:
            self.move(dt)
        elif keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer <= 0:
                self.shoot()
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt



    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_unit_vector = unit_vector.rotate(self.rotation)
        rotated_unit_vector *= PLAYER_SPEED * dt
        self.position += rotated_unit_vector

    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_unit_vector = unit_vector.rotate(self.rotation)
        rotated_unit_vector *= PLAYER_SHOOT_SPEED
        shot.velocity = rotated_unit_vector