import pygame
import player
import food

class Game_Window(object):
	def __init__(self):
		pygame.init()

		self.screen = pygame.display.set_mode((400,400),0,32)
		self.clock = pygame.time.Clock()
		self.player = player.Snake(400,400)
                self.Food = food.Food()

                self.font = pygame.font.SysFont('Comic Sans MS',40)
                
	def blit_grid(self):
		for x in range(20):
			pygame.draw.aaline(self.screen,(255,255,255),(x*20,0),(x*20,400))
		for y in range(20):
			pygame.draw.aaline(self.screen,(255,255,255),(0,y*20),(400,y*20))

	def game_over(self):
		running = True
		time = 0
		self.player.is_dead = False
		self.clock.tick()
		self.player.restart()
		self.Food.restart()

	def run(self):
		while True :
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					exit()
			self.screen.fill((255,255,255))

			dt = self.clock.tick()
			self.player.update(dt,self.screen)
			self.Food.update(dt,self.screen,self.player)
			self.blit_grid()

			if self.player.is_dead :
				self.game_over()

			point = self.font.render(str(self.player.point),True,(0,0,0))
			self.screen.blit(point,(0,0))
			pygame.display.update()


if __name__ == '__main__':
	app = Game_Window()
	app.run()
