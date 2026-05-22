from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS, PLAYER_RESPAWN_COUNT
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
        self.respawn_count = PLAYER_RESPAWN_COUNT
        self.frame_counter = 0 # for tracking number of frames between keypresses
        self.pressed_keys = pygame.key.get_pressed() # for tracking key pressed in previous frame
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH) 
        font = pygame.font.SysFont("Arial", 24) #respa
        text = font.render("Lives remaining: " + str(self.respawn_count), True, "white")
        screen.blit(text, (20, 20))
    
    def relocate_for_respawn(self, x, y):
        self.position = pygame.Vector2(x, y)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if (self.pressed_keys[pygame.K_w] and not keys[pygame.K_w]) or (self.pressed_keys[pygame.K_s] and not keys[pygame.K_s]):
            self.frame_counter = 0
        if keys[pygame.K_a] and keys[pygame.K_w]:
            self.frame_counter += 1
            if self.rotation >= 0:
                self.rotation -= 90*dt % 360
            else:
                self.rotation += 90*dt % 360
            if self.frame_counter < 60:
                self.move(dt)
            if self.frame_counter >= 60:
                self.accelerate(dt)
        elif keys[pygame.K_d] and keys[pygame.K_w]:
            self.frame_counter += 1
            if self.rotation >= 0:
                self.rotation += 90*dt % 360
            else:
                self.rotation -= 90*dt % 360
            if self.frame_counter < 60:
                self.move(dt)
            if self.frame_counter >= 60:
                self.accelerate(dt)
        elif keys[pygame.K_a] and keys[pygame.K_s]:
            self.frame_counter += 1
            if self.rotation >= 0:
                self.rotation += 90*dt % 360
            else:
                self.rotation -= 90*dt % 360
            if self.frame_counter < 60:
                self.move(-dt)
            if self.frame_counter >= 60:
                self.accelerate(-dt)
        elif keys[pygame.K_d] and keys[pygame.K_s]:
            self.frame_counter += 1
            if self.rotation >= 0:
                self.rotation -= 90*dt % 360
            else:
                self.rotation += 90*dt % 360
            if self.frame_counter < 60:
                self.move(-dt)
            if self.frame_counter >= 60:
                self.accelerate(-dt)
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
            self.frame_counter += 1
            if self.frame_counter < 60:
                self.move(dt)
            if self.frame_counter >= 60:
                self.accelerate(dt)
        elif keys[pygame.K_s]:
            self.frame_counter += 1
            if self.frame_counter < 60:
                self.move(-dt)
            if self.frame_counter >= 60:
                self.accelerate(-dt)
        if keys[pygame.K_SPACE]:
            if self.shot_cooldown_timer <= 0:
                self.shoot()
                self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        if self.shot_cooldown_timer > 0:
            self.shot_cooldown_timer -= dt
        self.pressed_keys = keys
        





    def move(self, dt):
        unit_vector = pygame.Vector2(0, 1)
        rotated_unit_vector = unit_vector.rotate(self.rotation)
        rotated_unit_vector *= PLAYER_SPEED * dt
        self.position += rotated_unit_vector

    def accelerate(self, dt):
        if self.frame_counter < 80:
            self.move(dt*1.5)
        elif self.frame_counter < 120:
            self.move(dt*2)
        elif self.frame_counter < 160:
            self.move(dt*2.5)
        elif self.frame_counter < 200:
            self.move(dt*3)


    def shoot(self):
        shot = Shot(self.position.x, self.position.y)
        unit_vector = pygame.Vector2(0, 1)
        rotated_unit_vector = unit_vector.rotate(self.rotation)
        rotated_unit_vector *= PLAYER_SHOOT_SPEED
        shot.velocity = rotated_unit_vector