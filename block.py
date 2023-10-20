import pygame

class Block:
	def __init__(self):
		self.walls = {
			"north": True,
			"south": True,
			"east": True,
			"west": True,
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
			return "west"
		if x == 1:
			return "east"

	def render(self, surface, blockSize, blockPosition, wallBorderSize):
		color = (150,150,150)
		y, x = blockPosition
		
		north = (x, y, blockSize, wallBorderSize)
		west  = (x, y, wallBorderSize, blockSize)

		south = (x, y + blockSize - wallBorderSize, blockSize, wallBorderSize)
		east  = (x + blockSize - wallBorderSize, y, wallBorderSize, blockSize)

		if self.walls["north"]:
			pygame.draw.rect(surface, color, pygame.Rect(north[0], north[1], north[2], north[3]))
			
		if self.walls["south"]:
			pygame.draw.rect(surface, color, pygame.Rect(south[0], south[1], south[2], south[3]))

		if self.walls["east"]:
			pygame.draw.rect(surface, color, pygame.Rect(east[0], east[1], east[2], east[3]))

		if self.walls["west"]:
			pygame.draw.rect(surface, color, pygame.Rect(west[0], west[1], west[2], west[3]))
		


	def renderString(self):
		string = ""
		#string += "|" if self.walls["west"] else " "
		string += "‾" if self.walls["north"] else " "
		#string += "_" if self.walls["south"] else " "
		string += "|" if self.walls["east"] else "‾"
		return string
