class vector:
	def __init__(self, mag = 0, direc = 0):
		self.magnitude = mag
		self.direction = direc

	def calc(self):
		dx = self.velocity.magnitude * math.cos(math.radians(self.velocity.direction))
		dy = self.velocity.magnitude * math.sin(math.radians(self.velocity.direction))
		return [dx, dy]

	def add(self,  otherVector):
		dxy1 = self.calc()
		dxy2 = otherVector.calc()
		return [dxy1[0] + dxy2[0], dxy1[1] + dxy2[1]]
