#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in range(len(matrix)):
        i = 1
        for col in range(len(matrix[row])):
            if i == len(matrix):
                print("{:d}".format(matrix[row][col]))
            else:
                print("{:d}".format(matrix[row][col]), end = " ")    
            i = i + 1
