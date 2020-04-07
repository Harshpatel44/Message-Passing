from socket import *
s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=7798
s.connect((host,port))
data=s.recv(1024).decode()
print(data)
while 1:
    a=input()
    s.send(a.encode())
    data=s.recv(1024).decode()
    print(data)

