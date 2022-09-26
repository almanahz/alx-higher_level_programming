#!/bin/usr/python3
def element_at(my_list, idx):
    for x in my_list:
	if idx < 0:
	    return "none"
	elif idx > len(my_list):
	    return "none"  
	else:
	    return my_list[idx]
