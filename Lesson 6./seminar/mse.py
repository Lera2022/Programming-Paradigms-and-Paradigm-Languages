import random


def create_array(n: int = 10):
    return [random.randint(0, 5) for _ in range(n)]


def find_mse(l1: list[int], l2: list[int]) -> float:
    return sum(map(lambda xy: (xy[0] - xy[1])**2, zip(l1, l2))) / len(l1)


def main():
    true_values = create_array()
    result_values = create_array()

    print(true_values, result_values, sep='\n')

    print(find_mse(true_values, result_values))


if __name__ == '__main__':
    main()
