import sys
from block import Block
sys.setrecursionlimit(10**8)

class MazeSolver:
	def solve(self, map, size, pos):
		self.height, self.width = size
		return self.dfs(map, pos, (0, 0), self.createEmptyNotVisitedMatrix())

	def dfs(self, map, currentPosition, direction, notVisited):
		y, x = currentPosition
		lookupQueue = self.createQueueOfBlocksToLookNext(y, x)
		notVisited[y][x] = False
		path = []

		for pos in lookupQueue:
			ny, nx = pos
			dy, dx = direction = (ny-y, nx-x)
			if self.isPlaceNotVisited(notVisited, pos) and map[y][x].canPlayerMoveTo(direction):
				if self.isPlaceExit(map, pos):
					return [direction, (0, 1)]
				else:
					subpath = self.dfs(map, pos, direction, notVisited)
					if len(subpath) > 0:
						return [direction] + subpath
		return []
	
	def isPlaceExit(self, map, pos):
		y, x = pos
		if y >= 0 and x >= 0 and y < self.height and x < self.width:
			return map[y][x].isExit
		return False
	
	def isPlaceNotVisited(self, notVisited, pos):
		y, x = pos
		if y >= 0 and x >= 0 and y < self.height and x < self.width:
			return notVisited[y][x]
		return False

	def createEmptyNotVisitedMatrix(self):
		notVisited = []
		for l in range(0, self.height):
			notVisited.append([])
			for c in range(0, self.width):
				notVisited[l].append(True)
		return notVisited

	def createQueueOfBlocksToLookNext(self, y, x):
		queue = [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]
		return queue