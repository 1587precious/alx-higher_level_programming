#!/usr/bin/python3
"""Module that defines a rebel MyInt class"""

class MyInt(int):
    """Rebel MyInt class that inverts == and != operators"""

    def __eq__(self, other):
        """Override the equality operator =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the inequality operator !="""
        return super().__eq__(other)

if __name__ == "__main__":
    my_i = MyInt(3)

    print(my_i)
    print(my_i == 3)
    print(my_i != 3)

