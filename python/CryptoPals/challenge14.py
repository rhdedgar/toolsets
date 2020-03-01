import base64

from challenge12 import random_bytes, cipher_block_size, encryption_oracle, enc_string, random_key, is_length
from challenge7 import encrypt_aes
from challenge9 import pad_block, test_block, pad_blocks


def encryption_oracle_c12(unknown_string):
    # base64 decode the string, pad it, and then encrypt with the random key
    unknown_string = test_block(unknown_string + base64.b64decode(enc_string), 16)
    encrypted = encrypt_aes(unknown_string, random_key)
    return encrypted


def is_length2(encryption_oracle, block_size, byte_string):
    pad_size = bytes([0] * (block_size - (len(byte_string) % block_size) - 1))
#    print('printing pad_size')
#    print(type(pad_size))
#    print(type(block_size))
#    print(type(byte_string))
    p_dict = {}
    for pos in range(256):
        # cycle through every byte possible, add to possibilities dictionary
        cur_item = encryption_oracle(pad_size + byte_string + bytes([pos]))
        print(cur_item)
        p_dict[cur_item[0:len(pad_size) + len(byte_string) + 1]] = pos
    cur_item = encryption_oracle(pad_size)
    inc_item = cur_item[0:len(pad_size) + len(byte_string) + 1]
    if inc_item in p_dict:
        return p_dict[inc_item]
#    print('not found in list')
    return None

def encrypter(to_decrypt):
#    print('printing enc_data')
    data = base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
    random_key = random_bytes(16)
    enc_data =  encrypt_aes(test_block(data + to_decrypt, 16), random_key)
#    print('printing enc_data from encrypter:', enc_data)
    return enc_data


def ecb_padding_oracle(to_decrypt):
#    print('inside ecb_padding_oracle')
#    print(to_decrypt)
    random_key = random_bytes(16)
#    print('random key is', random_key)
    def encrypt(data):
#        return encrypt_aes(pad_block(data + to_decrypt, 16), key)
#        print('data is type', data)
#        print('to_decrypt is type', type(to_decrypt))
#        print('to_decrypt')
#        print(to_decrypt)
#        print('data')
#        print(data)
        enc_data =  encrypt_aes(test_block(data + to_decrypt, 16), random_key)
#        print('printing from ecb padding oracle')
#        print(type(enc_data), enc_data)
        return enc_data
    return encrypt


#def encrypto(more_to):
#    print('printing from encrypto')
#    byte_len = 16
#    random_key = random_bytes(byte_len)
#    print(type(data))
#    m_results = encrypt_aes(pad_block(data + more_to, byte_len), random_key)
#    return m_results


if __name__ == '__main__':
    data =  base64.b64decode('Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK')
#    print(is_length(data, 16, ecb_padding_oracle))
#    print(data)
#    print('printing from main')
#    print(ecb_padding_oracle(data))
##    usedata = ecb_padding_oracle(data)
    usedata = encrypter(data)
#    print('printing userdata from main:        ', usedata)
##    print(test_fin(encryption_oracle, 16, data, usedata))
    print(is_length(encryption_oracle, 16, data))
#    usedata = encrypto(data)
#    print('printing usedata')
#    print(usedata)
#    print(is_length(ecb_padding_oracle, 16, data))
#    print(is_length(ecb_padding_oracle(data), 16, data))
#    print(is_length(usedata, 16, data))
##    print(is_length(ecb_padding_oracle, 16, data))
#    byte_string =b''
#    while True:
##        next_byte = is_length(ecb_padding_oracle, 16, byte_string)
#        next_byte = cipher_block_size(encryption_oracle)
#        if next_byte is None:
#            break
#        byte_string += bytes([next_byte])
#    print(byte_string)

