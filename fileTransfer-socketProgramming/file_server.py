from __future__ import print_function
__author__ = 'Harsh'
import socket
import file2

#from hurry.filesize import size
import os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()
host=socket.gethostbyname(host)
print("Host IP Adress:",host)
port=7797
s.bind((host,port))
s.listen(5)
print("Join The Connection...")
while 1:
    conn,addr=s.accept()
    print("Connected With ",str(addr))
    #data=conn.recv(1024).decode()
   # print("server recieved ",repr(data))
    name=input("Enter Filename:")
    conn.send(name.encode())
    #os.getcwd()
    os.chdir("C:\\Users\\Harsh\\Desktop")
    name_size=os.path.getsize(name)
    #name_size=str(name_size)+" "
    #print(name_size)
    f=open(name,'rb')
    os.path.getsize(name)
    conn.send(str(name_size).encode())
    l=f.read(3000000)
    i=0
    packet_size=3000000
    while (l):

       #print(" %s Copied:%.6s  %s "%(i, ((float(packet_size)/name_size)*100) ,size(packet_size)))
        print("Copied:%.6s\r"%( ((float(packet_size)/name_size)*100)),end="")
        packet_size=packet_size+3000000.0
        conn.send(l)
        i=i+1
       # print("sent",repr(l))
        l=f.read(3000000)
    f.close()
    print("\rCopied:100.000")
    print("File Copied Successfully")
    conn.close()