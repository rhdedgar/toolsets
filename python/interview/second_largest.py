""" Find the numbers not included in the provided list, within its range. """

from __future__ import print_function


MY_LIST = [1, 2, 3, 11, 4, 17, 5, 10, 15, 20]

print(MY_LIST)

LARGEST = 0
SECOND_LARGEST = 0

for cur_num in MY_LIST:
    if LARGEST == 0:
        LARGEST = cur_num

    elif SECOND_LARGEST == 0:
        SECOND_LARGEST = LARGEST

    elif cur_num > LARGEST:
        SECOND_LARGEST = LARGEST
        LARGEST = cur_num

print(LARGEST)
print(SECOND_LARGEST)
