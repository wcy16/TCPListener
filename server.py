'''
simple tcp server
'''

from socket import *
import binascii
import sys

if len(sys.argv) == 2:
    port = int(sys.argv[1])
else:
    port = 8888

host = ''
#port = 502
addr = (host, port)

server = socket(AF_INET, SOCK_STREAM)
server.bind(addr)
server.listen(3)

while True:
    print('++++++++++++++++++++++++++++++++++++')
    print('Port:', port)
    print('Server is waiting for connection...')
    client, addr = server.accept()
    print('Connection established.')
    print('Client address :', addr)

    client.settimeout(0.1)
    while True:
        # recv
        print('Receiving....')
        #print('===============================')
        try:
            while True:
                data = client.recv(1)
                # print(data)
                print(binascii.hexlify(data).decode(), end=' ')
                # time.sleep(1)
                if not data or data == '':
                    break
        except timeout:
            pass
            # print("recv timeout")
        print()
        print('===============================')
        print('Received')
        # send
        print('Sending...')
        send = input('Send message or type ENTER to exit:')
        if send != '':
            client.send(send.encode())
            print('Sent.')
        else:
            break

    client.close()
