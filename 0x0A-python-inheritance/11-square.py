#!/usr/bin/python3
"""Module that defines a Square class"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Square class that inherits from Rectangle"""

    def __init__(self, size):
        """Initialize the Square instance with a given size."""
        self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the Square."""
        return "[Square] {}/{}".format(self.width, self.height)

if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())

