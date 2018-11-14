'''
dummy client for test use
'''
import socket
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',9999))

print('connected.')

while True:
    #s.send(str(time.time()).encode())
    s.send(b'abcdefghijklmn')
    print(s.recv(1024))


# s.close()