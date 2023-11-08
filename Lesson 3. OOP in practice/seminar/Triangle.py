from Shape import Shape


class Triangle(Shape):

    def __init__(self, a: float, b: float, c: float):
        biggest_size = max(a, b, c)
        if biggest_size > (a + b + c - biggest_size):
            raise ValueError('Should be a triangle')
        self.c = c
        self.b = b
        self.a = a

    def get_area(self) -> float:
        p = 0.5 * self.get_perimeter()
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def get_perimeter(self) -> float:
        return self.a + self.b + self.c

    @staticmethod
    def greeting():
        print('hello')


if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print(triangle.get_area())
    print(triangle.get_perimeter())

    try:
        tt = Triangle(10, 2, 3)
    except ValueError as e:
        print('Error:', e)

    Triangle.greeting()
