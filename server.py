#!/usr/bin/python3

import socket
import select
import sys

from _thread import *

#Error check command line args

if len(sys.argv) != 3:
    print("Not enough arguments, Example of a corrct call:\n")
    print("./server <IP ADDR> <PORT NUM>")
    sys.exit()

#Command line args satisfied
print("Starting Server...\n")

IP_ADDR = str(sys.argv[1])
print("IP Address: " + IP_ADDR)


PORT = str(sys.argv[2])
print("Port: " + PORT)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(IP_ADDR, PORT)

