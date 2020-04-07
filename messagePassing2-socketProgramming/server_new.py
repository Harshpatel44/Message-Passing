__author__ = 'Harsh'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
port=7797
s.bind((host,port))
s.listen(5)
conn,addr=s.accept()
print("connected to %s"%(str(addr)))
while 1:
    message=input("message:")
    conn.send(message.encode())
    if (message == 'exit.'):
        s.close()
        break
    i=conn.recv(1024).decode()
    if(i=='exit.'):
        print("user gave you a bye.")
        s.close()
        break
    print('reply:',i)
s.close()

