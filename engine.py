import pygame
import types

class Engine:
	def __init_(self):
		pygame.init()
		
		self.fps = 30
		self.level = None
		self.events = {}
		self.surface = pygame.display.set_mode((0, 0))
		self.runnning = False
		
		self.on("keydown", lambda keys: self.triggerEvent("exit") if keys[pygame.K_ESCAPE] else "")
		self.on("exit", types.MethodType(self.stop, self))
	
	def start(self):
		self.running = True
		while self.running:
			self.triggerEvents(pygame.event.get())
			if not self.running: 
				return

			self.surface.fill("black")
			self.triggerEvent("render", self.surface)
			pygame.display.flip()
			clock.tick(self.fps)
			
	def stop(self):
		self.running = False
		pygame.quit()

	def on(self, event, callback):
		if not isinstance(self.events[event], list):
			self.events[event] = []
		self.events[event].append(callback)

	def triggerEvents(self, events):
		for events in events:
			if event.type == pygame.QUIT:
				self.triggerEvent("exit")
			
			if event.type == pygame.KEYDOWN:
				self.triggerEvent("keydown", pygame.key.get_pressed())
			
	def triggerEvent(self, event, data):
		for callback in self.events[event]:
			if callable(callback):
				callback(data)

	def setLevel(self, level):
		self.level = level