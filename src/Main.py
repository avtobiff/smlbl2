#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import pygame
from pygame.locals import *


class SMLBL2(object):
    def __init__(self):
        self.running = 1

    def input(self,event):
        if event.type == pygame.QUIT:
            self.running = 0
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESC:
                self.running = 0

    def init(self):
        pygame.init()
        screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Super Mario Långben Bruce Lee 2")
        pygame.mouse.set_visible(0)

        while self.running:
            self.input(pygame.event.poll())
            screen.fill((random.random()*255,random.random()*255,random.random()*255))
            pygame.display.flip()


if __name__ == "__main__":
    smlbl2 = SMLBL2()
    smlbl2.init()
