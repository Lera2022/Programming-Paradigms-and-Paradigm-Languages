import random
import time


def wrapper(fn):
    def inner(*args, **kwargs):
        start_time = time.perf_counter()
        result = fn(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(total_time)
        return result

    return inner


@wrapper
def proportion_of_numbers(numbers: list[int]) -> tuple[float, float, float]:
    negatives, positives, zeroes = 0, 0, 0
    for el in numbers:
        if el < 0:
            negatives += 1
        elif el > 0:
            positives += 1
        else:
            zeroes += 1
    if negatives > 0:
        negatives /= len(numbers)
    if positives > 0:
        positives /= len(numbers)
    if zeroes > 0:
        zeroes /= len(numbers)
    return negatives, zeroes, positives


@wrapper
def declarative_proportions(numbers: list[int]) -> tuple[float, float, float]:
    return len(list(filter(lambda el: el < 0, numbers))) / len(numbers), len(list(filter(lambda el: el == 0, numbers))) / len(
        numbers), len(list(filter(lambda el: el > 0, numbers))) / len(numbers),

@wrapper
def map_proportions(numbers: list[int]) -> tuple[float, float, float]:
    return sum(map(lambda el: el < 0, numbers)) / len(numbers), sum(map(lambda el: el == 0, numbers)) / len(
        numbers), sum(map(lambda el: el > 0, numbers)) / len(numbers),


if __name__ == '__main__':
    arr = [random.randint(-20, 20) for _ in range(20)]
    print(arr)
    print(proportion_of_numbers(arr))
    print(declarative_proportions(arr))
    print(map_proportions(arr))
