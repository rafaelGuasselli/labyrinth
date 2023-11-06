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

		if self.isPlaceExit(map, currentPosition):
			return [(0, 1), direction]
	
		for nextPos in lookupQueue:
			ny, nx = nextPos
			nextDirection = (ny-y, nx-x)
			if self.isPlaceNotVisited(notVisited, nextPos) and self.canMoveTo(map, currentPosition, nextDirection):
				subpath = self.dfs(map, nextPos, nextDirection, notVisited)
				if subpath and len(subpath) > 0:
					return subpath + [direction]
		return False
	
	def isPlaceExit(self, map, pos):
		y, x = pos
		if self.isMatrixPosition(pos):
			return map[y][x].isExit
		return False
	
	def canMoveTo(self, map, pos, direction):
		y, x = pos
		if self.isMatrixPosition(pos):
			return map[y][x].canPlayerMoveTo(direction)
		return False
	
	def isPlaceNotVisited(self, notVisited, pos):
		y, x = pos
		if self.isMatrixPosition(pos):
			return notVisited[y][x]
		return False
	
	def isMatrixPosition(self, pos):
		y, x = pos
		return y >= 0 and x >= 0 and y < self.height and x < self.width

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