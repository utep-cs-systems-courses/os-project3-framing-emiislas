#! /usr/bin/env python3


import socket, sys, re, os, time
sys.path.append("../lib")       # for params
import params
from archiver import *
import logging, threading, time

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )



progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''       # Symbolic name meaning all available interfaces

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)              # allow only one outstanding request
# s is a factory for connected sockets

def exThread(Cnum,msg):
	print(logging.info("Client number%s:", Cnum, "Starting: "))
        
	time.sleep(2)
	for i in range(len(msg)-1):
            readByteArray(i, msg)
	

threadList = list()
index = 0
while True:
    print("Waiting for connection...")
    conn, addr = s.accept() # wait until incoming connection request (and accept it)
    index+=1
    if os.fork() == 0:      # child becomes server
        print('Connected by', addr)
        msg = conn.recv(1024)
        print("Message Recieved", msg)
        time.sleep(0.25);       # delay 1/4s
        print("Decoding..")
        
        x = threading.Thread(target=exThread, args=(index,msg))
        threadList.append(x)
        
        x.start()
        
        print("Sending.. ")
        conn.send(b'0')
        x.join
        conn.shutdown(socket.SHUT_WR)


