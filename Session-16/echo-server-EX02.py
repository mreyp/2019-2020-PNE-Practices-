import http.server
import socketserver
import termcolor
from pathlib import Path

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


        if self.path == "/":
            contents = Path('form-EX02.html').read_text()
            code = 200

        elif "/echo" == self.path[0:self.path.find("?")]:  # /echo length
            chk = self.path[self.path.find("chk") + 4:] #chk= y a partir de ahi ya lo cojo

            if "chk" in self.path and "on" == chk:
                msg = self.path[self.path.find("=")+1:]  #http://127.0.0.1:8080/echo?msg=hello
                msg_converted = msg.upper()

            else:
                msg = self.path[self.path.find("msg") + 4:] #chk= y a partir de ahi ya lo cojo
                msg_converted = msg

            contents = f"""
                <!DOCTYPE html>
                       <html lang="en" dir="ltr">
                         <head>
                           <meta charset="utf-8">
                           <title>RESULT</title>
                         </head>
                         <body>
                           <h1>Received message:</h1>
                           <p>{msg}</p>
                           <a href="http://127.0.0.1:8080/">Main Page </a>
                         </body>
                       </html>
                       """
            code = 200  # -- Status line: OK!

        else:
            contents = Path("Error.html").read_text()
            code = 404  # -- Status line: ERROR NOT FOUND


        # Generating the response message
        self.send_response(code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

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