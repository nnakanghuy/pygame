import pygame
import time
from random import randint
pygame.init()
WIDTH =601
HEIGHT = 601
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("snake")

BLACK = (0,0,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
RED = (255,0,0)

snakes = [[5,6]]
direction = "right"

apple=[randint(0,19),randint(0,19)]

clock = pygame.time.Clock()
running = True
pausing = False

score = 0

big_font = pygame.font.SysFont('sans', 50)
small_font = pygame.font.SysFont('sans', 20)

apple_img = pygame.image.load("apple.png")
apple_img = pygame.transform.scale(apple_img,(30,30))

background_img = pygame.image.load("grass.jpg")
background_img = pygame.transform.scale(background_img,(WIDTH,HEIGHT))

snake_head_img = pygame.image.load("snake_head.png")
snake_head_img = pygame.transform.scale(snake_head_img,(30,30))

snake_body_img = pygame.image.load("snake_body.png")
snake_body_img = pygame.transform.scale(snake_body_img,(30,30))

snake_tail_img = pygame.image.load("snake_tail.png")
snake_tail_img = pygame.transform.scale(snake_tail_img,(30,30))


#speed
SPEED_SNAKE = 70
time_move = 0
#so sanh giua 2 flames khoang tgian ran ch an va an apple
snake_before_apple = 0
snake_after_apple = 0
like = False

while running:
	dt = clock.tick(60)
	screen.fill(BLACK)
	screen.blit(background_img,(0,0))

	if direction == "up":
		tail_img_rot = pygame.transform.rotate(snake_tail_img, 180)
		head_img_rot = pygame.transform.rotate(snake_head_img, 0)
		body_img_rot = pygame.transform.rotate(snake_body_img, 0)
	if direction == "down":
		tail_img_rot = pygame.transform.rotate(snake_tail_img, 0)
		head_img_rot = pygame.transform.rotate(snake_head_img, 180)
		body_img_rot = pygame.transform.rotate(snake_body_img, 0)
	if direction == "left":
		tail_img_rot = pygame.transform.rotate(snake_tail_img, -90)
		head_img_rot = pygame.transform.rotate(snake_head_img, 90)
		body_img_rot = pygame.transform.rotate(snake_body_img, 90)
	if direction == "right":
		tail_img_rot = pygame.transform.rotate(snake_tail_img, 90)
		head_img_rot = pygame.transform.rotate(snake_head_img, -90)
		body_img_rot = pygame.transform.rotate(snake_body_img, -90)
	tail_x = snakes[0][0]
	tail_y = snakes[0][1]

	# for i in range(21):
	# 	pygame.draw.line(screen, WHITE, (0,30*i), (600,30*i))
	# 	pygame.draw.line(screen, WHITE, (30*i,0), (30*i,600))

	for index,snake in enumerate(snakes):
		if len(snakes) == 1:
			snake_rect = screen.blit(head_img_rot,(snake[0]*30, snake[1]*30))
		else:
			if index == 0:
				screen.blit(tail_img_rot,(snake[0]*30, snake[1]*30))
			elif index == len(snakes)-1:
				screen.blit(head_img_rot,(snake[0]*30, snake[1]*30))
			else:
				screen.blit(body_img_rot,(snake[0]*30, snake[1]*30))

	apple_rect = screen.blit(apple_img,(apple[0]*30, apple[1]*30))


	#an diem
	if snakes[-1][0] == apple[0] and snakes[-1][1] == apple[1]:
		snakes.insert(0,[tail_x,tail_y])
		apple=[randint(0,19),randint(0,19)]
		score += 1
		snake_after_apple +=1
		like = False


	score_txt = small_font.render("score: " + str(score) , True, WHITE)
	screen.blit(score_txt,(0,0))


	time_move +=dt

	#va cham
	if snakes[-1][0] < 0 or snakes[-1][0] > 19 or snakes[-1][1] < 0 or snakes[-1][1] > 19:
		pausing = True

	if pausing:
		game_over_txt = big_font.render("GAME OVER, SCORE: " + str(score),True,WHITE)
		again_txt = big_font.render("SPACE TO CONTINUE", True, WHITE)
		screen.blit(game_over_txt,(100,100))
		screen.blit(again_txt, (100,170))
		time_move =0

	# time.sleep(0.05)
	#snake move
	if pausing == False and time_move >= SPEED_SNAKE:
		if direction == "up":
			snakes.append([snakes[-1][0],snakes[-1][1] - 1])
			snakes.pop(0)
		if direction == "down":
			snakes.append([snakes[-1][0],snakes[-1][1] + 1])
			snakes.pop(0)
		if direction == "left":
			snakes.append([snakes[-1][0] - 1,snakes[-1][1]])
			snakes.pop(0)
		if direction == "right":
			snakes.append([snakes[-1][0] + 1,snakes[-1][1]])
			snakes.pop(0)
		time_move -= SPEED_SNAKE
		if like == False:
			snake_before_apple +=1
		like = True


	for i in range(len(snakes) -1):
		if snakes[-1][0] == snakes[i][0] and snakes[-1][1] == snakes[i][1] and snake_after_apple != snake_before_apple:
			pausing = True
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP and direction != "down":
				direction = "up"
			if event.key == pygame.K_DOWN and direction != "up":
				direction = "down"
			if event.key == pygame.K_LEFT and direction != "right":
				direction = "left"
			if event.key == pygame.K_RIGHT and direction != "left":
				direction = "right"
			if event.key == pygame.K_SPACE and pausing == True:
				pausing = False
				direction = "right"
				snakes = [[5,6]]
				apple = [randint(0,19), randint(0,19)]
				score = 0
				snake_after_apple = 0
				snake_before_apple = 0
				like = False

	pygame.display.flip()

pygame.quit()
