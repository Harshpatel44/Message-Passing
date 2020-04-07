__author__ = 'Builder'
__author__ = 'Builder'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
#host="192.168.43.4"
print(host)
port=2003
s.connect((host,port))
i=0
while i<6:
    sa=s.recv(1024).decode()
    print(sa)
    i=i+1
#while((sa)!="exit"):
 #   sa=s.recv(1024).decode()
  #  print(sa)
   # a=raw_input("Reply:")
    #s.send(a.encode())
