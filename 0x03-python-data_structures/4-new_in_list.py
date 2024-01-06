#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
    if 0 <= idx < len(my_list):
        new_list[idx] = element
    return new_list

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# index = 2
# new_element = 10
# result = new_in_list(my_list, index, new_element)
