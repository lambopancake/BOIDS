import math,pygame, random
from vector import vector
class BOIDS:
	
	#acceleration is the rate that velocity increases
	def __init__(self, pos, screenSize):
		self.accel = pygame.math.Vector2()
		self.velocity = pygame.math.Vector2(random.randint(-50,50)*0.01, random.randint(-50,50)*0.01)
		self.pos = pos #[x,y]
		self.screenSize = screenSize


	def move(self):
		# dx = self.velocity.magnitude * math.cos(math.radians(self.velocity.direction)) #+ self.accel[0]
		# dy = self.velocity.magnitude * math.sin(math.radians(self.velocity.direction)) #+ self.accel[1]

		self.pos = [self.pos[0] + self.velocity[0], self.pos[1] + self.velocity[1]]
		
		#for x/y to  not go beyond the limit
		if(self.pos[0] > self.screenSize[0]):
			self.pos[0] = 0
		if(self.pos[0] < 0):
			self.pos[0] = self.screenSize[0]
		if(self.pos[1] > self.screenSize[1]):
			self.pos[1] = 0
		if(self.pos[1] < 0):
			self.pos[1] = self.screenSize[1]


		self.velocity[0] += self.accel[0]
		self.velocity[1] += self.accel[1]

		if(self.velocity[0] > 1):
			self.velocity[0] = 1
		if(self.velocity[0] < -1):
			self.velocity[0] = -1
		if(self.velocity[1] > 1):
			self.velocity[1] = 1
		if(self.velocity[1] < -1):
			self.velocity[1] = -1


	def separation(self, sep = 1):
		pass

	def Alignment(self,boidArr, i, per):
		x = 0
		y = 0
		per /= 100
		for boid in range(i, len(boidArr), 1):
			x = boidArr[boid].velocity[0]
			y = boidArr[boid].velocity[1]
		#average speed and angle of the entire flock
		x /= len(boidArr)
		y /= len(boidArr)
		#print(aS, " ", aA)
		self.accel = [x * per, y * per]
		maxA = 0.5
		if(self.accel[0] > maxA):
			self.accel[0] = maxA
		if(self.accel[0] < -maxA):
			self.accel[0] = -maxA
		if(self.accel[1] > maxA):
			self.accel[1] = maxA
		if(self.accel[1] < -maxA):
			self.accel[1] = -maxA


	def Cohesion(self):#https://medium.com/@errazkim/boids-simulation-in-java-407d2e924e1f
		pass
	
	def main(self,screen):
		pygame.draw.circle(screen,"BLUE",(self.pos[0],self.pos[1]),15,0)
		self.move()


if __name__ == '__main__':
	
	screenSize = (1200,700)

	bArr = [None] * 5
	for boids in range(5):
		bArr[boids] = BOIDS([600,350] , screenSize)
	screen = pygame.display.set_mode(screenSize)

	while True:
		pygame.time.delay(10)
		screen.fill((0,0,0))

		for b in range(5):
			bArr[b].main(screen)
			bArr[b].Alignment(bArr,b, 10)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()


