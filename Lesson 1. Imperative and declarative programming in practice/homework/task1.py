# Задача №1
# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.

import random


def quick_sort(sorting_numbers: list[int]) -> list[int]:
    if len(sorting_numbers) < 2:
        return sorting_numbers
    else:
        pivot = sorting_numbers[0]
        less = [i for i in sorting_numbers[1:] if i <= pivot]
        greater = [i for i in sorting_numbers[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)


if __name__ == '__main__':
    arr = [random.randint(0, 150) for _ in range(30)]
    print(arr)
    new_arr = quick_sort(arr)
    print(new_arr)
