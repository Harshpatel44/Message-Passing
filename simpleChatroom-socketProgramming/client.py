__author__ = 'Harsh'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client=socket.gethostname()   #takes machines host name
print("ClientName:",client)
client_id=socket.gethostbyname(client)
print("ClientID",client_id)

host=input("Enter Server IP:")
port=7797
s.connect((host, port))
# i=''
while 1:
    message = s.recv(1024).decode()

    print('message: ',message)
    a=input("reply: ")
    s.send(a.encode())
    # if (a == 'exit.'):
    #     #     s.close()
    #     #     break