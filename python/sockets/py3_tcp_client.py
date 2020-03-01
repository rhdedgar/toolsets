""" test udp client """
#!/usr/bin/python3
from __future__ import print_function

import socket

# create a socket object
S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
#HOST = socket.gethostname()
HOST = '10.0.0.124'
PORT = 9999

# connection to hostname on the port.
S.connect((HOST, PORT))

# Receive no more than 1024 bytes
MSG = S.recv(1024)

S.close()

print(MSG.decode('ascii'))
