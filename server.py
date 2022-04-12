#!/usr/bin/python3

import socket
import select
import sys

from _thread import *

#Error check command line args

if len(sys.argv) != 3:
    print("Not enough arguments, Example of a correct call:\n")
    print("./server.py <IP ADDR> <PORT NUM>")
    sys.exit()

#Command line args satisfied
print("Starting Server...\n")

IP_ADDR = str(sys.argv[1])
print("IP Address: " + IP_ADDR)


PORT = int(sys.argv[2])
print("Port: " + str(PORT))


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((IP_ADDR, PORT))


server.listen(100)

conn, addr = server.accept()
 
# prints the address of the user that just connected
print (addr[0] + " connected")

while True:
    try:
        message = conn.recv(2048)
        if message:
            print(addr[0] + "said " + message.decode())
            conn.close()
            server.close()
            sys.exit()
    except:
        continue






conn.close()
server.close()
