import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import sys

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    drawable = pygame.sprite.Group()
    updateable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (drawable, updateable)
    Asteroid.containers = (drawable, updateable, asteroids)
    Shot.containers = (drawable, updateable, shots)
    AsteroidField.containers = (updateable,)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = clock.tick(60) / 1000
        screen.fill("black")
        updateable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides(player):
                print("Game over!")
                sys.exit(1)
        
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides(shot):
                    asteroid.split()
                    shot.kill()

        for d in drawable:
            d.draw(screen)
        
        pygame.display.flip()

if __name__ == "__main__":
    main()
