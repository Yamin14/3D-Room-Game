import pygame
pygame.init()

width, height = 700, 900
screen = pygame.display.set_mode((width, height))
running = True
line_width = 3

#colours
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 255, 255)
white = (255, 255, 255)
black = (0, 0, 0)
grey = (140, 140, 140)

#character
speed = 10
tall, fat = 250, 150
x, y = 200, 550
		
while running:
	screen.fill(grey)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w or event.key == pygame.K_UP:
				if y > 550 and y +tall- 900 > -2* x and y +tall- 700 > 2*(x-600+fat) :
					y -= speed
				elif y > 550 and y +tall- 900 > -2* x:
					x -= speed
					y -= speed
				elif y > 550 and y +tall- 700 > 2*(x-600+fat):
					x += speed
					y -= speed

			elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
				if y < 650:
					y += speed

			elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
				if y +tall- 900 > -2* x:
					x -= speed

			elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
				if y +tall- 700 > 2*(x-600+fat):
					x += speed

	#screen boundary
	pygame.draw.line(screen, black, (width, 0), (width, height))
	pygame.draw.line(screen, black, (0, height), (width, height))

	#room
	pygame.draw.line(screen, black, (100, 200), (100, 700), line_width)
	pygame.draw.line(screen, black, (100, 200), (600, 200), line_width)
	pygame.draw.line(screen, black, (600, 200), (600, 700), line_width)
	pygame.draw.line(screen, black, (100, 700), (600, 700), line_width)
	
	pygame.draw.line(screen, black, (100, 200), (0, 0), line_width)
	pygame.draw.line(screen, black, (600, 200), (width, 0), line_width)
	pygame.draw.line(screen, black, (100, 700), (0, height), line_width)
	pygame.draw.line(screen, black, (600, 700), (width, height), line_width)

	#character
	pygame.draw.rect(screen, black, (x-line_width, y-line_width, fat+(line_width*2), tall+(line_width*2)))
	pygame.draw.rect(screen, blue, (x, y, fat, tall))
	
	pygame.draw.polygon(screen, black, [(x-line_width, y-line_width), (x+20, y-50), (x+fat-20, y-50), (x+line_width+fat, y-line_width)])
	pygame.draw.polygon(screen, blue, [(x, y-line_width), (x+20, y-50), (x+fat-20, y-50), (x+fat, y-line_width)])

	pygame.display.flip()
pygame.quit()
