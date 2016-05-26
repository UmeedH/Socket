'''
    Simple socket server using threads
'''
 
import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 9391 # Arbitrary non-privileged port
arr2=[]
arr =[] # this is to keep track of users
var=0
i = 0
arr1=[]
n=[]
k=0
p=0
j=0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server.') #send only takes string
    for k in range(i-1):
        conn.sendall("you are connected with " + (arr1[k]) + "\n")
    for j in range(i-1): 
        arr[j].sendall(str(newv))
    conn.sendall("Which address do you want to connect to?\n")
    while True:
        address = conn.recv(1024)
        three.append(address)
        three.append(conn)
        data=conn.recv(1024)
        conn.sendall('Type something and hit enter\n')
     
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        data=conn.recv(1024)
        if conn == [0]:
            conn = arr2[1]
            conn.sendall(data)
            conn = arr2[0]
        elif conn == arr2[1]:
            conn = arr2[0]
            conn.sendall(data)
            conn = arr2[1]
        if not data: 
            break
     
    #came out of loop
    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    arr.append(conn)
    two.append(conn,addr)
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
    arr1.append(str(addr[1]))
    n.append((addr[1]))
    var=addr[1]
    
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
    
    i += 1
 
s.close()
