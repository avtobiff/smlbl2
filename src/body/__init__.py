# -*- coding: utf-8 -*-
import random
import pygame

from models import SplashImage, LevelSplashImage, Level
from models.CharacterSelect import Background, Character, Cursor

from Exceptions import ExitSMLBL2


class Brain(object):
    """
    Model class.
    """

    # game states
    SPLASH           = 0
    CHARACTER_SELECT = 1
    LEVEL_SPLASH     = 2
    GAMEPLAY         = 3


    def __init__(self):
        self.scene = {self.SPLASH:           self.splash,
                      self.CHARACTER_SELECT: self.character_select,
                      self.LEVEL_SPLASH:     self.level_intro,
                      self.GAMEPLAY:         self.gameplay}

        self.next_state = self.SPLASH

        self.selected_character = None



    def tick(self):
        """
        Tick function for game play. This updates model with respect to
        control from user.
        """
        self.scene[self.next_state]()

        # just sleep for five seconds during splash
        if self.next_state == self.SPLASH:
            time.sleep(5)
            self.next_state = self.CHARACTER_SELECT
        # wait in chracter select until a character is selected
        elif self.next_state == self.CHARACTER_SELECT:
            if not self.selected_character:
                continue
            self.next_state = self.CHARACTER_SELECT
        # just sleep for five seconds during level splash
        elif self.next_state == self.LEVEL_SPLASH:
            time.sleep(5)
            self.next_state = self.GAMEPLAY
        # the actual gameplay!
        elif self.next_state == self.GAMEPLAY:
            pass # no more state transitions


    ## game states
    # the idea is to control and repaint everything from the beginning of the
    # list first and continue backwards
    def splash(self):
        self.current_scene = [SplashImage()]


    def character_select(self):
        self.current_scene = [Background(),
                              Character((100, 300), "data/character_0.png", 0),
                              Character((200, 300), "data/character_1.png", 1),
                              Character((300, 300), "data/character_2.png", 2),
                              Character((400, 300), "data/character_3.png", 3),
                              Cursor((100, 300), "data/cursor.png",
                                     [100, 200, 300, 400])]


    def level_intro(self):
        self.current_scene = [LevelSplashImage()]


    def gameplay(self):
        self.current_scene = [Level()]



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
            # TODO: handle cursor keys, send them to brain
