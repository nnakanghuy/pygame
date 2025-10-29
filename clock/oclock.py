import pygame
import time
import math
pygame.init()
screen = pygame.display.set_mode((550, 700))

GREY = (150,150,150)
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

running = True
font = pygame.font.SysFont('sans', 50)
text_1 = font.render("+",True,BLACK)
text_2 = font.render("-",True,BLACK)
# text_3 = font.render("+",True,BLACK)
# text_4 = font.render("-",True,BLACK)
# text_5 = font.render("+",True,BLACK)
# text_6 = font.render("-",True,BLACK)
text_7 = font.render("Start",True,BLACK)
text_8 = font.render("Reset",True,BLACK)

total_secs = 0
total = 0
start = False

sound = pygame.mixer.Sound("clock.wav")
clock = pygame.time.Clock()

while running:
	clock.tick(60)
	mouse_x, mouse_y = pygame.mouse.get_pos()

	screen.fill(GREY)
	pygame.draw.rect(screen,WHITE,(100,50,50,50))
	pygame.draw.rect(screen,WHITE,(100,200,50,50))
	pygame.draw.rect(screen,WHITE,(250,50,50,50))
	pygame.draw.rect(screen,WHITE,(250,200,50,50))
	pygame.draw.rect(screen,WHITE,(400,50,50,50))
	pygame.draw.rect(screen,WHITE,(400,200,50,50))

	pygame.draw.rect(screen,WHITE,(70,300,130,50))
	pygame.draw.rect(screen,WHITE,(350,300,130,50))

	pygame.draw.circle(screen,BLACK,(275,450),100)
	pygame.draw.circle(screen,WHITE,(275,450),97)
	pygame.draw.circle(screen,BLACK,(275,450),3)

	pygame.draw.rect(screen,BLACK,(100,570,350,50))
	pygame.draw.rect(screen,WHITE,(102,572,346,46))

	screen.blit(text_1,(100,50))
	screen.blit(text_2,(100,200))
	screen.blit(text_1,(250,50))
	screen.blit(text_2,(250,200))
	screen.blit(text_1,(400,50))
	screen.blit(text_2,(400,200))
	screen.blit(text_7,(70,300))
	screen.blit(text_8,(350,300))

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.MOUSEBUTTONDOWN:
			if event.button == 1:
				pygame.mixer.pause()
				if (100 < mouse_x < 150) and (50 < mouse_y < 100):
					total_secs += 3600
					# luc nao cung phai co total de ma khi bam tang giam thi khoang cach cua vach do van o trong pvi
					total = total_secs
					print("press + hour")
				if (100 < mouse_x < 150) and (200 < mouse_y < 250):
					total_secs -= 3600
					total = total_secs
					print("press - hour")
				if (250 < mouse_x < 300) and (50 < mouse_y < 100):
					total_secs += 60
					total = total_secs
					print("press + min")
				if (250 < mouse_x < 300) and (200 < mouse_y < 250):
					total_secs -= 60
					total = total_secs
					print("press - min")
				if (400 < mouse_x < 450) and (50 < mouse_y < 100):
					total_secs += 1
					total = total_secs
					print("press + sec")
				if (400 < mouse_x < 450) and (200 < mouse_y < 250):
					total_secs -= 1
					total = total_secs
					print("press - sec")
				if (70 < mouse_x < 200) and (300 < mouse_y < 350):
					start = True
					total = total_secs
					print("press Start")
				if (350 < mouse_x < 480) and (300 < mouse_y < 350):
					total_secs = 0
					print("press Reset")
	if start:
		total_secs -= 1
		if total_secs == 0:
			start = False
			pygame.mixer.Sound.play(sound)
		time.sleep(0.1)

	if total_secs < 0:
		total_secs = 0

	hours = int(total_secs/3600)
	mins = int((total_secs - hours*3600)/60)
	secs = total_secs - hours*3600 - mins*60

	time_now = str(hours) + "     :     " + str(mins) + "     :     " + str(secs)
	text_time = font.render(time_now,True,BLACK)
	screen.blit(text_time,(120,120))

	x_hour = 275 + 30 *math.sin(6*hours * math.pi/180)
	y_hour = 450 - 30 *math.cos(6*hours * math.pi/180)
	pygame.draw.line(screen,RED,(275,450),(int(x_hour),int(y_hour)))

	x_min = 275 + 70 *math.sin(6*mins * math.pi/180)
	y_min = 450 - 70 *math.cos(6*mins * math.pi/180)
	pygame.draw.line(screen,BLUE,(275,450),(int(x_min),int(y_min)))

	x_sec = 275 + 90 *math.sin(6*secs * math.pi/180)
	y_sec = 450 - 90 *math.cos(6*secs * math.pi/180)
	pygame.draw.line(screen,BLACK,(275,450),(int(x_sec),int(y_sec)))

	if total != 0:
		pygame.draw.rect(screen,RED,(102,572,int(346*total_secs/total),46))

	pygame.display.flip()


pygame.quit()