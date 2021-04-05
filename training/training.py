import subprocess as sp
from multiprocessing import Process
from snake.server import start_server
from time import sleep
from os import kill
from signal import SIGTERM

def start_snake(port):
	process = Process(target=start_server, args=(port,))
	process.start()
	return process

def kill_snake(process):
	kill(process.pid, SIGTERM)
	process.join(3)

def start_game(num_snakes, snake_url):
	# creates a game with 'num_snakes' amount of the same snake
	cmd = './battlesnake play -W 11 -H 11'
	for i in range(num_snakes):
		cmd = f"{cmd} --name snake{str(i)} --url {snake_url}"
		
	game = sp.run(cmd, shell=True, capture_output=True, cwd='training/engine')

if __name__ == '__main__':
	num_snakes = 2
	port = '8080'
	url = 'http://0.0.0.0:' + port
	
	snake = start_snake(port)
	for i in range(5, 0, -1):
		sleep(1)
		print(f'Starting game in: {str(i)}')

	start_game(num_snakes, url)
	sleep(10)
	kill_snake(snake)