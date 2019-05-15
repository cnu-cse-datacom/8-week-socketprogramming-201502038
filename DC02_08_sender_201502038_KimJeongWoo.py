import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host ="127.0.0.1" 
port = 9000
buf = 1024

addr = (host,port) 
filename = input("input filename:");

size = str(os.path.getsize(filename)).encode()
f=open(filename,"rb")
data=f.read(buf)

s.sendto(size,(addr))
number = 0
while(data):
    number += 1
    proceed = ((1024*number)/int(size))*100
    if(s.sendto(data,addr)):
        if proceed>100:
            print(print("current_size / total_size=",100))
        else:
            print("current_size / total_size=",proceed)
        data = f.read(buf) 

s.close() 
f.close()
print("file_send_end")
