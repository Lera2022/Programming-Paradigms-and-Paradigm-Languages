import random


def normalize(numbers: list[int]) -> list[float]:
    max_val = max(numbers)
    min_val = min(numbers)
    delta = max_val - min_val

    return list(map(lambda x: (x - min_val) / delta, numbers))


if __name__ == '__main__':
    print(normalize([random.randint(0, 50) for _ in range(15)]))
