#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    x = min(my_list)
    else:
        for i in my_list:
            if i > x:
                x = i
        return x
