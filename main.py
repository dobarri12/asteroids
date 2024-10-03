import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

	dt = 0
	
	clock = pygame.time.Clock()

	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()

	Asteroid.containers = (asteroids, updatable, drawable)
	AsteroidField.containers = updatable
	Player.containers = (updatable, drawable)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	BLACK = (0, 0, 0)
	asteroid_field = AsteroidField()
	
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		
		dt = clock.tick(60) / 1000
		
		for obj in updatable:
			obj.update(dt)

		
		for asteroid in asteroids:
			if asteroid.check_collision(player):
				print("Game over!")
				sys.exit()

		screen.fill(BLACK)
		
		for obj in drawable:
			obj.draw(screen)
		
		pygame.display.flip()

if __name__ == "__main__":
	main()

