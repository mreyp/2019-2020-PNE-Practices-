import socket
import termcolor

# Configure the Server's IP and PORT
IP = "192.168.1.58"
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
count = 0
while True:

    # -- Wait for a client to connect
    print("Waiting for Clients to connect")
    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listening socket
        ls.close()

        # -- Exit!
        exit()

        # -- Execute this part if there are no errors
    else:
        c = (IP, PORT)
        count += 1
        print(f'CONNECTION {count}. ', end="")
        print("IP, PORT:", c)

        # Step 5: receiving information from the server (recv and decode)
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        print("Received Message: ", end="")
        termcolor.cprint(msg, "green")

        # -- Step 6: Send a response message to the client
        # -- Send a response message to the client
        response = f"ECHO: {msg}"

        # -- The message has to be encoded into bytes
        cs.send(response.encode())
        # -- Close the socket
        cs.close()
