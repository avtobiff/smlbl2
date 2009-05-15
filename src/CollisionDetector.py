class CollisionDetector:
	"""
	a class (why?) to look for collisions between GameObjects
	"""
	def __init__(self):
		pass

	"""
	obj1 and obj2 are GameObjects or extensions or whatever, at least
	they have x, y, width and height values
	"""
	def rectCollision(self, obj1, obj2):
		if obj1.x > obj2.x + obj2.width:
			return False
		if obj1.y > obj2.y + obj2.height:
			return False
		if obj2.x > obj1.x + obj1.width:
			return False
		if obj2.y > obj1.y + obj1.height:
			return False
		return True

