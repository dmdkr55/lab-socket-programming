#!/usr/bin/env python3
# test5
import socket
import time

IP_ADDR = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1) 
s.bind((IP_ADDR, TCP_PORT))
s.listen(1)

data = b"Hello World"

conn, addr = s.accept()
print('Client address:', addr)

for _ in range(10): 
     #currentTime = time.ctime(time.time()) 
     data = b"Hello World" 
     #+ currentTime.encode('ascii')
     time.sleep(0.000001)
     conn.send(data*24)  # echo

conn.close()
