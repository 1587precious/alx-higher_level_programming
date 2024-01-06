#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        if len(row) == 0:
            print()
        for n in range(len(row)):
            print('{:d}'.format(row[n]), end=' ')
        print()

# Example usage:
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print_matrix_integer(matrix)
