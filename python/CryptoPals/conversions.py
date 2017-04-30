import base64
from binascii import hexlify, unhexlify
import Crypto.Cipher
import inspect


def fromhex():
    print('\ninput hex to decode:\n')
    astring = input()
    print(unhexlify(astring))

def frombase():
    print('\ninput base64 to decode:\n')
    astring = input()
    print (base64.b64decode(astring))

function_dict = {'fromhex':fromhex, 'frombase':frombase}

if __name__ == "__main__":
#    all_functions = inspect.getmembers(self(), inspect.isfunction)
#    somelist = [method for method in (object) if callable(getattr(object, method))]
#    print(somelist)
    print('pick from the following functions: \n\nfromhex\n\nfrombase\n')
    command = input()
    function_dict[command]()