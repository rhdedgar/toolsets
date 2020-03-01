""" Simple TCP client for simulating outbound TCP data. """
from __future__ import print_function

import socket
import threading


def re_run():
    """ Schedule a job to repeatedly run. """

    print("testing")
    threading.Timer(5, re_run).start()


def tcp_traffic():
    """ Send test outbound TCP connection to google. """

    target_host = 'www.shinobu-shinobu.rhcloud.com'
    target_port = 80

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((target_host, target_port))

    client.send(b'GET / HTTP/1.1\r\\nHost: shinobu-shinobu.rhcloud.com\r\n\r\n')

    response = client.recv(4096)

    print(response, '\n')
    threading.Timer(15, tcp_traffic).start()


def main():
    """ Main function. """

    tcp_traffic()


if __name__ == '__main__':
    main()
