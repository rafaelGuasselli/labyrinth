from action_handler import ActionHandler
from event_handler import EventHandler
import pygame

class Player(EventHandler, ActionHandler):
	def __init__(self, level):
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
		})
	
	def setPosition(self, position):
		self.y, self.x = position

	def handleKeyDown(self, key):
		super().runAction(key, None)

	def up(self):
		self.move((-1, 0))
		
	def down(self):
		self.move((1, 0))
		
	def left(self):
		self.move((0, -1))

	def right(self):
		win = self.level.isExit((self.y, self.x))
		if win:
			self.triggerEvent("win", None)
			return
		self.move((0, 1))

	def move(self, direction):
		my, mx = direction
		position = (self.y, self.x)
		canPlayerMoveTo = self.level.canPlayerMoveTo(position, direction)
		if canPlayerMoveTo:
			self.y += my
			self.x += mx
			self.triggerEvent("moved", position)

	def render(self, surface, blockSize, mapPosition):
		py, px = (self.y, self.x)
		my, mx = mapPosition
		playerSize = blockSize
		dy = (py * playerSize) + my
		dx = (px * playerSize) + mx

		color = (255,0,0)
		pygame.draw.rect(surface, color, pygame.Rect(dx, dy, blockSize, blockSize))