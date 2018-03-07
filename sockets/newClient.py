i#!/usr/bin/python 

import socket 

s = socket.socket() #create a socket object
port = 12345 #Reserve a port for your service

s.connect(('',port))
print s.recv(1024)
s.close
