# -*- coding: cp936 -*-
import socket

target_host = "www.baidu.com"
target_port = 80

#����һ��socket ����
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#���ӿͻ���
client.connect((target_host,target_port))

#����һЩ����
client.send("GET / HTTP/1.1\r\nHost: baidu.com\r\n\r\n")

#����һЩ����
response = client.recv(4096)

print response
