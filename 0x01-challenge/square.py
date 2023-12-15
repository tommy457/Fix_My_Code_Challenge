#!/usr/bin/python3
""" Module for square class """


class square:
    """ Square class """
    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """Constructor"""
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        """ Permiter of the square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ Return a human-readable represantation of a square """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Create square and print its area and permiter and its represantation"""
    s = square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
