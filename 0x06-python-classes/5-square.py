#!/usr/bin/python3
"""class Square that defines a square"""


class Square():
    """square class with its proper validation and size"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if (self.__size):
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end="")
                print()
        else:
            print()