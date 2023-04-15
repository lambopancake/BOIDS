from Boids import BOIDS
import math, pygame, random

if __name__ == '__main__':
	

	screenSize = (1200,700)

	bArr = [None] * 90
	for boids in range(90):
		bArr[boids] = BOIDS([random.randint(0,screenSize[0]),random.randint(0,screenSize[1])], screenSize)
	screen = pygame.display.set_mode(screenSize)

	while True:

		pygame.time.delay(1)
		screen.fill((0,0,0))

		for b in range(90):
			bArr[b].main(screen)
			bArr[b].Alignment(bArr,b,10)











		##################################
		###########IGNORE THIS############
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()
		##################################