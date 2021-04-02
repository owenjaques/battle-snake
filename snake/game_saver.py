import json

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