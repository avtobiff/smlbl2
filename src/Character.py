class Character(object):
    def __init__(self,sprite,coord):
        self.sprite = sprite
        self.coord = coord

    def move(self,coord):
        pass

    def repaint(self):
        pass


class NPC(Character):
    pass


class Player(Character):
    pass
