#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

#note the usual http port is 80
PORT_NUMBER = 8080

try:
	#create a web server and specify the handler class for requests
	server = HTTPServer(('', PORT_NUMBER), BaseHTTPRequestHandler)
	print 'Started http server on: ' server.socket.getsockname()
	#wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
