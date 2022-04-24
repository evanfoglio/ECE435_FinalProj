#!/usr/bin/python3

import socket
import select
import sys
import os
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

connList = []


def client_multithread(conn, addr):
    global connList
    conn.send("You have entered the Matrix".encode())
    while True:
        try:
            #see if theres a message
            msg = conn.recv(2048)
            #if there is a message,
            if msg :
                print(str(msg.decode()))
                broadcast((str(addr[0]) + " said: " + str(msg.decode())), conn)
            else:
                if conn in connList:
                    connList.remove(client)
        # if theres no message, then just check again
        except:
            continue

def broadcast(msg, connection):
    global connList
    for client in connList:
        if client != connection:
            try:
                client.send(msg.encode())
            except:
                client.close()
                if connection in connList:
                    connList.remove(client)

print("SERVER INIT")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((IP_ADDR, PORT))


server.listen(100)
print("SERVER LISTENING")


while True:
    
    conn, addr = server.accept()
    print("ACEPTED")
    connList.append(conn)
    print(addr[0] + " connected")
    
    start_new_thread(client_multithread, (conn, addr))


conn.close()
server.close()
