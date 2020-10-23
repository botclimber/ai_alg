# GENERIC CLASS

# INITIAL STATE
# FINAL STATE
# ALL STATES
# TARGET TEST (COMPARE ACTUAL STATE WITH TARGET STATE)
# ACTIONS


class magicBox:	

	def __init__(self, iState, fState = 0):
		
		self.iState = iState
		self.fState = fState # optional

	def chState(self):
		# METHOD TO MOVE INTO NEXT STATE
		return		

	def whoami(self):
		print(self.iState)
		print(self.fState)
