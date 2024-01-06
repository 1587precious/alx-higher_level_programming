#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    for num in my_list:
        if num % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list

# Example usage:
# my_list = [1, 2, 3, 4, 5]
# result = divisible_by_2(my_list)
# print(result)
