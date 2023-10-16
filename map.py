from labyrinth_generator import LabyrinthGenerator


class Map:
	def __init__(self, size):
		self.height, self.width = size
		self.map = self.createEmptyMap(size)
		self.generator = LabyrinthGenerator()
		self.generator.generate(self.map, size)

	def createEmptyMap(self, size):
		height, width = size
		map = []
		for i in range(0, height):
			line = []
			for j in range(0, width):
				line.append(None)
			map.append(line)
		return map

	def render(self):		
		string = ""
		for l in range(0, self.height):
			string += "|"
			for c in range(0, self.width):
				string += self.map[l][c].render()
			string += "\n"

		for i in range(0, self.width*2+1):
			string+= "‾"

		return string