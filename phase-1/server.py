from http.server import HTTPServer, BaseHTTPRequestHandler
# first line fetches the HTTPServer and BaseHTTPRequestHandler from the http.server dictionary

def get_greeting():
    try:
        with open('content.txt', 'r', encoding="utf-8") as f:
            read_data =  f.read()
            return read_data
    except FileNotFoundError:
        return "Greeting unavailable"

class MyHandler(BaseHTTPRequestHandler): #Creates a class called 
    def do_GET(self): # defines a function named do_GET
        '''self refers to the particular instance handling that request'''
        if self.path == "/":
            self.send_response(200) #sends the status code back, 200 means OK
            self.send_header("Content-Type", "text/plain") #Tells the client what type of content is coming, in this case, it's a plain text
            self.end_headers()#This line ends the headers and everything after it is a body.
            self.wfile.write(get_greeting().encode())
        elif self.path == "/about":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"This server was built by Arthur Mulunda")
        else:
            self.send_response(404)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Not Found")

server = HTTPServer(("localhost", 8000), MyHandler) #Creates the server, tells it to listen on localhost at port 8000, and to use MyHandler to handle incoming requests
print("Server running on port 8000")# It should print Server running on port 8000 after starting the server, that means after running the program
server.serve_forever() #Starts the server and it keeps running until it is stopped manually.