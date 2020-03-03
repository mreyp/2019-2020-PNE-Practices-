from Client0 import Client
import termcolor

IP = "192.168.1.58"
PORT = 8080

c = Client(IP, PORT)

for i in range(5):
    print('To Server: ', end="")
    termcolor.cprint(f"Message {i}", 'blue')
    print('From Server: ', end="")
    termcolor.cprint(c.debug_talk(f"ECHO: Message {i}"))
