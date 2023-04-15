from Boids import BOIDS
import math, pygame, random

if __name__ == '__main__':
	

	screenSize = (1200,700)
	screen = pygame.display.set_mode(screenSize)
	bArr = [None] * 90
	for boids in range(90):
		bArr[boids] = BOIDS([random.randint(0,screenSize[0]),random.randint(0,screenSize[1])], screenSize, screen)
	

	while True:

		pygame.time.delay(1)
		screen.fill((0,0,0))

		for b in range(90):
			bArr[b].main(screen)
			#bArr[b].separation(bArr,b)
			bArr[b].Alignment(bArr,b,150)
			











		##################################
		###########IGNORE THIS############
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()
		##################################