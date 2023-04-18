from Boids import BOIDS
import math, pygame, random,time

if __name__ == '__main__':
	

	screenSize = (1200,700)
	screen = pygame.display.set_mode(screenSize)
	bArr = [None] * 100
	for boids in range(100):
		bArr[boids] = BOIDS([random.randint(0,screenSize[0]),random.randint(0,screenSize[1])], screenSize, screen)
	

	while True:

		pygame.time.delay(1)
		screen.fill((0,0,0))

		for b in range(100):
			bArr[b].main(screen,b, bArr)
			#bArr[b].Alignment(100)
			#bArr[b].neighbor(b, bArr,100)
			#bArr[b].separation(bArr,b)
		

			











		##################################
		###########IGNORE THIS############
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()
		##################################