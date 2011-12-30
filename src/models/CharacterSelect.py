from models import GameObject


class Background(GameObject):
    """
    The character select background.
    """
    def __init__(self):
        GameObject.__init__(self, (0, 0), (640, 480),
                            "data/character_select_background.png")


class Character(GameObject):
    """
    Selectable character.
    """
    def __init__(self, coords, sprite, player_num):
        GameObject.__init__(self, coords, (80, 200), sprite)
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

    offset = 20


    def __init__(self, coords, sprite, positions):
        x, y = coords
        # move cursor 50 pixels to the right so we get right above the
        # character
        GameObject.__init__(self, (x + self.offset, y), (40, 80), sprite)
        self.y = y
        self.positions = positions
        self.selected_position = 0

    def move(self, left = True):
        if left:
            direction = -1

        self.selected_position += direction
        x = self.positions[self.selected_position]
        self.coords = (x + self.offset, self.y)

    def move_left(self):
        print "Move cursor left..."
        # wrap around if we are at beginning
        if self.selected_position == 0:
            self.selected_position = len(self.positions)
        self.move(left = True) # i.e. left <-

    def move_right(self):
        print "Move cursor right..."
        # wrap around if we are at far end
        if self.selected_position == len(self.positions):
            self.selected_position = 0
        self.move(left = False) # i.e. right ->
