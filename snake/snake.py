from utilities import *
import random

class Snake:
	def __init__(self):
		self.game_saver = GameSaver()

	def start(self, data):
		pass

	def move(self, data):
		self.game_saver.save_move(data)
		print_map(get_map(data))
		return self.get_move(data)

	def end(self, data):
		self.game_saver.save_move(data)
		self.game_saver.save_game_to_file()
		print('Winning Game?', not did_die())

	def get_move(self, data):
		# TODO: move this to a seperate 'Brain' class once actual decisions are made here
		possible_moves = ['up', 'down', 'left', 'right']
		return random.choice(possible_moves)