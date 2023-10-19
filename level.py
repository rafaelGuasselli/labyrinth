from labyrinth_generator import LabyrinthGenerator
from event_handler import EventHandler
from player import Player
import types
import pygame


class Level(EventHandler):
	def __init__(self, startSize):
		super().__init__()
		self.height, self.width = startSize
		self.player = Player(self)
		self.createLevel(startSize)
	
	def nextLevel(self):
		self.height, self.width = (self.height + 3, self.width + 3)
		self.createLevel((self.height, self.width))

	def createLevel(self, size):
		self.height, self.width = size
		self.map = self.createEmptyMap(size)
		self.player.setPosition((0,0))
		LabyrinthGenerator().generate(self.map, size)
		print(self.renderString())

	def createEmptyMap(self, size):
		height, width = size
		map = []
		for i in range(0, height):
			line = []
			for j in range(0, width):
				line.append(None)
			map.append(line)
		return map
	
	def close(self):
		self.triggerEvent("close")
	
	def checkIfPlayerReachExit(self, position):
		y, x = position
		reached = self.map[y][x].isExit
		if reached:
			self.triggerEvent("win", None)

	def canPlayerMoveTo(self, position, direction):
		y, x = position
		if y < 0 or x < 0:
			return False
		if y >= self.height or x >= self.width:
			return False
		return self.map[y][x].canPlayerMoveTo(direction)

	def handleKeyDown(self, key):
		self.player.handleKeyDown(key)

	def render(self, surface):
		ww, wh = surface.get_size()

		UI_SIZE = 0
		mh, mw = mapSize = (wh, ww)
		blockSize = max(min(mh/self.height, mw/self.width)/3, 1) * 3
		wallBorderSize = 2

		padding = (ww - (blockSize * self.width))/2
		my, mx = mapPosition = (0, padding)

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