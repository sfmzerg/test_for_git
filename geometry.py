import math
from abc import ABC, abstractmethod


class Shape(ABC):
    """Abstract base class for all geometric shapes"""

    @abstractmethod
    def area(self) -> float:
        """Calculate the area of the shape"""
        pass

    @abstractmethod
    def is_right_angled(self) -> bool:
        """Check if the shape is right-angled (if applicable)"""
        pass


class Circle(Shape):
    """Circle shape defined by radius"""

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def is_right_angled(self) -> bool:
        """Circles cannot be right-angled"""
        return False


class Triangle(Shape):
    """Triangle shape defined by three sides"""

    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        """Check if sides can form a valid triangle"""
        return (a + b > c) and (a + c > b) and (b + c > a)

    def area(self) -> float:
        """Calculate area using Heron's formula"""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self) -> bool:
        """Check if triangle is right-angled using Pythagorean theorem"""
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(
            sides[0] ** 2 + sides[1] ** 2,
            sides[2] ** 2,
            rel_tol=1e-9
        )


class ShapeFactory:
    """Factory for creating shape instances without knowing type at compile-time"""

    @staticmethod
    def create_shape(shape_type: str, *args) -> Shape:
        """
        Create a shape instance based on type name and parameters

        Args:
            shape_type: 'circle' or 'triangle'
            *args: radius for circle, three sides for triangle

        Returns:
            Shape instance
        """
        shape_type = shape_type.lower()

        if shape_type == 'circle':
            return Circle(*args)
        elif shape_type == 'triangle':
            return Triangle(*args)
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


def calculate_area(shape: Shape) -> float:
    """Calculate area of any shape without knowing its type at compile-time"""
    return shape.area()