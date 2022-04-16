# Using TDD, create a Rectangle class. It should be initialized with width and height.
# #It should have the following methods: get_area, get_perimeter. Create a Square class.
# It should be a subclass of Rectangle. It should be initialized with length.

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        area = self.width * self.height
        return area

    def get_perimeter(self, width, height):
        perimeter = width + height
        return perimeter


class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)


