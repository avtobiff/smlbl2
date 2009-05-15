import sys, pygame
from pygame.locals import *

pygame.init()
window = pygame.display.set_mode((640,480))
screen = pygame.display.get_surface()
clock = pygame.time.Clock()
fps = 10
print "this is what mr. goofy looks like at 10 fps"

def input(events):
	for e in events:
		if e.type == QUIT:
			sys.exit(0)
		if e.type == KEYDOWN:
			if e.key == K_ESCAPE:
				pygame.quit()
				sys.exit(0)

goofy = pygame.image.load('../data/goofysprite.png')
splitgoofy = []
splitgoofy.append(goofy.subsurface(0,0,16,32))
splitgoofy.append(goofy.subsurface(16,0,16,32))
splitgoofy.append(goofy.subsurface(32,0,16,32))
splitgoofy.append(goofy.subsurface(48,0,16,32))

bigsplitgoofy = []
for sg in splitgoofy:
	bigsplitgoofy.append(pygame.transform.scale(sg, (sg.get_width()*3, sg.get_height()*3)))

movie = [0,2,1,2,0,2,1,2,0,2,1,2,0,2,1,2,3,3,3,3,3,3,3,3]

frame = 0
x = 200
y = 200

while True:
	input(pygame.event.get())
	frame += 1
	if frame >= len(movie):
		frame = 0
	x += 3
	if x > 400:
		x = 200
	if movie[frame] == 3:
		y -= 4
	else:
		y = 200
	screen.fill((0, 90, 0))
	screen.blit(splitgoofy[movie[frame]], (x, y))
	screen.blit(bigsplitgoofy[movie[frame]], ((x-200)*3, (y-200)*3+300))
	pygame.display.flip()
	clock.tick(fps)

