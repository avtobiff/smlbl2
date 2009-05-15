import sys, pygame
from pygame.locals import *
sys.path.append('..')
import CollisionDetector
import GameObject

print 'pygame.init():', pygame.init()
window = pygame.display.set_mode((640,480))
screen = pygame.display.get_surface()

def input(events):
	for e in events:
		if e.type == QUIT:
			sys.exit(0)
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				pygame.quit()
				sys.exit(0)
			if e.key == K_LEFT:
				player.x -= 5
			if e.key == K_RIGHT:
				player.x += 5
			if e.key == K_UP:
				player.y -= 5
			if e.key == K_DOWN:
				player.y += 5

sprite = pygame.image.load('sprite.png')
font = pygame.font.Font(None, 24)
text = font.render('Collision', True, (255, 255, 255))
textpos = (5, 5)
font = pygame.font.Font(None, 14)
instructions = font.render('Move the square with arrow keys', True,\
		(255, 255, 255))
instrpos = (5, 34)

player = GameObject.GameObject(100, 200, 30, 30)
npc = GameObject.GameObject(200, 200, 30, 30)
cd = CollisionDetector.CollisionDetector()

while True:
	input(pygame.event.get())
	screen.fill((0, 0, 0))
	screen.blit(instructions, instrpos)
	screen.blit(sprite, (player.x, player.y))
	screen.blit(sprite, (npc.x, npc.y))
	if cd.rectCollision(player, npc):
		screen.blit(text, textpos)
	pygame.display.flip()

