import math,pygame, random
class BOIDS:
	
	#acceleration is the rate that velocity increases
	def __init__(self, pos, screenSize,screen = None):
		self.accel = pygame.math.Vector2()
		self.velocity = pygame.math.Vector2(random.randint(-50,50)*0.01, random.randint(-50,50)*0.01)
		self.pos = pos #[x,y]
		self.screenSize = screenSize
		self.screen = screen


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


	def neighbor(self, i, arr, limDist):
		neighbor = []
		for boid in range(i, len(arr), 1):
			dist = math.sqrt(pow((arr[boid].pos[0]- self.pos[0]),2) + pow((arr[boid].pos[1]- self.pos[1]),2))
			if(dist < limDist):
				pygame.draw.line(self.screen, "GREEN",self.pos,arr[boid].pos)
				neighbor.append(arr[boid])
		return neighbor

	def separation(self, boidArr, i, sep = 10):
		neig = self.neighbor(i,boidArr, 70)
		for boid in range(i, len(boidArr), 1):
			if((boidArr[boid] in neig)):
				if(abs(boidArr[boid].pos[0] - self.pos[0]) < sep):
					if(boidArr[boid].pos[0] <= self.pos[0]):
						self.velocity[0] += 0.1
					else:
						self.velocity[0] -= 0.1

				if(abs(boidArr[boid].pos[1] - self.pos[1]) < sep):
					if(boidArr[boid].pos[1] <= self.pos[1]):
						self.velocity[1] += 0.1
					else:
						self.velocity[1] -= 0.1


				

	def Alignment(self,boidArr, i, per = 70):
		x = 0
		y = 0
		per /= 100
		neig = self.neighbor(i,boidArr, 100)
		for boid in range(i, len(boidArr), 1):
			if(boidArr[boid] in neig):
				x = boidArr[boid].velocity[0]
				y = boidArr[boid].velocity[1]
		#average speed and angle of the entire flock
		x /= len(boidArr)
		y /= len(boidArr)
		#print(aS, " ", aA)
		# self.accel = [x * per, y * per]
		self.accel[0] = x * per
		self.accel[1] = y * per
		maxA = 0.5# mess around with this number
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
	screen = pygame.display.set_mode(screenSize)
	bArr = [None] * 5
	for boids in range(5):
		bArr[boids] = BOIDS([random.randint(-300,300),random.randint(-300,300)] , screenSize, screen)
	

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


