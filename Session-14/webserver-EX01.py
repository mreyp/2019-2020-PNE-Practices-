import http.server
import socketserver
import termcolor

# Define the Server's port
PORT = 8080

# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'blue')

        #analize req line
        req_line = self.requestline.split(" ")

        #path
        path = req_line[1]
        path = path[1:]

        #message to client
        contents = ""

        #status
        status = 0

        #content type header
        content_type = 'text/plain'


        #2 options:
        if path == "":
            termcolor.cprint("Main page has been requested", 'green')

            # Message to client
            contents = "Welcome to y server"

            # status code
            status = 200

        else:
            # -- Resource NOT FOUND
            termcolor.cprint("ERROR 404, not found", 'red')

            # Message to  client
            contents = "Resource not available"

            # status code no found
            status = 404

            # Generating the response message
            self.send_response(status)

            # Define the content-type header:
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Content-Length', len(contents.encode()))

            # The header is finished
            self.end_headers()

            # Send the response message
            self.wfile.write(contents.encode())

            return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()