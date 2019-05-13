import socket
import os
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 

host ="192.168.31.193" 
port = 3500
buf = 1024

addr = (host,port) 
filename = input("input filename:");

f=open(filename, "rb") 
data=f.read(buf) 

while(data):
    if(s.sendto(data,addr)):
        print("sending ...")
        data = f.read(buf) 

s.close() 
f.close()
print("file_send_end")
