import json
from enum import Enum
import numpy as np

# TODO: create did collide with self function
# TODO: create did collide with wall function
# TODO: create did kill other snake function
# TODO: create did eat food function

# TODO: move this to a seperate 'constants' file
FREE = 0
FOOD = 1
SNAKE = 2
HEAD = 3

class GameSaver:
	def __init__(self):
		self.game_data = []

	def save_move(self, data):
		self.game_data.append(data)

	def save_game_to_file(self):
		try:
			id = self.game_data[0]['game']['id']
		except:
			print('Game data is empty. Not saving to file.')

		try:
			with open('game_data/' + id +'.json', 'x') as f:
				json.dump(self.game_data, f)
		except Exception as e:
			print('Error saving game data to file.')
			print(e)

def get_map(data):
	board_width = data['board']['width']
	game_map = np.zeros((board_width, board_width), dtype=int)

	# adds all food to map
	for food in data['board']['food']:
		x = food['x']
		y = food['y']
		game_map[y][x] = FOOD
	
	# adds all snake parts to map
	for snake in data['board']['snakes']:
		for points in snake['body']:
			x = points['x']
			y = points['y']
			game_map[y][x] = SNAKE

	# adds your snake's head to map
	head = data['you']['body'][0]
	x = head['x']
	y = head['y']
	game_map[y][x] = HEAD

	return game_map

def print_map(game_map):
	# flips the y axis so that it can match what the screen shows
	print(np.flip(game_map, 0))