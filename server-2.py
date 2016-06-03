'''
    Simple socket server using threads
'''
  
import socket
import sys
from thread import *
  
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 9000 # Arbitrary non-privileged port

check=[]
check.append(0)
add = []
cl=[]
cl.append(0)
name=[]
Sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
  
#Bind socket to local host and port
try:
    Sock.bind((HOST, PORT))
except socket.error as m:
    print 'Bind failed. Error Code : ' + str(m[0]) + ' Message ' + m[1]
    sys.exit()
      
print 'Socket bind complete'
  
#Start listening on socket
Sock.listen(10)
print 'Socket now listening'
  
#Function for handling connections. This will be used to create threads

def clientthread(conn):
    #Sending message to connected client
    nconn=conn.recv(1024)
    name.append(nconn)
    for i in range(len(name)-1):
	add[i].sendall(nconn+' is Available for chat:')
    check[0] = 0	
    conn.send('Welcome to the server. Available clients are : \n') #send only takes string
    for i in range(len(name)):
	conn.send(name[i]+'\n')
    #infinite loop so that function do not terminate and thread do not end.
    while True:  
        #Receiving from client
	data = conn.recv(1024)
	reciever,rep=data.split(' ',1)
	if rep== "show":	
		conn.send('Available Clients are  : \n')		
		for i in range(len(name)):
			conn.sendall(name[i])
			conn.sendall('\n')
		
	elif rep == 'exit':
		for x in range(len(add)):
			if add[x] == conn:
				nconn=name.pop(x)
				add.pop(x)
				for s in range(len(add)):
					add[s].sendall(nconn+' left the chat\n')			
			break
	else:
		flag=0		
		for x in range(len(name)):
			if reciever == name[x]:		
				add[x].sendall(rep)
				flag=1
		if flag==0:
			conn.sendall('User is not Available : Typer list to check Users \n')
		
	if not data: 
		conn.sendall('Your client left the chat \n To see list : type :: list ')            
		break
	#came out of loop
    conn.close()
  
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = Sock.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    add.append(conn)
    start_new_thread(clientthread ,(conn,))
 	 
Sock.close()
