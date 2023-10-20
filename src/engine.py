from event_handler import EventHandler
import pygame


class Engine(EventHandler):
	def __init_(self):
		super().__init__()
		
		self.fps = 30
		self.level = None
		self.events = {}
		self.runnning = False
		self.on("exit", engine.stop)
	
	def start(self):
		pygame.init()
		
		self.running = True
		self.surface = pygame.display.set_mode((500,500), pygame.RESIZABLE)
		self.clock = pygame.time.Clock()
		while self.running:
			self.triggerEvents(pygame.event.get())
			if not self.running: 
				return

			self.surface.fill("black")
			self.triggerEvent("render", self.surface)
			pygame.display.flip()
			self.clock.tick(self.fps)
			
	def stop(self):
		self.running = False
		pygame.quit()

	def setFps(self, value):
		self.fps = value

	def triggerEvents(self, events):
		for event in events:
			if event.type == pygame.QUIT:
				self.triggerEvent("exit", None)
			
			if event.type == pygame.KEYDOWN:
				self.triggerEvent("keydown", event.key)

	def setLevel(self, level):
		self.level = level