import socket
import termcolor

class Client:

    def __init__(self, ip, port):
        self.ip= ip
        self.port = int(port)
        return

    def ping(self):
        print('OK!')

    def __str__(self):
        return "Connection to SERVER at "+ self.ip+ ", PORT: "+ str(self.port)

    def talk(self, msg):

        # -- Create the socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # establish the connection to the Server (IP, PORT)
        s.connect((self.ip, self.port))

        # Send data.
        s.send(str.encode(msg))

    def debug_talk(self, msg):
        message = str(msg)
        response = self.talk(msg)

        print("To sever: ", end="")
        termcolor.cprint(message, "green")

        print("From sever: ", end="")
        termcolor.cprint(message, "blue")


