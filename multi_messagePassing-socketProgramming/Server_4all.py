__author__ = 'Builder'
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=socket.gethostname()  #socket.gethostbyname("LAPTOP-FAG651NP")
print(host)
port=2003
s.bind((host,port))
conn=input("Enter no of connections:")
s.listen(int(conn))

n=["n1","n2","n3"]           #creating list for diffrent connections name
a=["a1","a2","a3"]              #specify diffent addressses
for i in range(0,int(conn)):
    print("Join Connection:%s,%s"%(n[i],a[i]))
    (n[i],a[i])=s.accept()
    print(a[i])
for i in range(0,2):
    print("loopno %s:",i)
    for j in range(0,int(conn)):
        a=input("enter for (%s):".format(j))
        n[j].send(a.encode())
#a=input("Write something for all:")
#.send(a.encode())
s.close()



