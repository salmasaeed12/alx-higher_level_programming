#!/usr/bin/python3
"""
A peak element is an element that is strictly greater than its neighbors"""


def find_peak(list_of_integers):
    """find the peak element in a list"""
    i = 0
    if list_of_integers:
        for i in range(len(list_of_integers)):
            if i == 0 and list_of_integers[i] >= list_of_integers[i + 1]\
                    or i == len(list_of_integers) - 1 and\
                    list_of_integers[i] >= list_of_integers[i - 1]:
                return list_of_integers[i]
            else:
                if list_of_integers[i] >= list_of_integers[i - 1]\
                        and list_of_integers[i] >= list_of_integers[i + 1]:
                    return list_of_integers[i]
    else:
        return "None"
