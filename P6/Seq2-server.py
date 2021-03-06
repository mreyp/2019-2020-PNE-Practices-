import http.server
import socketserver
import termcolor
from pathlib import Path
from Seq1 import Seq

# Define the Server's port
PORT = 8080


def html_response(title="", body="", color='white'):
    default_body = f"""
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>{title}</title>
  </head>
  <body style="background-color: {color};">{body} 
    </body>
    <body>
    <a href="http://127.0.0.1:8080/">Main Page </a>
  </body>
</html>
"""
    return default_body


def argument_command(request_line):
    argument = request_line[request_line.find("=") + 1:]    # Devuelve lo q hay después del =
    return argument


#  Preventing the error: "Port already in use"
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
            file = "form-4.html"
            contents = Path(file).read_text()
            error = 200

        elif "/ping" in self.path:
            html = "<h1>PING OK!</h1><p>The SEQ2 server is running...</p>"
            contents = html_response("PING", html, 'orange')  # En title va PING y en body el resto
            error = 200

        elif "/get" in self.path:

            seq_list = ["TGTGAACATTCTGCACAGGTCTCTGGCTGCGCCTGGGCGGGTTTCTT",
                        "CAGGAGGGGACTGTCTGTGTTCTCCCTCCCTCCGAGCTCCAGCCTTC",
                        "CTCCCAGCTCCCTGGAGTCTCTCACGTAGAATGTCCTCTCCACCCC",
                        "GAACTCCTGCAGGTTCTGCAGGCCACGGCTGGCCCCCCTCGAAAGT",
                        "CTGCAGGGGGACGCTTGAAAGTTGCTGGAGGAGCCGGGGGGAA"]

            sequence_number = int(argument_command(self.path))
            sequence = seq_list[sequence_number]

            html = "<h1>Sequence number " + str(sequence_number) + "</h1> <p>" + sequence + "</p>"
            contents = html_response("GET", html, 'pink')

            error = 200  # -- Status line: OK!

        elif "/gene" in self.path:

            gene = argument_command(self.path)

            s = Seq()
            s.read_fasta("../Session-04/" + gene + ".txt")

            html = "<h1>Gene Sequence: " + gene + '</h1> <textarea readonly rows = "20" cols = "80">' + str(
                s) + '</textarea>'
            contents = html_response("GENE", html, 'yellow')

            error = 200

        elif "/operation" in self.path:
            requests = self.path.split("&")
            sequence = argument_command(requests[0])
            op = argument_command(requests[1])
            seq = Seq(sequence)
            bases = ['A', 'C', 'T', 'G']
            for b in sequence:
                if b in bases:
                    if "info" == op:
                        count_bases_string = ""
                        for base, count in seq.count().items():
                            s_base = str(base) + ": " + str(count) + " (" + str(
                                round(count / seq.len() * 100, 2)) + "%)" + "<br>"
                            count_bases_string += s_base

                        response_info = ("Sequence: " + str(seq) + " <br>" +
                                         "Total length: " + str(seq.len()) + "<br>" +
                                         count_bases_string)

                        html_operation = "<h1>Operation:</h1><p>Information</p>"
                        html_result = "<h1>Result:</h1>" + "<p>" + response_info + "</p>"
                        color = 'lightblue'

                    elif "comp" == op:
                        response_comp = seq.complement() + "\n"

                        html_operation = "<h1>Operation:</h1><p>Complementary sequence</p>"
                        html_result = "<h1>Result:</h1>" + "<p>" + response_comp + "</p>"
                        color = 'lightgrey'

                    elif "rev" == op:
                        response_rev = seq.reverse() + "\n"

                        html_operation = "<h1>Operation:</h1><p>Reverse sequence</p>"
                        html_result = "<h1>Result:</h1>" + "<p>" + response_rev + "</p>"
                        color = 'lightgreen'

                    html_sequence = "<h1>Sequence:</h1>" + "<p>" + sequence + "</p>"
                    html = html_sequence + html_operation + html_result

                    contents = html_response("OPERATION", html, color)
                    error = 200
                else:
                    file = "Error-1.html"
                    contents = Path(file).read_text()
                    error = 404

        else:
            file = "Error-1.html"
            contents = Path(file).read_text()
            error = 404  # -- Status line: ERROR NOT FOUND

        self.send_response(error)
        # Generating the response message
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
    # -- client, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()




