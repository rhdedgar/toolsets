""" Find the numbers not included in the provided list, within its range. """

from __future__ import print_function

# using extended slice sequence method
ITEM_0 = 'wasitacatisaw'
#ITEM_1 = ''

print(ITEM_0)

ITEM_REV = ITEM_0[::-1]

if ITEM_0 == ITEM_REV:
    print('yep!')
else:
    print('nope!')
