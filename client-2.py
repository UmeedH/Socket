import socket               # Import socket module
import sys
import os
from thread import *
 

Sock = socket.socket()         
host = socket.gethostname()
port = 9000                # Reserve a port for your service.
 
Sock.connect((host, port))
name = raw_input("Enter Your Name : ")
name=name
Sock.send(name)
print Sock.recv(1024)
def recv():
    while True:  
        #Receiving from client        
	data = Sock.recv(1024)
        print data
start_new_thread(recv,())
while 1:		
	m= raw_input()
	if m=='show':
            os.system('clear')
            Sock.send(' list')		
	elif m=='exit':
	    Sock.send(' exit')			
	else:
            n,rep = m.split(' ',1)		
	    Sock.send(n+' '+name+' : '+rep)
	if not rep:
	    break

	
