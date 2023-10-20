from maze_generator import MazeGenerator
from action_handler import ActionHandler
from event_handler import EventHandler
from player import Player
import pygame


class Level(EventHandler, ActionHandler):
	def __init__(self, startSize):
		EventHandler.__init__(self)
		ActionHandler.__init__(self, {
			pygame.K_COMMA: self.previousLevel,
			pygame.K_PERIOD: self.nextLevel,
		})

		self.startSize = startSize
		self.height, self.width = startSize

		self.player = Player(self)
		self.player.on("win", self.nextLevel)

		self.createLevel(startSize)

	def nextLevel(self):
		self.height, self.width = (self.height + 3, self.width + 3)
		self.createLevel((self.height, self.width))
	
	def previousLevel(self):
		startH, startW = self.startSize
		self.height, self.width = (max(self.height - 3, startH), max(self.width - 3, startW))
		self.createLevel((self.height, self.width))

	def createLevel(self, size):
		self.height, self.width = size
		self.map = self.createEmptyMap(size)
		self.player.setPosition((0,0))
		MazeGenerator().generate(self.map, size)
		print(self.renderString())
		print(size)

	def createEmptyMap(self, size):
		height, width = size
		map = []
		for i in range(0, height):
			line = []
			for j in range(0, width):
				line.append(None)
			map.append(line)
		return map
	
	def isExit(self, position):
		y, x = position
		return self.map[y][x].isExit

	def canPlayerMoveTo(self, position, direction):
		y, x = position
		return self.map[y][x].canPlayerMoveTo(direction)

	def handleKeyDown(self, key):
		super().runAction(key, None)
		self.player.handleKeyDown(key)

	def render(self, surface):
		ww, wh = surface.get_size()
		mh, mw = mapSize = (wh, ww)
		blockSize = min(mh/self.height, mw/self.width)
		wallBorderSize = 1

		paddingH = (ww - (blockSize * self.width))/2
		paddingV = (wh - (blockSize * self.height))/2
		my, mx = mapPosition = (paddingV, paddingH)

		self.player.render(surface, blockSize, mapPosition)
		for l in range(0, self.height):
			for c in range(0, self.width):
				blockPosition = ((blockSize * l) + my, (blockSize * c) + mx)
				self.map[l][c].render(surface, blockSize, blockPosition, wallBorderSize)

	def renderString(self):
		string = ""
		for l in range(0, self.height):
			string += "|"
			for c in range(0, self.width):
				string += self.map[l][c].renderString()
			string += "\n"

		for i in range(0, self.width*2+1):
			string+= "‾"

		return string