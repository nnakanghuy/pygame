import pygame
from random import randint
pygame.init()
WIDTH = 400
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Flappy Bird")

GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
running = True
clock = pygame.time.Clock()

#so do ong
TUBE_WIDTH = 50
tube1_x = 600
tube2_x = 800
tube3_x = 1000
TUBE_VELOCITY = 3
tube1_height = randint(10,340)
tube2_height = randint(10,340)
tube3_height = randint(10,340)
TUBE_GAP = 150

sand = 500

# so do chim
BIRD_X = 50
bird_y = 300
BIRD_WIDTH = 35
BIRD_HEIGHT = 35
bird_drop_velocity = 0
GRAVITY = 0.5

#diem
score = 0
Y_SCORE = 50
tube1_pass = False
tube2_pass = False
tube3_pass = False

pausing = False

number_images = [
    pygame.image.load("0.png"),
    pygame.image.load("1.png"),
    pygame.image.load("2.png"),
    pygame.image.load("3.png"),
    pygame.image.load("4.png"),
    pygame.image.load("5.png"),
    pygame.image.load("6.png"),
    pygame.image.load("7.png"),
    pygame.image.load("8.png"),
    pygame.image.load("9.png"), 
]
gameover_img = pygame.image.load("gameover.png")
message_img = pygame.image.load("message.png")
background_img = pygame.image.load("background.png")
background_img = pygame.transform.scale(background_img,(WIDTH,HEIGHT - 100))
bird_img = pygame.image.load("bird.png")
birdup_img = pygame.image.load("birdup.png")
birddown_img = pygame.image.load("birddown.png")
sand_img = pygame.image.load("base.png")
sand_img = pygame.transform.scale(sand_img,(WIDTH,100))
tube_img = pygame.image.load("tube.png")


while running:
	clock.tick(60)
	screen.fill(GREEN)
	screen.blit(background_img,(0,0))
	#dieu chinh ong khi randint(phai cho vao trong vong while vi height randint)
	tube1_img_up = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube1_height))
	tube1_img_up = pygame.transform.flip(tube1_img_up, False, True)

	tube2_img_up = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube2_height))
	tube2_img_up = pygame.transform.flip(tube2_img_up,False,True)

	tube3_img_up = pygame.transform.scale(tube_img,(TUBE_WIDTH,tube3_height))
	tube3_img_up = pygame.transform.flip(tube3_img_up,False,True)

	tube1_img_down = pygame.transform.scale(tube_img,(TUBE_WIDTH,HEIGHT - tube1_height - TUBE_GAP))
	tube2_img_down = pygame.transform.scale(tube_img,(TUBE_WIDTH,HEIGHT - tube2_height - TUBE_GAP))
	tube3_img_down = pygame.transform.scale(tube_img,(TUBE_WIDTH,HEIGHT - tube3_height - TUBE_GAP))

	#ve ong
	tube1_rect = screen.blit(tube1_img_up,(tube1_x,0))
	tube2_rect = screen.blit(tube2_img_up,(tube2_x,0))
	tube3_rect = screen.blit(tube3_img_up,(tube3_x,0))
	#ve ong doi dien
	tube1_rect_inv = screen.blit(tube1_img_down,(tube1_x,tube1_height + TUBE_GAP))
	tube2_rect_inv = screen.blit(tube2_img_down,(tube2_x,tube2_height + TUBE_GAP))
	tube3_rect_inv = screen.blit(tube3_img_down,(tube3_x,tube3_height + TUBE_GAP))

	#ve chim
	if bird_drop_velocity == 0:
		bird_rect = screen.blit(bird_img,(BIRD_X,bird_y))
	elif bird_drop_velocity > 0:
		bird_rect = screen.blit(birdup_img,(BIRD_X,bird_y))
	else:
		bird_rect = screen.blit(birddown_img,(BIRD_X,bird_y))
	bird_y += bird_drop_velocity
	bird_drop_velocity += GRAVITY

	sand_rect = screen.blit(sand_img,(0,sand))
	#ong di chuyen
	tube1_x = tube1_x - TUBE_VELOCITY
	tube2_x = tube2_x - TUBE_VELOCITY
	tube3_x = tube3_x - TUBE_VELOCITY

	if tube1_x <= -TUBE_WIDTH:
		tube1_x = 550
		tube1_height = randint(10,340)
		tube1_pass = False
	if tube2_x <= -TUBE_WIDTH:
		tube2_x = 550
		tube2_height = randint(10,340)
		tube2_pass = False
	if tube3_x <= -TUBE_WIDTH:
		tube3_x = 550
		tube3_height = randint(10,340)
		tube3_pass = False

	#kiem tra va cham collision
	for tube in ([tube1_rect,tube2_rect,tube3_rect,tube1_rect_inv,tube2_rect_inv,tube3_rect_inv,sand_rect]):
		if bird_rect.colliderect(tube):
			pausing = True
			TUBE_VELOCITY = 0
			bird_drop_velocity = 0
			screen.blit(gameover_img,(100,100))
			screen.blit(message_img,(100,200))

	# tinh diem
	if tube1_x + TUBE_WIDTH <= BIRD_X and tube1_pass == False:
		score +=1
		tube1_pass = True
	if tube2_x + TUBE_WIDTH <= BIRD_X and tube2_pass == False:
		score +=1
		tube2_pass = True
	if tube3_x + TUBE_WIDTH <= BIRD_X and tube3_pass == False:
		score +=1
		tube3_pass = True
	score_img = str(score)
	# giu toa do ve ban 
	x_score = 180
	for d in score_img:
		img = number_images[int(d)]
		screen.blit(img,(x_score,Y_SCORE))
		x_score += img.get_width()

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type ==pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				if pausing:
					tube1_x = 600
					tube2_x = 800
					tube3_x = 1000
					bird_y = 300
					pausing = False
					score = 0
					TUBE_VELOCITY = 3
				bird_drop_velocity = 0
				bird_drop_velocity -= 9
	pygame.display.flip()

pygame.quit()
