import pygame
import time
import random

pygame.init()

white = (250,250,250)
black = (0, 0, 0)
red = (250, 0, 0)
green = (0, 250, 0)
blue = (0, 0, 250)
violet = (100, 100, 160)

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('snake')


clock = pygame.time.Clock()

block_size = 15
# Fps = 30

font1 = pygame.font.SysFont(None,100)
font2 = pygame.font.SysFont(None,25)
font3 = pygame.font.SysFont(None,50)

def pause():

	paused = True;

	while paused:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_c:
					paused = False
				if event.key == pygame.K_q:
					pygame.quit()
					quit()

		gameDisplay.fill(white)
		message_to_screen1("Paused",
							black,
							25)
		message_to_screen2("Press C to continue or Q to quit.",
							black,
							100)
		pygame.display.update();
		clock.tick(5)									

def score(score):
	text = font3.render("Score : " + str(score), True, violet)
	gameDisplay.blit(text, [0, 0])

def snake(block_size, snakelist):
	for XnY in snakelist:
		pygame.draw.rect(gameDisplay,black,[XnY[0],XnY[1],block_size,block_size])

def text_objects1(text,color):
	textSurface = font1.render(text, True, color)
	return textSurface, textSurface.get_rect()

def text_objects2(text,color):
	textSurface = font2.render(text, True, color)
	return textSurface, textSurface.get_rect()

def message_to_screen1(msg,color,adjust):
	# screen_text = font1.render(msg,True,color)
	# gameDisplay.blit(screen_text,[display_width/2 - 100,display_height/2 - 100])
	textsurf, textRect = text_objects1(msg, color)
	textRect.center = (display_width / 2) , (display_height / 2 - adjust)
	gameDisplay.blit(textsurf, textRect)


def message_to_screen2(msg,color,adjust):
	# screen_text = font2.render(msg,True,color)
	# gameDisplay.blit(screen_text,[display_width/2 - 130,display_height/2 + 100])
	textsurf, textRect = text_objects2(msg, color)
	textRect.center = (display_width / 2) , (display_height / 2 + adjust)	
	gameDisplay.blit(textsurf, textRect)

def gameloop():
	gameexit = True
	gameOver = False
	Fps = 20
	lead_x = display_width/2
	lead_y = display_height/2
	lead_x_change = 0
	lead_y_change = 0
	snakeList = []
	snakelength = 1
	randAppleX = round(random.randrange(0, display_width-block_size))
	randAppleY = round(random.randrange(0, display_height-block_size))
	while gameexit:
		while gameOver:
			gameDisplay.fill(blue)
			message_to_screen1("Game Over",black, 50)
			message_to_screen2("Press R to Restart or Q to quit",black, 50)
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					gameOver = False
					gameexit = False
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_q:
						gameOver = False
						gameexit = False
					if event.key == pygame.K_c:
						gameloop()	
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				gameexit=False
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					lead_x_change = -block_size
					lead_y_change = 0
				elif event.key == pygame.K_RIGHT:
					lead_x_change = block_size
					lead_y_change = 0
				elif event.key == pygame.K_UP:
					lead_y_change = -block_size
					lead_x_change = 0
				elif event.key == pygame.K_DOWN:
					lead_y_change = block_size
					lead_x_change = 0
				elif event.key == pygame.K_p:
					pause()
			if lead_x>=display_width or lead_x<=0 or lead_y<=0 or lead_y>=display_height:
				gameOver = True			
		lead_x+=lead_x_change
		lead_y+=lead_y_change					
		gameDisplay.fill(green)
		AppleThickness = 20
		pygame.draw.rect(gameDisplay,blue,[randAppleX,randAppleY,AppleThickness,AppleThickness])
		snakeHead = []
		snakeHead.append(lead_x)
		snakeHead.append(lead_y)
		snakeList.append(snakeHead)
		if len(snakeList) > snakelength:
			del snakeList[0]

		snake(block_size,snakeList)
		score(snakelength - 1)
		pygame.display.update()
		# if lead_x == randAppleX and lead_y == randAppleY:
		# 	randAppleX = round(random.randrange(0, display_width-block_size)/10.0)*10.0
		# 	randAppleY = round(random.randrange(0, display_height-block_size)/10.0)*10.0
		# 	snakelength += 1
		# 	Fps += 1
		if lead_x > randAppleX and lead_x < randAppleX + AppleThickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + AppleThickness:

			if lead_y > randAppleY and lead_y < randAppleY + AppleThickness:
				randAppleX = round(random.randrange(0, display_width-block_size))
				randAppleY = round(random.randrange(0, display_height-block_size))
				snakelength += 1
			elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + AppleThickness:
				randAppleX = round(random.randrange(0, display_width-block_size))
				randAppleY = round(random.randrange(0, display_height-block_size))
				snakelength += 1
		clock.tick(Fps)			
	pygame.quit()
	quit()
gameloop()	