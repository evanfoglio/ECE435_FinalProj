#!/usr/bin/python3

import socket
import select
import sys
from _thread import *


#intended to be used in a sepaerate thread
# than the sending of messages
def msg_recv (conn, i):
    while True:
        sockets_list = [sys.stdin, server]
        read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
        for socks in read_sockets:
            if socks == server:
                #recive message
                message = socks.recv(2048)
                #decode and print
                print (str(message.decode()))




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


start_new_thread(msg_recv, (server, 5))
while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
    #get user input
    message = input()
    #encode msg and send to server
    server.send(message.encode())

server.close()




