# polymorphism_demo.py

import math

class Shape:
    """Base class representing a generic shape."""
    def area(self):
        """Method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method.")


class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius: float):
        self.radius = radius

    def area(self):
        """Calculate and return the area of the circle."""
        return math.pi * (self.radius ** 2)


# Example usage demonstrating polymorphism
if __name__ == "__main__":
    # Create a list of different shapes
    shapes = [
        Rectangle(10, 5),
        Circle(7),
        Rectangle(3, 8),
        Circle(2.5)
    ]

    # Iterate through shapes and call area() polymorphically
    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area():.2f}")
