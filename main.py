import sys

import pygame
from asteroid import Asteroid
from constants import *
from logger import log_state, log_event
from player import Player
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    AsteroidField.containers = updatable
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        milliseconds = clock.tick(60)
        dt = milliseconds / 1000.0

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
