__author__ = 'Harsh'

"""
This is a simple chat-room where all the clients will connect with the server and server broadcasts the message to others and 
can even message directly to the sender.
"""

import socket
import _thread
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
host_id=socket.gethostbyname(host)
print("Server_ip:",host_id)
port=7797
s.bind((host,port))
s.listen(5)

clients=[]

def MainFunction(conn,addr):
    conn.send("Welcome to chatroom".encode())
    while True:
        message=conn.recv(1024).decode()
        print(message)
        for i in clients:
            if(i!=conn):
                i.send("broadcast message"+str(message.encode()))
            else:
                i.send("direct message"+str(message.encode()))


while 1:
    conn, addr = s.accept()
    clients.append(conn)
    #conn.send(("hi").encode())
    print(str(addr[0])+" Connected")
    _thread.start_new_thread(MainFunction,(conn,addr))

