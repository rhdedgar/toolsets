import socket

UDP_IP = b"127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
total_sent = 0
for i in range(1, 100):
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    total_sent += 1
print("done")
print("total sent", total_sent)
