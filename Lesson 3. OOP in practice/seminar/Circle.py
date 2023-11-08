import math

from Shape import Shape


class Circle(Shape):

    def __init__(self, radius: float):
        self.radius = radius

    def get_area(self) -> float:
        return math.pi * self.radius ** 2

    def get_perimeter(self) -> float:
        return 2 * math.pi * self.radius


if __name__ == '__main__':
    circle = Circle(5)
    print(circle.get_perimeter())
    print(circle.get_area())