#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        i = 1
        for col in row:
            if i == len(matrix):
                print("{:d}".format(col))
            else:
                print("{:d}".format(col), end = " ")
            i = i + 1

