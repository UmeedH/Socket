
import socket               # Import socket module
import sys
from thread import *
s = socket.socket()         
host = socket.gethostname()
port = 5182                # Reserve a port for your service.
name = raw_input("Name:")
s.connect((host, port))
print s.recv(1024)
s.close                     # Close the socket when done
def recieve():
    while True:
        #Receiving from client
        data = s.recv(1024)
        print data
start_new_thread(recieve,())
while 1:
	reply = raw_input()
	s.send(name+' : '+reply)
	if not reply:
		break