import socket

# SERVER IP, PORT
PORT = 8080
IP = "212.128.253.128"

while True:
    # -- Ask the user for the message
    message = input("Enter the message you want to send:")

    # -- Create the socket
    # We will always use this parameters: AF_INET (connected to internet) y SOCK_STREAM
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # establish the connection to the Server
    s.connect((IP, PORT))

    # Send user message
    msg_sent = str.encode(message)
    s.send(msg_sent)

    # -- Close the socket
    s.close()
