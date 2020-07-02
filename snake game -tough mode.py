import pygame
win=pygame.display.set_mode((500,500))
pygame.display.set_caption("first game")
x=50
y=50
x1=0
y1=0
width=10
height=20
v=10
run=True
#time=pygame.time.Clock()
while run:
	pygame.time.delay(100)
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			run=False
		key=pygame.key.get_pressed()
		if key[pygame.K_LEFT]:
			x1-=v
			if x==-height:
				x=500
		if key[pygame.K_RIGHT]:
			x1+=v
			if x==500:
				x=0
		if key[pygame.K_DOWN]:
			y1+=v
			if y==500:
				y=0
		#else key[pygame.K_UP]:
			y1-=v
			if y==-height:
				y=500
	x+=x1
	y+=y1
	win.fill((0,0,0))
	pygame.draw.rect(win,(255,0,0),(x,y,width,height))
	#time.tick(20)
	#pygame.draw.rect(win,(255,255,255),(100,300,10,10))
	pygame.display.update()
pygame.quit()
