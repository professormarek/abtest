#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import random
import cgi

#note the usual http port is 80
PORT_NUMBER = 8080

#a constant that defines how often the "B" version of the site is shown
TEST_THRESHOLD = 0.2 #show the "B" version 20% of the time

#store the html we're going to display as a string (it's simple text after all)
HTMLA =  """
<!DOCTYPE html>
<html>
    <head>
        <title>My Test Site</title>
    </head>
    <body>
        We love python..just kidding
        <form action="/" method="post" >
            <button type='submit' name = 'my_button' value= 'A' >
            <h2>Spectacular Professor</h2>
            <img src="https://media.licdn.com/mpr/mpr/shrinknp_400_400/AAEAAQAAAAAAAAK4AAAAJDMyZjI3Mjg4LTRhNTAtNDU2OS1hMWQ1LTkzZWFiOGU5ZjE1Ng.jpg" alt="Mountain View" style="width:304px;height:228px;">   
                
            </button>
        </form>
    </body>
</html>
"""

HTMLB="""
<!DOCTYPE html>
<html>
    <head>
        <title>Happy International Women's Day !!!</title>
    </head>
    <body>
        Happy International Women's Day !!!
       <p> <b>You are so hot Prof. Laskowski!</b></p>
        Group Members:Saishang Jiang, Mingyi Xu, Yansong Chen, Yingjun Feng
        <form action="/" method="post" >
            <button type='submit' name = 'my_button' value= 'B' >
                OK
            </button>
        </form>
    </body>
</html>

"""

THANKS = """
<!DOCTYPE html>
<html>
    <head>
        <title>My Test Site</title>
    </head>
    <body>
        Thanks for your bitcoins mwa ha ha
    </body>
</html>"""
#in order to respond to http requests we need to create a custom handler class
class myHandler(BaseHTTPRequestHandler):
	#declare a method to handle GET requests so that we can serve a page!
	def do_GET(self):
		print "LOG: We recieved a GET request!"
		#compose a response and send it back to the browser
		self.send_response(200)
		#send http header
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		#also send some html for the browser to render

		#to do an A/B test let's send the browser either version A or B randomly
		if random.random() < TEST_THRESHOLD:
			HTML = HTMLB #use the B version
			print "LOG: served version B"
		else:
			HTML = HTMLA #use the A version
			print "LOG: served version A"

		#wfile is an object where we can write the response to the broswer
		self.wfile.write(HTML)

	#declare a method to handle http POST requests
	def do_POST(self):
		print "LOG: We received a POST request!"

		#process the data submitted by the browser (which button was clicked)
		#(this code is a little ugly)
		form = cgi.FieldStorage(
			fp=self.rfile,
			headers=self.headers,
			environ={'REQUEST_METHOD':'POST',
			'CONTENT_TYPE':self.headers['Content-Type'],
			})
		#iterate through the data returned by the form
		for field in form.keys():
			field_item = form[field]
			#print field_item
			if field_item.name == 'my_button':
				if field_item.value == 'A':
					print "LOG: version A was clicked!"
				else:
					print "LOG: version B was clicked!"

		self.send_response(200)
		#send http header
		self.send_header('Content-type', 'text/html')
		self.end_headers()
		self.wfile.write(THANKS)

try:
	#create a web server and specify the handler class for requests
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started http server on: ', server.socket.getsockname()
	#wait forever for incoming http requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()
