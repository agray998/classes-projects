'''
Create a shape class, and sub-classes which represent different geometric
shapes, such as rectangles, circles and triangles. Give these classes 
methods to perform standard geometric calculations such as finding the 
area and perimeter of a shape.
'''

from abc import ABC, abstractmethod
from math import pi, sqrt

class Shape(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def calculate_perimeter(self):
        return pi * (2 * self.radius)
    
    calculate_circumference = lambda self: self.calculate_perimeter()
    
    def calculate_area(self):
        return pi * (self.radius ** 2)
    
    def arc_length(self, theta):
        return self.radius * theta
    
    def sector_area(self, theta):
        return 0.5 * (self.radius ** 2) * theta

class Triangle(Shape):
    def __init__(self, base, height, a = 1):
        self.base = base
        self.height = height
        self.a = a
    
    def calculate_area(self):
        return 0.5 * self.base * self.height
    
    def calculate_perimeter(self):
        tr_a = RightTriangle((self.a * self.base), self.height)
        tr_b = RightTriangle(((1 - self.a) * self.base), self.height)
        return self.base + tr_a.calculate_hypotenuse() + tr_b.calculate_hypotenuse()

class RightTriangle(Triangle):
    def calculate_hypotenuse(self):
        return sqrt((self.base ** 2) + (self.height ** 2))
    
    def calculate_perimeter(self):
        return self.base + self.height + self.calculate_hypotenuse()

class Trapezoid(Shape):
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h
    
    def calculate_area(self):
        return 0.5 * (self.a + self.b) * self.h
    
    def calculate_perimeter(self):
        triangle = RightTriangle(abs(self.a - self.b), self.h)
        return self.a + self.b + 2 * (triangle.calculate_hypotenuse())

# Example usage
rect = Rectangle(3, 4)
print("Rectangle perimeter:",rect.calculate_perimeter())
print("Rectangle area:", rect.calculate_area())
circ = Circle(5)
print("Circle area:", circ.calculate_area())
print("Circle circumference:", circ.calculate_circumference())
trap = Trapezoid(3, 5, 3)
print("Trapezoid area:", trap.calculate_area())
print("Trapezoid perimeter:", trap.calculate_perimeter())
tri = Triangle(6, 1.5, (3.2 / 6))
print("Triangle perimeter:", tri.calculate_perimeter())
