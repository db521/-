# -*- coding: cp936 -*-
import socket

target_host = "127.0.0.1"
target_port = 80

#����һ��socket ����
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#����һЩ����
client.sendto("AAABBBCCC",(target_host,target_port))

#����һЩ����
data,addr = client.recvfrom(4096)

print data
