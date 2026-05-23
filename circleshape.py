import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass

    def update(self, dt):
        # must override
        pass

    def collides_with(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius
    
    def check_bounds(self, screen_width, screen_height):
        boundary_states = []
        left_boundary = (self.position.x + self.radius < 0)
        boundary_states.append(left_boundary)
        right_boundary = (self.position.x - self.radius > screen_width) 
        boundary_states.append(right_boundary)
        top_boundary = (self.position.y + self.radius < 0)
        boundary_states.append(top_boundary)
        bottom_boundary = (self.position.y - self.radius > screen_height)
        boundary_states.append(bottom_boundary)
        return boundary_states  

    def wrap(self, boundary_states, screen_width, screen_height):
        for state in boundary_states:
            if state == True:
                if state == boundary_states[0]:
                    self.position = pygame.Vector2(screen_width - self.position.x, self.position.y) 
                if state == boundary_states[1]:
                    self.position = pygame.Vector2(screen_width - self.position.x, self.position.y)
                if state == boundary_states[2]:
                    self.position = pygame.Vector2(self.position.x, -self.position.y + screen_height)
                if state == boundary_states[3]:
                    self.position = pygame.Vector2(self.position.x, -self.position.y + screen_height)

           
