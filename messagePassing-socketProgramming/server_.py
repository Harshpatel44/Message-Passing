from socket import *
import _thread
s=socket(AF_INET,SOCK_STREAM)
host=gethostname()
port=7798
s.bind((host,port))
s.listen(10)
def clientthread(conn):
    conn.send("Welcome to Python".encode())
    while 1:
        data=conn.recv(1024).decode()
        print(str(addr)+" "+data)
        reply="ok.."+str(data)
        if not data:
            break
        conn.sendall(reply.encode())
    conn.close()


while 1:

    conn,addr=s.accept()
    print("Connected with %s"%str(addr))
    _thread.start_new_thread(clientthread,(conn,))

s.close()