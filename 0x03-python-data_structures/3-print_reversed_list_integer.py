#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    new = my_list[::-1]
    for item in new:
        print("{:d}".format(item))
