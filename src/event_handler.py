class EventHandler:
	def __init__(self):
		self.events = {}

	def on(self, event, callback):
		if not event in self.events:
			self.events[event] = []
		self.events[event].append(callback)
			
	def triggerEvent(self, event, data):
		if not event in self.events: return
		for callback in self.events[event]:
			if callable(callback):
				if data:
					callback(data)
				else:
					callback()