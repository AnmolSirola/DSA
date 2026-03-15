# Abstraction hides implementation details and only exposes essential features.
# Python implements abstraction using abstract classes.

from abc import ABC, abstractmethod


class Shape(ABC):   # abstract base class

    @abstractmethod
    def area(self):   # abstract method
        pass


class Circle(Shape):

    def __init__(self, radius):
        self.radius = radius

    def area(self):   # implementing abstract method
        return 3.14 * self.radius * self.radius


circle = Circle(5)

print(circle.area())