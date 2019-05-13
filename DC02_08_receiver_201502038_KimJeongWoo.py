import socket

host='0.0.0.0'
port = 4160
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((host, port))

f = open("result_file",'wb')
data, addr = s.recvfrom(2000)

print('연결됨', addr)

while(data):
    f.write(data)
    if data:
      break
    data,_ =s.recvfrom(1024)

f.close()
s.close()
print("FILE RECEIVE END")
