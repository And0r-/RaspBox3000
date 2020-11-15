#socket_echo_client.py

import socket
import sys
import kb_map

import keyboard
import time

NULL_CHAR = chr(0)
release_key = (NULL_CHAR*8).encode()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.50.242', 10000)
server_address2 = ('192.168.50.117', 10000)


print('connecting to {} port {}'.format(*server_address))

sock.connect(server_address)

print('connecting to {} port {}'.format(*server_address2))
sock2.connect(server_address2)



def send_key(key):


    try:

        # Send data
        message = (chr(kb_map.convert(key)[0])+NULL_CHAR+chr(kb_map.convert(key)[1])+NULL_CHAR*5).encode()
        print('sending {!r}'.format(message))
        sock.sendall(message)
        sock.sendall(release_key)
        sock2.sendall(message)
        sock2.sendall(release_key)

        # Look for the response
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received {!r}'.format(data))

    finally:
        print('gesendet')

def key_press(key):
    send_key(key.name)

keyboard.on_press(key_press)

while True:
    time.sleep(1)
