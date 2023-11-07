import random


def imperative_search(array: list[int], target: int) -> bool:
    for el in array:
        if el == target:
            return True
    else:
        return False


if __name__ == '__main__':
    arr = [random.randint(0, 50) for _ in range(20)]
    print(arr)
    result = imperative_search(arr, 12)
    print(result)
