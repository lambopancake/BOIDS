import math,pygame,random,time
class BOIDS:

	radDist = 80

	#acceleration is the rate that velocity increases
	def __init__(self, pos, screenSize,screen):
		self.accel = pygame.math.Vector2(random.randint(-50, 50) * 0,random.randint(-50, 50) * 0)
		self.velocity = pygame.math.Vector2(random.randint(-50,50) * 0.01, random.randint(-50,50) * 0.01)
		self.pos = pos #[x,y]
		self.screenSize = screenSize
		self.screen = screen
		self.neighbor = {}
		self.perSep = 5
		self.SepRad = 35
		self.perAli = 3
		self.perCoh = 5


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

		#print("this should be accel ",self.accel)
		self.velocity[0] += self.accel[0]
		self.velocity[1] += self.accel[1]
		#print(self, ": ", self.velocity)

		a = 1
		if(self.velocity[0] >= a):
			self.velocity[0] = a
		if(self.velocity[0] < -a):
			self.velocity[0] = -a
		if(self.velocity[1] >= a):
			self.velocity[1] = a
		if(self.velocity[1] < -a):
			self.velocity[1] = -a


	def neighbors(self, arr, limDist):
		self.neighbor = {}
		for boid in range(len(arr)):
			dist = math.sqrt(pow((arr[boid].pos[0]- self.pos[0]),2) + pow((arr[boid].pos[1]- self.pos[1]),2))
			if(dist < BOIDS.radDist and self != arr[boid]):
				#pygame.draw.line(self.screen, "GREEN",self.pos,arr[boid].pos)
				self.neighbor[arr[boid]] = dist

	def Separation(self):
		per = self.SepRad
		x = 0
		y = 0
		keyList = list(self.neighbor.keys())
		for near in range(len(keyList)):
			if(self.neighbor[keyList[near]] < per):
				x += self.pos[0] - keyList[near].pos[0]
				y += self.pos[1] - keyList[near].pos[1]
		a = 0.0001 * self.perSep
		self.accel[0] += x*a
		self.accel[1] += y*a


	def Alignment(self):
		x = self.velocity[0]
		y = self.velocity[1]
		keyList = list(self.neighbor.keys())
		for nearest in range(len(keyList)):
			x += keyList[nearest].velocity[0]
			y += keyList[nearest].velocity[1]
		if(len(keyList) > 0):	
			x /= len(keyList) + 1
			y /= len(keyList) + 1
			a = 0.001 * self.perAli
			#print(self.pos," ",x," ",y)
			self.accel[0] += x*a
			self.accel[1] += y*a

	def Cohesion(self):#https://medium.com/@errazkim/boids-simulation-in-java-407d2e924e1f
		x = self.pos[0]
		y = self.pos[1]
		keyList = list(self.neighbor.keys())
		for nearest in range(len(keyList)):
			x += keyList[nearest].pos[0]
			y += keyList[nearest].pos[1]
		if(len(keyList) > 0):	
			x /= len(keyList) + 1
			y /= len(keyList) + 1
			#figure out how to use the average (a,y)
			#pygame.draw.circle(self.screen,"WHITE",(x,y),10,0)
			x = self.pos[0] - x
			y = self.pos[1] - y
			a = 0.0001 * self.perCoh
			#print(self.pos," ",x," ",y)
			self.accel[0] -= x*a
			self.accel[1] -= y*a

	def main(self,screen, i, arr,):
		pygame.draw.circle(screen,"BLUE",(self.pos[0],self.pos[1]),10,0)
		#self.velocity = [self.velocity[0] + self.accel[0], self.velocity[1] + self.accel[1]]
		self.move()
		self.accel = [0,0]
		self.neighbors(arr, 100)
		self.Cohesion()
		self.Separation()
		self.Alignment()


if __name__ == '__main__':
	
	screenSize = (1200,700)
	screen = pygame.display.set_mode(screenSize)
	a = 15
	bArr = [None] * a
	for boids in range(a):
		bArr[boids] = BOIDS([random.randint(-300,300),random.randint(-300,300)] , screenSize, screen)
	
	bArr[boids].accel = [0.01,0.01]
	while True:
		pygame.time.delay(10)
		screen.fill((0,0,0))

		for b in range(a):
			bArr[b].main(screen, b, bArr)
		
		#time.sleep(1)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()


