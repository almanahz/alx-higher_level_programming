#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):



    if my_list:
        index = 0
        count = 0

        while (index < x):
            try:
                print("{:d}".format(my_list[index]), end="")
                count+=1
                index += 1
            except (TypeError, ValueError):
                index += 1
                continue
          
        print("")

    return count
