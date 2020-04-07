from __future__ import print_function
__author__ = 'Harsh'
import socket
#from hurry.filesize import size
from file2 import *
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=input("Enter Host:")
#host="192.168.43.4"
#host=socket.gethostname()
port=7797
s.connect((host,port))
new=s.recv(1024).decode()
name_size=s.recv(1024).decode()
print(name_size)
packet_size=3000000
#new2='2'+new
#s.send(("Hello Server").encode())
new=moving(new)
i=0
#print(os.getcwd())
with open(new,'wb') as f:
    #print("file Opened")
    while True:
        data=s.recv(3000000)
        if not data:
            break
        #print("%s Recieved:%.6s  %s "%(i, ((float(packet_size)/float(name_size))*100) ,size(packet_size)))
        print("Recieved:%.6s\r"%( ((float(packet_size)/float(name_size))*100)),end="")
        #print("Recieved: %.6s %s" %( ((float(packet_size)/name_size)*100) ,size(packet_size) ) )
        packet_size=packet_size+3000000
        #print("data=",data)
        i=i+1

        f.write(data)
f.close()
print("Recieved: 100.000")
print("File Recieved Successfully")
s.close()
print("Connection Closed")