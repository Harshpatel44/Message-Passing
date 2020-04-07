__author__ = 'Harsh'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()   #takes machines host name
#host=""                    # any host name can be specified

port=7797
s.connect((host, port))
i=''
while 1:
    message = s.recv(1024).decode()
    if (message == 'exit.'):
        print("user gave you a bye.")
        s.close()
        break
    print('message: ',message)
    a=input("reply: ")
    s.send(a.encode())
    if (a == 'exit.'):
        s.close()
        break