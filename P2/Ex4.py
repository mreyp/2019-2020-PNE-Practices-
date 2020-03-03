from Client0 import Client

PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

# -- Parameters of the server to talk to
IP = "10.3.33.54"
PORT = 8086

# -- Create a client object
c = Client(IP, PORT)

c.debug_talk("Message 1---", 'green')
c.debug_talk("Message 2: Testing !!!", 'green')
