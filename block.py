class Block:
	def __init__(self):
		self.walls = {
			"north": True,
			"south": True,
			"east": True,
			"weast": True,
			"invalid": True,
		}

		self.isExit = False

	def canPlayerMoveTo(self, direction):
		direction = self.directionToLabel(direction)
		return not self.walls[direction]

	def setExit(self, value):
		self.isExit = value
		self.walls["east"] = not value

	def openWall(self, direction):
		direction = self.directionToLabel(direction)
		if direction != "invalid":
			self.walls[direction] = False

	def closeWall(self, direction):
		direction = self.directionToLabel(direction)
		if direction != "invalid":
			self.walls[direction] = True

	def directionToLabel(self, direction):
		y, x = direction
		if y == x and x == 0:
			return "invalid"
		if y == x and x == 1:
			return "invalid"
		if abs(x) > 1 or abs(y) > 1:
			return "invalid"
		if y == -1:
			return "north"
		if y == 1:
			return "south"
		if x == -1:
			return "weast"
		if x == 1:
			return "east"

	def render(self):
		string = ""
		#string += "|" if self.walls["weast"] else " "
		string += "‾" if self.walls["north"] else " "
		#string += "_" if self.walls["south"] else " "
		string += "|" if self.walls["east"] else "‾"
		return string
