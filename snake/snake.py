from snake.utilities import *
import random
from collections import OrderedDict

class Snake:
	def __init__(self, save_game=False, is_training=False):
		self.is_training = is_training
		self.save_game = save_game
		self.game_saver = GameSaver() if save_game else None
		
		# tracks the data of each different game so that the snake can play at multiple games at once
		self.games = OrderedDict()

		# the max amount of games that can be played at once
		self.max_games = 16

	def start(self, data):
		# if the list has the max amount of games take out the oldest game
		if len(self.games) >= self.max_games:
			self.games.popitem(0)
		
		# create an entry in the games list for this game
		self.games[data['you']['id']] = []

	def move(self, data):
		if self.save_game:
			self.game_saver.save_move(data)

		self.games[data['you']['id']].append(data)
		return self.get_move()

	def end(self, data):
		if self.save_game:
			self.game_saver.save_move(data)
			self.game_saver.save_game_to_file()

		self.games[data['you']['id']].append(data)
		
		# The game engine only seems to have a bug in it that only sends data to the /end endpoint
		# of the winning snake. This enforces that in case something changes to keep the training
		# consistent.
		if not did_die(data) and self.is_training:
			# appends the missed move to the data of each snake
			for snake in data['board']['snakes']:
				self.games[data['board']['snakes']].append(data)
				self.games[data['board']['snakes']][-1]['you'] = snake

	def get_move(self):
		# TODO: move this to a seperate 'Brain' class once actual decisions are made here
		possible_moves = ['up', 'down', 'left', 'right']
		return random.choice(possible_moves)