from Crypto.Cipher import AES
from Crypto.Random import random
import base64
import challenge12
from challenge11 import random_bytes
from challenge9 import test_block
from challenge8 import get_block, get_intblock


key = None
prefix = None


def encryption_oracle(s):
    global key
    global prefix
    if key is None:
        key = random_bytes(16)
    if prefix is None:
        # TODO(akalin): Extend to arbitrary sizes.
        randcount = random.randint(16, 32)
        prefix = random_bytes(randcount)
    cipher = AES.new(key, AES.MODE_ECB)
    s = test_block(prefix + s + base64.b64decode(challenge12.enc_string), 16)
    return cipher.encrypt(s)


#def getBlocks(s, blocksize):
#    return [s[i:i+blocksize] for i in range(0, len(s), blocksize)]


def findPrefixBlock(encryption_oracle, blocksize):
    x1 = encryption_oracle(b'')
    x2 = encryption_oracle(b'0')
    blocks1 = get_block(x1, blocksize)
    blocks2 = get_block(x2, blocksize)
    for i in range(len(blocks1)):
        if blocks1[i] != blocks2[i]:
            return i


def findPrefixSizeModBlockSize(encryption_oracle, blocksize):
    def has_equal_block(blocks):
        for i in range(len(blocks) - 1):
            if blocks[i] == blocks[i+1]:
                return True
        return False

    for i in range(blocksize):
        s = bytes([0] * (2*blocksize + i))
        t = encryption_oracle(s)
        blocks = get_block(t, blocksize)
        if has_equal_block(blocks):
            return blocksize - i

    raise Exception('Not using ECB')


def findPrefixSize(encryption_oracle, blocksize):
    return blocksize*findPrefixBlock(encryption_oracle, blocksize) + findPrefixSizeModBlockSize(encryption_oracle, blocksize)


def findNextByte(encryption_oracle, blocksize, prefixsize, knownBytes):
    k1 = blocksize - (prefixsize % blocksize)
    k2 = blocksize - (len(knownBytes) % blocksize) - 1
    k3 = prefixsize - (prefixsize % blocksize)
    s = bytes([0] * (k1 + k2))
    d = {}
    for i in range(256):
        t = encryption_oracle(s + knownBytes + bytes([i]))
        d[t[k3+k1:k3+k1+k2 + len(knownBytes) + 1]] = i
    t = encryption_oracle(s)
    u = t[k3+k1:k3+k1+k2 + len(knownBytes) + 1]
    if u in d:
        return d[u]
    return None

blocksize = challenge12.cipher_block_size(encryption_oracle)
prefixsize = findPrefixSize(encryption_oracle, blocksize)
s = b''
while True:
    b = findNextByte(encryption_oracle, blocksize, prefixsize, s)
    if b is None:
        break
    s += bytes([b])
print(s)
