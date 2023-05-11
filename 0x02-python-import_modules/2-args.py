#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    len_args = len(argv) - 1
    if len_args == 0:
        print("0 arguments.")
    elif len_args == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print("{} arguments:".format(len_args))
        for i in range(1, len(argv)):
            print("{}: {}".format(i, argv[i]))
