__author__ = 'Harsh'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
host=socket.gethostbyname(host)
print(host)