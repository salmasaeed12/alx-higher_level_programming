#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0 or idx > (len(my_list) - 1)):
        return (my_list.copy())
    else:
        count = 0
        copied_list = my_list.copy()
        for i in copied_list:
            if (count == idx):
                copied_list[count] = element
                return (copied_list)
            count += 1
