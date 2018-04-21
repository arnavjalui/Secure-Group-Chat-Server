# Python program to implement client side of chat room.
import socket
import select
import sys
from encryption import encryption
from decryption import decryption
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print "Correct usage: script, IP address, port number"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
 
while True:
 
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
 
    """ There are two possible input situations. Either the
    user wants to give  manual input to send to other people,
    or the server is sending a message  to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input. So for example, if the server wants
    to send a message, then the if condition will hold true
    below.If the user wants to send a message, the else
    condition will evaluate as true"""
    read_sockets, write_socket, error_socket = select.select(sockets_list,[],[])
 
    for socks in read_sockets:
        if socks == server:
            msg = socks.recv(2048)
            index = msg.find(" ")
            # print index
            sender = msg[:(index+1)]
            msg = msg[(index+1):]
            # message = str(msg)
            # print sender
            print sender,
            msg = decryption(msg)
            print msg
        else:
            message = sys.stdin.readline()
            encMsg = encryption(message)
            print ""
            server.send(encMsg)
            sys.stdout.flush()
server.close()