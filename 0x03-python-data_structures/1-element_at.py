#!/bin/usr/python3
def element_at(my_list, idx):
    if idx >= len(my_list):
        return "none"
    elif idx < 0:
        return "none"
    else:
        return my_list[idx]
