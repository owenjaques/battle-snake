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
				'url': 'https://localhost:' + port,
				'process': Process(target=start_server, args=(port,))
			}
		)
		snakes[i]['process'].start()

def kill_snakes(num_snakes, snakes):
	for i in range(num_snakes):
		kill(snakes[i]['process'].pid, SIGTERM)
		snakes[i]['process'].join(3)

if __name__ == '__main__':
	snakes = []
	num_snakes = 2

	start_snakes(num_snakes, snakes)
	sleep(5)
	kill_snakes(num_snakes, snakes)