from models import SplashImage, LevelSplashImage, Level
from models.CharacterSelect import Background, Character, Cursor


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



    def tick(self):
        """
        Tick function for game play. This updates model with respect to
        control from user.
        """
        self.scene[self.next_state]()

    ## game states
    # the idea is to control and repaint everything from the beginning of the
    # list first and continue backwards
    def splash(self):
        self.next_state = self.CHARACTER_SELECT
        self.current_scene = [SplashImage()]


    def character_select(self):
        self.next_state = self.LEVEL_SPLASH
        self.current_scene = [Background(),
                              Character(100, 300, "data/character_0.png", 0),
                              Character(200, 300, "data/character_1.png", 1),
                              Character(300, 300, "data/character_2.png", 2),
                              Character(400, 300, "data/character_3.png", 3),
                              Cursor(100, 300, "data/cursor.png",
                                     [100, 200, 300, 400])]


    def level_intro(self):
        self.next_state = self.GAMEPLAY
        self.current_scene = [LevelSplashImage()]


    def gameplay(self):
        self.current_scene = [Level()]
