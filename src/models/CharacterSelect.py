from models import GameObject


class Background(GameObject):
    """
    The character select background.
    """
    def __init__(self):
        GameObject.__init__(self, 0, 0, 640, 480, "data/character_select_background.png")


class Character(GameObject):
    """
    Selectable character.
    """
    def __init__(self, x, y, sprite, player_num):
        GameObject.__init__(self, 100, 100, 20, 100, sprite)
        self.player_num = player_num
        self.orig_sprite = sprite

    def select(self):
        """
        Select character with cursor.
        """
        # remove file suffix, assume only one dot in file name
        sprite_basename = self.sprite.split(".")[0]
        self.set_sprite(sprite_basename + "_selected.png")

    def unselect(self):
        """
        Unselect character with cursor.
        """
        self.set_sprite(self.orig_sprite)

    def chosen(self):
        """
        Return player num when selected.
        """
        return self.player_num


class Cursor(GameObject):
    """
    The cursor which selects characters.
    """
    def __init__(self, x, y, sprite, positions):
        GameObject.__init__(self, x, y, 20, 40, sprite)
        self.positions = positions
        self.selected_position = 0

    def move(self, left = True):
        if left:
            direction = -1

        self.selected_position += direction
        self.x = self.positions[self.selected_position]

    def move_left(self):
        # wrap around if we are at beginning
        if self.selected_position == 0:
            self.selected_position = len(self.positions)
        self.move(left = True) # i.e. left <-

    def move_right(self):
        # wrap around if we are at far end
        if self.selected_position == len(self.positions):
            self.selected_position = 0
        self.move(left = False) # i.e. right ->
