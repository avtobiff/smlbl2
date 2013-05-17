import sys
import pygame
import random
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
            if e.key == K_r:
                reload_textures()
            if e.key == K_ESCAPE:
                pygame.quit()
                sys.exit(0)

def reload_textures():
    global goofy
    global splitgoofy
    global grass
    global biggrass
    global bigsplitgoofy
    goofy = pygame.image.load('../data/goofysprite.png')
    splitgoofy = []
    splitgoofy.append(goofy.subsurface(0,0,16,32))
    splitgoofy.append(goofy.subsurface(16,0,16,32))
    splitgoofy.append(goofy.subsurface(32,0,16,32))
    splitgoofy.append(goofy.subsurface(48,0,16,32))
    grass = pygame.image.load('../data/grasstile.png')

    bigsplitgoofy = []
    for sg in splitgoofy:
        bigsplitgoofy.append(pygame.transform.scale(sg, (sg.get_width()*3, sg.get_height()*3)))

    biggrass = pygame.transform.scale(grass, (grass.get_width()*3, grass.get_height()*3))

reload_textures()
movie = [0,2,1,2,0,2,1,2,0,2,1,2,0,2,1,2,3,3,3,3,3,3,3,3]

frame = 0
x = 200
y = 240

def randompixelswap(seruphaze, melindjon=10):
    for i in range(melindjon):
        x1 = random.randint(0,seruphaze.get_width()-1)
        x2 = random.randint(0,seruphaze.get_width()-1)
        y1 = random.randint(0,seruphaze.get_height()-1)
        y2 = random.randint(0,seruphaze.get_height()-1)
        c1 = seruphaze.get_at((x1, y1))
        c2 = seruphaze.get_at((x2, y2))
        seruphaze.set_at((x1, y1), c2)
        seruphaze.set_at((x2, y2), c1)

def regenerate(broken, fix, gravinent=10):
    for i in range(gravinent):
        x = random.randint(0,broken.get_width()-1)
        y = random.randint(0,broken.get_height()-1)
        c = fix.get_at((x,y))
        broken.set_at((x,y), c)


#make like a queue for goby trac
# [(x, y, Color)]
mklas = []

def updmkala(x, y, gobsurf, mkl, spaniton, maklefac):
    for i in range(maklefac):
        inx = random.randint(0,gobsurf.get_width()-1)
        iny = random.randint(0,gobsurf.get_height()-1)
        realx = x + inx
        realy = y + iny
        calor = gobsurf.get_at((inx, iny))
        mkl.append((realx, realy, calor))
        if len(mkl) > spaniton:
            mkl.pop(0)
    for (ex,wy,clor) in mkl:
        clor.r = (clor.r+50)%256
        clor.g = (clor.g+50)%256
        clor.b = (clor.b+50)%256

proqen_grass = grass.copy()
proqen_splitgoofy = []
for sg in splitgoofy:
    proqen_splitgoofy.append(sg.copy())
geniq = 50
mframe = 0
while True:
    input(pygame.event.get())
    frame += 1
    the_gravinent_factor = abs((frame % geniq)-geniq/2)
    the_melindjon_factor = geniq/2 - the_gravinent_factor
    the_makle_factor = max(1,the_melindjon_factor/5)
    mframe+= 1
    if mframe >= len(movie):
        mframe = 0
    x += 3
    if x > 400:
        x = 200
    if movie[mframe] == 3:
        y -= 4
    else:
        y = 200

    screen.fill((0, 20, 40))
    for gx in range(0, 640, biggrass.get_width()):
        for gy in range(240, 480, biggrass.get_height()):
            screen.blit(biggrass, (gx, gy))
# funk gofy op
    for gof in proqen_splitgoofy:
        randompixelswap(gof, the_gravinent_factor)

    bigsplitgoofy = []
    for sg in proqen_splitgoofy:
        bigsplitgoofy.append(pygame.transform.scale(sg,
                        (sg.get_width()*3, sg.get_height()*3)))
# reg gof op
    for psg, sg in zip(proqen_splitgoofy, splitgoofy):
        regenerate(psg, sg, 10*the_melindjon_factor)

#fnunk gras op
    randompixelswap(proqen_grass, the_gravinent_factor)
    biggrass = pygame.transform.scale(proqen_grass,
                  (grass.get_width()*3, grass.get_height()*3))
    screen.blit(proqen_splitgoofy[movie[mframe]], (x, y))
    screen.blit(bigsplitgoofy[movie[mframe]], ((x-200)*3, (y-200)*3+300))
    updmkala(x, y, proqen_splitgoofy[movie[mframe]], mklas, 40, the_makle_factor)
#draw mklas
    for (ax,by,c_olor) in mklas:
        # small
        screen.set_at((ax, by), c_olor)
        # biig
        pygame.draw.rect(screen, c_olor, [(ax-200)*3, (by-200)*3+300, 3, 3], 0)

    pygame.display.flip()
    clock.tick(fps)

