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
print("Attempting to connect to specified server...")
server.connect((IP_ADDR, PORT))
print("Connected")
while True:
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
        else:
            message = sys.stdin.readline()
            server.send(message.encode())
server.close()




