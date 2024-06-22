#!/usr/bin/python3
def no_c(my_string):
    copied_list = ""
    for i in my_string:
        if (i != 'c' and i != 'C'):
            copied_list += i
    return (copied_list)
