import sys

import pygame

from asteroid import *
from asteroidfield import *
from constants import *
from player import *
from shot import *

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        
        for member in updatable:
            member.update(dt)
        for member in drawable:
            member.draw(screen)
        for member in asteroids:
            if member.check_collision(player):
                print("Game over!")
                sys.exit(0)
        for member in shots:
            for asteroid in asteroids:
                if member.check_collision(asteroid):
                    member.kill()
                    asteroid.split()
        
        pygame.display.flip()
        dt = clock.tick(60) / 1000


    # print("Starting Asteroids!")
    # print(f"Screen width: {SCREEN_WIDTH}")
    # print(f"Screen height: {SCREEN_HEIGHT}")
    return

if __name__ == "__main__":
    main()