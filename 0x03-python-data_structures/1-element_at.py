#!/usr/bin/python3

def get_element(my_list, index):
    if index < 0 or index >= len(my_list):
        return None
    else:
        return my_list[index]

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# index = 2
# result = get_element(my_list, index)
# print(result)
