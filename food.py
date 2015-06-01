import pygame
import random

class Food_piece(object):
	def __init__(self,pos,color = (255,0,0)):
		self.m_x = pos[0]
		self.m_y = pos[1]
		self.x = self.m_x * 20
		self.y = self.m_y * 20
		self.color = color

	def blit(self,screen):
		rect = pygame.Rect(self.x,self.y,20,20)
		pygame.draw.rect(screen,self.color,rect)

class Food(object):
	def __init__(self):
		self.food = list()

		self.time = 3000
		self.time_tick = 3000

	def random_pos(self,snake):
                print "random_pos called."
		running = True 
		while running:
			x,y = random.randint(1,19),random.randint(1,19)
			running = False
			for t in snake.tail :
				if t.m_x == x and t.m_y == y :
					running = True
			if x == snake.x and y == snake.y :
				running = True
			for p in self.food :
				if p.m_x == x and p.m_y == y :
					running = True
		return x,y

	def restart(self):
		self.food = []
		self.time = 300

	def update(self,dt,screen,snake):
		self.time += dt
		if len(self.food) <= 0:
			self.time = 0
			x,y = self.random_pos(snake)
			f_piece = Food_piece((x,y))
			self.food.append(f_piece)

		for f_piece in self.food :
			if f_piece.m_x == snake.x and f_piece.m_y == snake.y :
				snake.increase_lenght(1,1)
				self.food.remove(f_piece)
			f_piece.blit(screen)
