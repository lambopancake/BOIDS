import math,pygame
class BOIDS:
	
	def __init__(self, vel, angle, pos, screenSize):
		self.vel = vel #veleocity
		self.angle = angle #degree
		self.pos = pos #[x,y]
		self.screenSize = screenSize

	def move(self):
		dx = self.vel * math.cos(math.radians(self.angle))
		dy = self.vel * math.sin(math.radians(self.angle))
		self.pos = [self.pos[0] + dx, self.pos[1] + dy]
		#for x to  
		if(self.pos[0] > self.screenSize[0]):
			self.pos[0] = 0
		if(self.pos[0] < 0):
			self.pos[0] = self.screenSize[0]
		if(self.pos[1] > self.screenSize[1]):
			self.pos[1] = 0
		if(self.pos[1] < 0):
			self.pos[1] = self.screenSize[1]


	def separation(self):
		pass

	def Alignment(self):
		pass

	def Cohesion(self):
		pass
	
	def main(self,screen):
		pygame.draw.circle(screen,"BLUE",(self.pos[0],self.pos[1]),15,0)
		self.move()


if __name__ == '__main__':
	
	screenSize = (1200,700)

	bArr = [None] * 1
	for boids in range(1):
		bArr[boids] = BOIDS(0.5,boids*4,[600,350], screenSize)
	screen = pygame.display.set_mode(screenSize)

	while True:
		pygame.time.delay(1)
		screen.fill((0,0,0))

		for b in range(1):
			bArr[b].main(screen)
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()


