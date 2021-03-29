import numpy as np

class Brain:
	def __init__(self):
		self.board_width = 0
		self.game = None

	def start(self, data):
		self.board_width = data['board']['width'] + 2
		self.game_map = np.zeros((self.board_width, self.board_width), dtype=int)

	def update_map(self, data):
		self.game_map = np.zeros((self.board_width, self.board_width), dtype=int)
		
		#adds walls to map
		for i in range(self.board_width):
			self.game_map[i][0] = 1
			self.game_map[i][self.board_width-1] = 1
			self.game_map[0][i] = 1
			self.game_map[self.board_width-1][i] = 1

		#adds all snake parts to map
		for snake in data['board']['snakes']:
			for points in snake['body']:
				x = points['x'] + 1
				y = points['y'] + 1
				self.game_map[y][x] = 2

		#adds all food to map
		for food in data['board']['food']:
			x = food['x'] + 1
			y = food['y'] + 1
			self.game_map[y][x] = 3

		#adds head to map
		head = data['you']['body'][0]
		x = head['x'] + 1
		y = head['y'] + 1
		self.game_map[y][x] = 4

		print(np.flip(self.game_map, 0))