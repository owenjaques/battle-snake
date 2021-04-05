import subprocess as sp
from multiprocessing import Process
from snake.server import start_server
from time import sleep
from os import kill
from signal import SIGTERM

def start_snakes(num_snakes, snakes):
	# creates a seperate process for every snake created
	for i in range(num_snakes):
		port = '808' + str(i)
		snakes.append(
			{
				'url': 'http://localhost:' + port,
				'process': Process(target=start_server, args=(port,))
			}
		)
		snakes[i]['process'].start()

def kill_snakes(num_snakes, snakes):
	# kills snakes running on seperate processes
	for i in range(num_snakes):
		kill(snakes[i]['process'].pid, SIGTERM)
		snakes[i]['process'].join(3)

def start_game(num_snakes, snakes):
	# creates a game with snakes running on seperate processes
	cmd = './battlesnake play -W 11 -H 11'
	for i in range(num_snakes):
		cmd = f"{cmd} --name snake{str(i)} --url {snakes[i]['url']}"
		
	game = sp.run(cmd, shell=True, capture_output=True, cwd='training/engine')

if __name__ == '__main__':
	snakes = []
	num_snakes = 3

	start_snakes(num_snakes, snakes)

	for i in range(5, 0, -1):
		sleep(1)
		print(f'Starting game in: {str(i)}')

	start_game(num_snakes, snakes)

	sleep(10)

	kill_snakes(num_snakes, snakes)