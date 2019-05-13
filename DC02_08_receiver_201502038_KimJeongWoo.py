import socket

host='0.0.0.0'
port = 3700
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('', port))

addr = (host,port)
buf=1024

f = open("result_file",'w')
data, addr= s.recvfrom(buf)

#size = int(data)
size = 1024
print('연결됨', addr)
print("out while")
count_num = 0;
while count_num < size:
    f.write(data.decode())
    count_num = count_num + 1024

f.close()
s.close()
print("FILE RECEIVE END")
