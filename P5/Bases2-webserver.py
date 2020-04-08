import http.server
import socketserver
import termcolor
from pathlib import Path


def read_file(filename):
    # -- Open and read the file
    file_contents = Path(filename).read_text().split("\n")[1:]
    body = "".join(file_contents)
    return body


FOLDER = "../P5/"

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
        termcolor.cprint(self.requestline, 'green')

        if self.path == "/" or self.path == "/index.html":
            file = "index.html"

        else:
            file = self.path

        try:
            contents = read_file(FOLDER + file)

            # status code
            status = 200

        except FileNotFoundError:
            contents = read_file(FOLDER + "error.html")

            # status code no found
            status = 404

        # Generating the response message
        self.send_response(status)

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
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
        print("Stopped by the user")
        httpd.server_close()
