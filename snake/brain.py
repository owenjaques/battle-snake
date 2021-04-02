#TODO: move all data processing related functions to a seperate file
# create did collide with self function
# create did collide with wall function
# create did kill other snake function
# remove wall from game data
# create did eat food function

import numpy as np
import json
from game_saver import GameSaver

# TILES = {
# 	EMPTY: 0,
# 	WALL: 1,
# 	BODY: 2,
# 	FOOD: 3,
# 	HEAD: 4
# }

class Brain:
	def __init__(self):
		self.board_width = 0
		self.game_map = None
		self.game_saver = GameSaver()

	def start(self, data):
		self.board_width = data['board']['width'] + 2
		self.update_map(data)

	def move(self, data):
		possible_moves = ["up", "down", "left", "right"]
		self.update_map(data)
		self.game_saver.save_move(data)
		return possible_moves[0]

	def end(self, data):
		self.game_saver.save_move(data)
		self.game_saver.save_game_to_file()

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

		# print(np.flip(self.game_map, 0))