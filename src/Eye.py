# -*- coding: utf-8 -*-

import random
import pygame


class Eye(object):
    """
    Viewer class.
    """
    def __init__(self, brain):
        self.brain = brain
        self.screen = pygame.display.set_mode((640,480))
        pygame.display.set_caption("Super Mario Långben Bruce Lee 2")
        pygame.mouse.set_visible(0)


    def repaint(self):
        self.screen.fill((random.random()*255,random.random()*255,random.random()*255))
        pygame.display.flip()
