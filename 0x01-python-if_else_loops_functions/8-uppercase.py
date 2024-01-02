#!/usr/bin/python3
def uppercase(input_str):
    for char_index in range(len(input_str)):
        if ord(input_str[char_index]) >= 97 and ord(input_str[char_index]) <= 122:
            offset = 32
        else:
            offset = 0
        print("{:c}".format(ord(input_str[char_index]) - offset), end='')
