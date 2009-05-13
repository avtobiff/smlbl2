class GameObject:
	"""
	A representation of an object in the game, eg. a monster, player, rock
	etc.
	"""
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
