#!/usr/bin/python3
"""
square class
"""


class Square:

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position
    """
    creates a square object
    """
    @property
    def size(self):
        return self.__size
        """
        gets size
        """
    @property
    def position(self):
        return self.__position
        """
        gets position
        """
    @position.setter
    def position(self, value):
        """sets position"""
        if(type(value) is not tuple or len(value) is not 2 or
           type(value[0]) is not int or
           type(value[1]) is not int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if(value[0] < 0 or value[1] < 0):
            raise ValueError("position must be a tuple of 2 positive integers")
        self.__position = value

    @size.setter
    """sets size to an integer"""
    def size(self, value):
        if(type(value) is not int):
            raise TypeError("size must be an integer")
        elif(value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
    def area(self):
        """return area"""
        return(self.__size * self.__size)

    def my_print(self):
        """prints"""
        if(self.size == 0):
            print()
            return
        for x in range(self.position[1]):
            print()
        for x in range(self.size):
            print("{}{}".format(" " * self.position[0], "#" * self.size))
