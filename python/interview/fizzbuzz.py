"""
 count from 1 to 100, print fizz for multiples of 3,
 buzz for multiples of 5, and fizzbuzz for numbers that are multiples of both
"""

from __future__ import print_function


def fizzbuzz(some_int):
    """ Print the provided int or replace it with a string. """

    if some_int % 3 == 0 and some_int % 5 == 00:
        print('FizzBuzz')

    elif some_int % 3 == 0:
        print('Fizz')

    elif some_int % 5 == 0:
        print('Buzz')

    else:
        print(some_int)


def main():
    """ Main function, specify the range to provide to fizzbuzz method """

    for some_int in range(1, 101):
        fizzbuzz(some_int)


if __name__ == '__main__':
    main()
