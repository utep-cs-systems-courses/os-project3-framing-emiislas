import socket, sys, re, os, time
import params
from archiver import *
import logging, threading, time

switchesVarDefaults = (
    (('-1', '--listenPort'), 'listenPort', 50001),
    (('-?', '--usage'), "usage", False),
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)

def threads(Cnum):
	logging.info("Client number:", Cnum, "Starting: ")
	time.sleep(5)
	#for i in range(len(msg)):
         #   readByteArray(i, msg)
    
threadList = list()
index = 1 
print("Waiting for connection...")
conn, addr = s.accept() #wait to accept connection
print('Connected by: ', addr)
while 1:
   
    if os.fork() == 0: #child is server
       
        msg = conn.recv(1024)
        print("Recieved Code: ", msg)
	  
        
        time.sleep(0.25)

        print("Decoding...")
	  
        #x = threading.Thread(target=threads, args=(index,))
        #threadList.append(x)
        #x.start()
         	
        #for i in range(len(msg)):
        readByteArray(0, msg)
		
        #test = 0
        #test = test.to_bytes(2, 'big')
        #conn.send(test)	
        conn.shutdown(socket.SHUT_WR)
        s.close()
        
    



#add multiple clients with threading, same filename issue
#recieve a text file in form of byte array 
#save file or print contents 
