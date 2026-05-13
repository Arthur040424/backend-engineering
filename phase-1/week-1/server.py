from http.server import HTTPServer, BaseHTTPRequestHandler
# first line fetches the HTTPServer and BaseHTTPRequestHandler from the http.server dictionary

class MyHandler(BaseHTTPRequestHandler): #Creates a class called MyHandler
    def do_GET(self): # defines a function named do_GET
        '''self refers to the particular instance handling that request'''
        self.send_response(200) #sends the status code back, 200 means OK
        self.send_header("Content-Type", "text/plain") #Tells the client what type of content is coming, in this case, it's a plain text
        self.end_headers()#This line ends the headers and everything after it is a body.
        self.wfile.write(b"Hello from Arthur's server") #writes the response body. The b prefix means bytes. networks speak bytes, not strings.

server = HTTPServer(("localhost", 8000), MyHandler) #Creates the server, tells it to listen on localhost at port 8000, and to use MyHandler to handle incoming requests
print("Server running on port 8000")# It should print Server running on port 8000 after starting the server, that means after running the program
server.serve_forever() #Starts the server and it keeps running until it is stopped manually.

""".
I know nothing about python, I thought you would be teaching me python, but I just wrote a code that I actually do not understand or know what it does, tho I am aware that what I have written is a http server"""