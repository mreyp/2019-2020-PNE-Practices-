import socket

# SERVER IP, PORT
# Write here the correct parameter for connecting to the
# Teacher's server
PORT = 8080
IP = "212.128.253.128"   # Teacher's server ip


# First, create the socket
# We will always use this parameters: AF_INET (connected to internet) y SOCK_STREAM
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# establish the connection to the Server (IP, PORT)
s.connect((IP, PORT))

#Send data to server. No strings can be send, only bytes
# It necessary to encode the string into bytes
s.send(str.encode("HELLO FROM THE CLIENT!!!"))

