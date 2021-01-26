# Exercise 1: Object Oriented Programming

import math

class Circle:

    def __init__(self, radius: int):
        self.radius = radius

    def findArea(self) -> float:
        return math.pi * (self.radius ** 2)

    def findPerimeter(self) -> float:
        return 2 * math.pi * self.radius


circle = Circle(3)
print('Circle area: ', circle.findArea())
print('Circle perimeter: ', circle.findPerimeter())

# total time used: 3 mins