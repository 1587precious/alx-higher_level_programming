#!/usr/bin/python3
"""Module that defines a Square class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the Square instance with a given size."""
        super().__init__(size, size)

if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

