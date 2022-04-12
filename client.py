#!/usr/bin/python3

import socket
import select
import sys


print("Starting Client...\n")

if len(sys.argv) != 3:
    print("Not enough arguments, Example of a correct call:\n")
    print("./client.py <IP ADDR> <PORT NUM>")
    sys.exit();i

IP_ADDR = str(sys.argv[1])
print("IP Address: " + IP_ADDR)


PORT = int(sys.argv[2])
print("Port: " + str(PORT))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect((IP_ADDR, PORT))

message = "Hi"

server.send(message.encode())
server.close()




