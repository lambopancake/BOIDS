from Boids import BOIDS
import math, pygame, random, threading
from tkinter import * 

SepConst = 0
def chaSep(a):
	global SepConst
	SepConst = float(a)


AliConst = 0
def chaAli(a):
	global AliConst
	AliConst = float(a)

CohConst = 0
def chaCoh(a):
	global CohConst
	CohConst = float(a)
RadConst = 0
def RadCoh(a):
	global RadConst
	RadConst = float(a)

def slider():
	print("running")
	slides = Tk()
	Sep = Scale(slides, label = "Separation", from_ = 0, to = 50, resolution = 0.01, command = chaSep, orient = "horizontal" )
	Sep.set(5)
	Sep.pack()

	Rad = Scale(slides, label = "RAD", from_ = 0, to = 50, resolution = 0.01, command = RadCoh, orient = "horizontal" )
	Rad.set(35)
	Rad.pack()

	ali = Scale(slides, label = "Alignment", from_ = 0, to = 50, resolution = 0.01, command = chaAli, orient = "horizontal" )
	ali.set(3)
	ali.pack()

	Coh = Scale(slides, label = "Cohesion", from_ = 0, to = 50, resolution = 0.01, command = chaCoh, orient = "horizontal" )
	Coh.set(5)
	Coh.pack()

	mainloop()

t1 = threading.Thread(target = slider)
t1.start()

if __name__ == '__main__':
	
	a = 100
	screenSize = (1200,700)
	screen = pygame.display.set_mode(screenSize)
	bArr = [None] * a
	for boids in range(a):
		bArr[boids] = BOIDS([random.randint(0,screenSize[0]),random.randint(0,screenSize[1])], screenSize, screen)
	
	
	while True:

		pygame.time.delay(1)
		screen.fill((0,0,0))
		print(SepConst, " ", AliConst, " ",CohConst)
		
		

		for b in range(a):
			bArr[b].perSep = SepConst
			bArr[b].perAli = AliConst
			bArr[b].perCoh = CohConst
			bArr[b].SepRad = RadConst 
			bArr[b].main(screen,b, bArr)
			#bArr[b].Alignment(100)
			#bArr[b].neighbor(b, bArr,100)
			#bArr[b].separation(bArr,cb)
		

			











		##################################
		###########IGNORE THIS############
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				exit()
		pygame.display.update()
		##################################