class GameObject:
    """
    A representation of an object in the game, eg. a background, monster,
    player, rock etc.
    """
    def __init__(self, coords, dimensions, sprite):
        self.coords = coords
        self.dimensions = dimensions
        self.sprite = sprite

    def set_sprite(self, sprite):
        self.sprite = sprite


class SplashImage(GameObject):
    """
    The SMLBL2 splash image.
    """
    def __init__(self):
        GameObject.__init__(self, (0, 0), (640, 480), "data/splash_image.png")


class LevelSplashImage(GameObject):
    """
    The level splash image.
    """
    def __init__(self):
        GameObject.__init__(self, (0, 0), (640, 480),
                            "data/level_splash_image.png")


# only placeholder for now. should be a collection instead of GameObject
class Level(GameObject):
    def __init__(self):
        GameObject.__init__(self, (0, 0), (640, 480), "data/level.png")
