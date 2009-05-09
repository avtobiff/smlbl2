import pygame

from Exceptions import ExitSMLBL2


class Hand(object):
    """
    This is the controller class.
    """
    def __init__(self,brain,eye):
        self.brain = brain
        self.eye = eye


    def handle_input(self,event):
        if event.type == pygame.QUIT:
            raise ExitSMLBL2
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                raise ExitSMLBL2
