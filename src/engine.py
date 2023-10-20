from action_handler import ActionHandler
from event_handler import EventHandler
import pygame

class Engine(EventHandler, ActionHandler):
	def __init__(self):
		EventHandler.__init__(self)
		ActionHandler.__init__(self, {
			pygame.QUIT: lambda event:self.stop(),
			pygame.KEYDOWN: self.handleKeydown
		})

		self.fps = 30
		self.level = None
		self.runnning = False
	
	def start(self):
		pygame.init()
		
		self.running = True
		self.surface = pygame.display.set_mode((500,500), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()

		while self.running:
			self.handlePygameEvents(pygame.event.get())
			if not self.running: 
				return

			self.render()
			self.clock.tick(self.fps)

	def render(self):
		self.surface.fill("black")
		self.triggerEvent("render", self.surface)
		pygame.display.flip()

	def stop(self):
		self.running = False
		pygame.quit()

	def handlePygameEvents(self, events):
		for event in events:
			super().runAction(event.type, event)

	def handleKeydown(self, event):
		self.triggerEvent("keydown", event.key)

	def setFps(self, value):
		self.fps = value