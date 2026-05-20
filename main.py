import random
import pygame
import sys
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event



def main():
    print("Starting Asteroids with pygame version: ", pygame.version.ver)
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        updatable.update(dt)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(player):
                    player.respawn_count -= 1
                    if player.respawn_count == 0:
                        player.kill()
                        log_event("player_hit")
                        print("No lives remaining. Game over!")
                        sys.exit()
                    else:
                        player.relocate_for_respawn(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                        log_event("player_respawn")
                        print("Respawning player...")
                elif asteroid.collides_with(shot):
                    log_event("asteroid_hit")
                    asteroid.split()
                    shot.kill()
 
        pygame.display.flip()
        dt = clock.tick(60) / 1000






if __name__ == "__main__":
    main()
