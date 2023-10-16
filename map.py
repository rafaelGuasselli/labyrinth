from labyrinth_generator import LabyrinthGenerator


class Map:
	def __init__(self, size):
		self.height, self.width = size
		self.generator = LabyrinthGenerator(size)
		self.createMap()

	def createMap(self):
		self.clearMap()
		self.generator.generate(self.map)

	def clearMap(self):
		self.map = []
		for i in range(0, self.height):
			line = []
			for j in range(0, self.width):
				line.append(None)
			self.map.append(line)

	def render(self):
		string = ""
		for l in range(0, self.height):
			for c in range(0, self.width):
				string += self.map[l][c].render()
			string += "\n"

		return string