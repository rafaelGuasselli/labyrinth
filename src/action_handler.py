class ActionHandler:
	def __init__(self, actions):
		self.actions = actions or {}

	def runAction(self, action, data):
		if not action in self.actions: 
			return
		if not callable(self.actions[action]):
			return
		if data:
			self.actions[action](data)
		else:
			self.actions[action]()