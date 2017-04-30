""" make a random list, prove you can count all uniqe occurrences of each item """

from __future__ import print_function

def random_list():
    """ Make random-length list of random numbers

    Returns:
        a list of ints
    """

    ip_list = []

    for i in range(0, 256):
        for j in range(0, 256):
#            print('10.0.' + str(i) + '.' + str(j))
            ip_list.append('-A oo-udp-limit -s 10.0.' + str(i) + '.' + str(j) +\
            ' -m limit --limit 30/s -m comment --comment "oo_udp_limit_id_%s_%s" -j RETURN' % (i, j))

    return ip_list


def main():
    """ Main function, print how many times the most common number appears """

    my_list = random_list()
    print('total number of rules: ', len(my_list))

    for i in my_list:
        print(i)


if __name__ == '__main__':
    main()
