import pytest
import math
from geometry import Circle, Triangle, ShapeFactory, calculate_area


class TestCircle:
    def test_area(self):
        circle = Circle(5)
        assert math.isclose(circle.area(), 78.539816, rel_tol=1e-6)

    def test_negative_radius(self):
        with pytest.raises(ValueError):
            Circle(-1)

    def test_zero_radius(self):
        with pytest.raises(ValueError):
            Circle(0)

    def test_right_angled(self):
        assert not Circle(5).is_right_angled()


class TestTriangle:
    def test_area(self):
        triangle = Triangle(3, 4, 5)
        assert math.isclose(triangle.area(), 6.0)

    def test_invalid_triangle(self):
        with pytest.raises(ValueError):
            Triangle(1, 1, 3)

    def test_right_angled(self):
        assert Triangle(3, 4, 5).is_right_angled()
        assert not Triangle(3, 4, 6).is_right_angled()

    def test_negative_sides(self):
        with pytest.raises(ValueError):
            Triangle(-1, 2, 2)


class TestShapeFactory:
    def test_create_circle(self):
        circle = ShapeFactory.create_shape('circle', 10)
        assert isinstance(circle, Circle)
        assert math.isclose(circle.area(), 314.159265, rel_tol=1e-6)

    def test_create_triangle(self):
        triangle = ShapeFactory.create_shape('triangle', 5, 12, 13)
        assert isinstance(triangle, Triangle)
        assert triangle.is_right_angled()

    def test_invalid_shape_type(self):
        with pytest.raises(ValueError):
            ShapeFactory.create_shape('square', 5)


class TestCalculateArea:
    def test_polymorphic_area(self):
        shapes = [
            Circle(2),
            Triangle(3, 4, 5)
        ]
        areas = [calculate_area(s) for s in shapes]
        assert math.isclose(areas[0], 12.566371, rel_tol=1e-6)
        assert math.isclose(areas[1], 6.0)