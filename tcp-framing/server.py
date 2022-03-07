import socket, sys, re, os, time
import params

switchesVarDefaults = (
    (('-1', '--listenPort'), 'listenPort', 50001),
    (('-?', '--usage'), "usage", False),
    )

progname = "ProjectServer"
paramMap = params.parseParams(switchesVarDefaults)

listenPort = paramMap['listenPort']
listenAddr = ''

if paramMap['usage']:
    params.usage()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((listenAddr, listenPort))
s.listen(1)

while True:
    conn, addr = s.accept()
    if os.fork() == 0:
        print('Connected by', addr)
        conn.send(b"Will send file to archive")#send recieve message
        time.sleep(0.25)
        #conn.send()#send other message
        conn.shutdown(socket.SHUT_WR)

