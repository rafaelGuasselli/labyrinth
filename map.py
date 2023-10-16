from labyrinth_generator import LabyrinthGenerator


class Map:
	def __init__(self, size):
		self.createEmptyMap()
		self.generator = LabyrinthGenerator()
		self.generator.generate(self.map, size)

	def createEmptyMap(self):
		self.map = []
		for i in range(0, self.height):
			line = []
			for j in range(0, self.width):
				line.append(None)
			self.map.append(line)

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