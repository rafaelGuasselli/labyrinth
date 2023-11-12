from action_handler import ActionHandler
from event_handler import EventHandler
from maze_solver import MazeSolver
import pygame

class Player(EventHandler, ActionHandler):
	def __init__(self, level):
		self.path = []
		self.level = level
		EventHandler.__init__(self)
		ActionHandler.__init__(self, {
			pygame.K_UP: self.up,
			pygame.K_DOWN: self.down,
			pygame.K_LEFT: self.left,
			pygame.K_RIGHT: self.right,
			pygame.K_w: self.up,
			pygame.K_s: self.down,
			pygame.K_a: self.left,
			pygame.K_d: self.right,
			pygame.K_r: self.solve,
		})

	def tick(self):
		if self.path and len(self.path) > 0:
			self.move(self.path.pop(0))

	def render(self, surface, blockSize, mapPosition):
		py, px = (self.y, self.x)
		my, mx = mapPosition
		playerSize = blockSize
		dy = (py * playerSize) + my
		dx = (px * playerSize) + mx

		color = (255,0,0)
		pygame.draw.rect(surface, color, pygame.Rect(dx, dy, blockSize, blockSize))
	
	def solve(self):
		size = (self.level.height, self.level.width)
		pos = (self.y, self.x)
		self.path = MazeSolver().solve(self.level.map, size, pos)

	def setPosition(self, position):
		self.y, self.x = position

	def handleKeyDown(self, key):
		if self.path and len(self.path) > 0: 
			return
		super().runAction(key, None)

	def up(self):
		self.move((-1, 0))
		
	def down(self):
		self.move((1, 0))
		
	def left(self):
		self.move((0, -1))

	def right(self):
		self.move((0, 1))

	def move(self, direction):
		my, mx = direction
		position = (self.y, self.x)
		canPlayerMoveTo = self.level.canPlayerMoveTo(position, direction)

		win = self.level.isExit((self.y, self.x)) and direction == (0, 1)
		if win:
			self.triggerEvent("win", None)
			return
		
		if canPlayerMoveTo:
			self.y += my
			self.x += mx
			self.triggerEvent("moved", position)