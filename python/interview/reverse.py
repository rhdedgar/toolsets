""" Find the numbers not included in the provided list, within its range. """

from __future__ import print_function


ITEM_0 = 'wasitacatisaw'
#ITEM_1 = ''

print(ITEM_0)

COUNTER = 0
LENGTH_OF_ITEM = len(ITEM_0)

for letter in ITEM_0:
    pos = LENGTH_OF_ITEM - COUNTER -1

    print(letter, ITEM_0[pos])

    if letter == ITEM_0[pos]:
        COUNTER += 1
    else:
        break

print(COUNTER, LENGTH_OF_ITEM)

if COUNTER == (LENGTH_OF_ITEM):
    print('yep!')
else:
    print('nope!')
