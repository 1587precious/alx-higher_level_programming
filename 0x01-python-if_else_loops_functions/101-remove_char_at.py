#!/usr/bin/python3
def remove_char_at(input_str, index):
    result_str = ""
    for i in range(len(input_str)):
        if i != index:
            result_str = result_str + input_str[i]
    return result_str
