#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import socket
import time

IP = '3.34.178.210'
TCP_PORT = 54147
BUFFER_SIZE = 1024
MESSAGE = '안녕 서버'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, TCP_PORT))
s.send(MESSAGE.encode('utf-8'))
print('Sending data:', MESSAGE)
data = s.recv(BUFFER_SIZE)
print('Data from server:', data.decode('utf-8'))
s.close()
