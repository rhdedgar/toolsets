""" Simple TCP client for simulating outbound TCP data. """
from __future__ import print_function

import urllib.request
import threading

def test_func():
    """testing tcp traffic."""

    print(urllib.request.urlopen\
    ("http://dedgarpy1-shinodev.5c20.ded-stage-aws.openshiftapps.com/").read())
    print('\n')
    threading.Timer(5, test_func).start()

def main():
    """main function."""
    test_func()

if __name__ == '__main__':
    main()
