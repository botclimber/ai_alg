# GENERIC CLASS

# INITIAL STATE
# FINAL STATE
# ALL STATES
# TARGET TEST (COMPARE ACTUAL STATE WITH TARGET STATE)
# ACTIONS

import numpy as np
import random
import sys

sys.setrecursionlimit(10**4)

class magicBox:

	def __init__(self, i, j, iState, fState = 0): # iState initial State, fState final State target
		self.cost = 0 # number of state changes

		self.rows = i
		self.cols = j

		self.aState = np.array(iState)
		self.fState = np.array(fState) # optional

	def chState(self):
	# METHOD TO CHANGE STATE

		if np.array_equal(self.aState, self.fState):
			return [[self.aState],[self.cost]]

		past_zI = None # save past i position
		past_zJ = None # save past j position

		iCounter = 1 # when 1 increments i ,0 decrementes i
		jCounter = 1 # when 1 increments j ,0 decrementes j

		while np.array_equal(self.aState, self.fState) == False:
			zIndex = np.where( self.aState == None ) # empty space current position

			x = random.randrange(0,2) # generates randomly move between 0 or 1, if i increment j if 0 increments i

			# aux variables with empty position
			zJ = zIndex[1][0]
			zI = zIndex[0][0]

			# move to a valid position of matrix, check if position exists by knowing the border of matrix. Generates coordenates ij for new empty space
			if x:
				if jCounter:
					if zJ+1 < self.cols:
						zJ += 1
					else:
						zJ -= 1
						jCounter = 0
				else:
					if zJ > 0:
						zJ -= 1
					else:
						zJ += 1
						jCounter = 1
			else:
				if iCounter:
					if zI+1 < self.rows:
						zI += 1
					else:
						zI -= 1
						iCounter = 0
				else:
					if zI > 0:
						zI -= 1
					else:
						zI += 1
						iCounter = 1

			# certificates that dont move to the same place in a row
			if zI == past_zI and zJ == past_zJ:
				zI = zIndex[0][0] + 1 if zIndex[0][0] + 1 < self.rows and zIndex[0][0] == zI else zIndex[0][0] - 1 if (zIndex[0][0] > 0 and zIndex[0][0] == zI) else zIndex[0][0]
				zJ = zIndex[1][0] + 1 if zIndex[1][0] + 1 < self.cols and zIndex[1][0] == zJ else zIndex[1][0] - 1 if (zIndex[1][0] > 0 and zIndex[1][0] == zJ) else zIndex[1][0]

			# trades empty space with an other value of matrix
			aux = self.aState[zI][zJ]
			self.aState[zI][zJ] = None
			self.aState[zIndex[0][0]][zIndex[1][0]] = aux

			self.cost += 1 # number of moves

			past_zI = zIndex[0][0]
			past_zJ = zIndex[1][0]

			print(self.cost)
			print("Actual State: {}".format(self.aState))

		return [[self.aState],[self.cost]]


	def whoami(self):
		print(self.aState)
		print(self.fState)
