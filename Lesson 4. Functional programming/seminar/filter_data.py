import random


def filter_data(people: list[tuple]) -> int:
    return sum(map(lambda p: p[1] > 30, people))


def another_filter():
    data = [{"name": "Sergey", "age": random.randint(20, 38)}, {"name": "Maxim", "age": random.randint(20, 38)},
            {"name": "Ivan", "age": random.randint(20, 38)}]
    print(data)
    return sum(map(lambda p: p['age'] > 30, data))


if __name__ == '__main__':
    data = [
        ('John', random.randint(20, 38)),
        ('John', random.randint(20, 38)),
        ('John', random.randint(20, 38)),
        ('John', random.randint(20, 38)),
        ('John', random.randint(20, 38)),
        ('John', random.randint(20, 38)),
        ('John', random.randint(20, 38)),
    ]
    print(data)
    print(filter_data(data))
    print(another_filter())
