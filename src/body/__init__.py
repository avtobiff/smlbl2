# -*- coding: utf-8 -*-
import random, time
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

        self.state = self.SPLASH
        self.do_sleep = False
        self.do_repaint = True
        self.selected_character = None
        self.character_select_scene = [Background(),
                                       Character((50,  200), "data/character_0.png", 0),
                                       Character((200, 200), "data/character_1.png", 1),
                                       Character((350, 200), "data/character_2.png", 2),
                                       Character((500, 200), "data/character_3.png", 3),
                                       Cursor((50, 100), "data/cursor.png",
                                              [50, 200, 350, 500])]

        # set current secne to initial value
        self.scene[self.state]()


    # movement controls
    def pressed_right(self):
        if self.state == self.CHARACTER_SELECT:
            self.move_cursor_right()
            self.do_repaint = True

    def pressed_left(self):
        if self.state == self.CHARACTER_SELECT:
            self.move_cursor_left()
            self.do_repaint = True

    def pressed_enter(self):
        if self.state == self.CHARACTER_SELECT:
            self.select_character()
            self.do_repaint = True


    def tick(self):
        """
        Tick function for game play. This updates model with respect to
        control from user.
        """
        # just sleep for five seconds during splash
        if self.state == self.SPLASH and self.do_sleep:
            print "Splash..."
            time.sleep(5)
            self.do_sleep = False
            self.state = self.CHARACTER_SELECT
            print "Select character..."
        # wait in chracter select until a character is selected
        elif self.state == self.CHARACTER_SELECT:
            # repaint indication is handled by move functions
            if self.selected_character == None:
                self.do_repaint = False
                return
            print "Selected character %s..." % self.selected_character
            self.state = self.LEVEL_SPLASH
            # hack for allowing to blit level splash
            self.do_sleep = False
            self.do_repaint = True
        # just sleep for five seconds during level splash
        elif self.state == self.LEVEL_SPLASH and self.do_sleep:
            print "Level splash..."
            time.sleep(5)
            self.do_sleep = False
            self.state = self.GAMEPLAY
        # the actual gameplay!
        # no more state transitions
        elif self.state == self.GAMEPLAY:
            print "Gameplay..."

        self.do_sleep = True
        # update current scene according to new state
        self.scene[self.state]()



    ## game states
    # the idea is to control and repaint everything from the beginning of the
    # list first and continue backwards
    def splash(self):
        self.current_scene = [SplashImage()]


    def character_select(self):
        self.current_scene = self.character_select_scene

    def move_cursor_right(self):
        cursor = self.current_scene[-1]
        cursor.move_right()

    def move_cursor_left(self):
        cursor = self.current_scene[-1]
        cursor.move_left()

    def select_character(self):
        cursor = self.current_scene[-1]
        self.selected_character = cursor.selected_position


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
        print "Repainting..."

        # create a surface for every game object in brain's scene
        graphical_scene = []
        for game_object in self.brain.current_scene:
            # XXX placeholder for now
            surface = pygame.Surface(game_object.dimensions)
            color = pygame.Color(random.randint(0, 255), random.randint(0, 255),
                                 random.randint(0, 255))
            surface.fill(color)
            # TODO: actually load sprite
            #surface = pygame.image.load(game_object.sprite)
            graphical_scene.append((surface, game_object.coords))

        self.screen.fill(pygame.Color(0, 0, 0))

        for (surface, coords) in graphical_scene:
            self.screen.blit(surface, coords)

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
            elif event.key == pygame.K_RIGHT:
                self.brain.pressed_right()
            elif event.key == pygame.K_LEFT:
                self.brain.pressed_left()
            elif event.key == pygame.K_RETURN:
                self.brain.pressed_enter()
