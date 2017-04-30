""" send regular UDP traffic """

import socket
import threading

UDP_IP = b"127.0.0.1"
UDP_PORT = 5005
MESSAGE = b"Hello, World!"

print ("UDP target IP:", UDP_IP)
print ("UDP target port:", UDP_PORT)
print ("message:", MESSAGE)


def test_func():
    """ Simulating UDP traffic. """

    sock = socket.socket(socket.AF_INET, # Internet
                         socket.SOCK_DGRAM) # UDP
    total_sent = 0

    for _ in range(1, 100):
        sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
        total_sent += 1

    print("total sent", total_sent)
    threading.Timer(1, test_func).start()


def main():
    """main function."""
    test_func()


if __name__ == '__main__':
    main()
