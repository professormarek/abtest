#!/usr/bin/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

#note the usual http port is 80
PORT_NUMBER = 8080

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
            <button type='submit' name = 'my_button' value= 'This is a value I chose for this button' >
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
            <button type='submit' name = 'my_button' value= 'This is a value I chose for this button' >
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
		#wfile is an object where we can write the response to the broswer
		self.wfile.write(HTML)

	#declare a method to handle http POST requests
	def do_POST(self):
		print "LOG: We received a POST request!"
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
