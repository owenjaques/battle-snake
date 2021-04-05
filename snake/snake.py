from snake.utilities import *
import random

class Snake:
	def __init__(self, save_game=False):
		self.save_game = save_game
		self.game_saver = GameSaver() if save_game else None

	def start(self, data):
		pass

	def move(self, data):
		if self.save_game:
			self.game_saver.save_move(data)
		
		return self.get_move(data)

	def end(self, data):
		if self.save_game:
			self.game_saver.save_move(data)
			self.game_saver.save_game_to_file()
		
		print('Winning Game?', not did_die(data))

	def get_move(self, data):
		# TODO: move this to a seperate 'Brain' class once actual decisions are made here
		possible_moves = ['up', 'down', 'left', 'right']
		return random.choice(possible_moves)