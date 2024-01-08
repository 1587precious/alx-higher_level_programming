#!/usr/bin/python3

def replace_in_list(my_list, index, new_element):
    if 0 <= index < len(my_list):
        my_list[index] = new_element
    return my_list

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# index = 2
# new_element = 10
# result = replace_in_list(my_list, index, new_element)
# print(result)
