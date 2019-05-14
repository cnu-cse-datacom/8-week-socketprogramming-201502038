import socket
import time

host='0.0.0.0'
port = 4220
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host, port))

data,addr = s.recvfrom(1024)

size = int(data)

f = open("result_file",'wb')
_data, addr = s.recvfrom(2000)
print('연결됨', addr)
number = 0
try:
   while(_data):
       number += 1
       proceed = ((1024*number)/size)*100
       if proceed > 100:
           print(print("current_size / total_size=",100))
       else:
           print("current_size / total_size=",proceed)
       f.write(_data)
       s.settimeout(2)
       _data,_ =s.recvfrom(1024)
except OSError:
             f.close()
             s.close()
             print("File Receive End")

