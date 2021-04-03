import os

import cherrypy
from snake import Snake

# TODO: make this support multiple games at once
# TODO: once this is working semi well and the snake is made public, switch to Heroku and find a way to keep
#		the app from sleeping (Heroku free apps sleep after 30 minutes of inactivity)

class Battlesnake(object):
	def __init__(self):
		self.snake = Snake()

	@cherrypy.expose
	@cherrypy.tools.json_out()
	def index(self):
		return {
			'apiversion': '1',
			'author': 'owenj',
			'color': '#906df9',
			'head': 'caffeine',
			'tail': 'round-bum'
		}

	@cherrypy.expose
	@cherrypy.tools.json_in()
	def start(self):
		data = cherrypy.request.json
		self.snake.start(data)

		print('START')
		return 'ok'

	@cherrypy.expose
	@cherrypy.tools.json_in()
	@cherrypy.tools.json_out()
	def move(self):
		data = cherrypy.request.json
		move = self.snake.move(data)

		print('MOVE:', move)
		return {'move': move}

	@cherrypy.expose
	@cherrypy.tools.json_in()
	def end(self):
		data = cherrypy.request.json
		self.snake.end(data)

		print('END')
		return 'ok'

if __name__ == '__main__':
	server = Battlesnake()
	cherrypy.config.update({'server.socket_host': '0.0.0.0'})
	cherrypy.config.update(
		{'server.socket_port': int(os.environ.get('PORT', '8080')),}
	)
	print('Starting Battlesnake Server...')
	cherrypy.quickstart(server)
