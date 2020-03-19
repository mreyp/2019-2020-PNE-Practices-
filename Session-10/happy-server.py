import socket

# Configure the Server's IP and PORT
IP = "10.3.35.145"
PORT = 8080

# -- Step 1: create the socket
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Optional: for avoiding the problem of not available port
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()

print('The server is configured!')

while True:

    # -- Wait for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_op_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

        # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")

        # Step 5: receiving information from the server (recv and decode)
        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print(f"Received Message: {msg}")

        # -- Step 6: Send a response message to the client
        response = "HELLO. I am the Happy Server :-)\n"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        # -- Close the socket
        cs.close()
