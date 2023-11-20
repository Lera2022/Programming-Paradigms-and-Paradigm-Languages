import random


def merge_lists(n_list: list[int], m_list: list[int]) -> list[int]:
    n = len(n_list)
    m = len(m_list)
    result = []
    i, j = 0, 0

    while i < n and j < m:
        if n_list[i] < m_list[j]:
            result.append(n_list[i])
            i += 1
        else:
            result.append(m_list[j])
            j += 1
    else:
        result.extend([*n_list[i:], *m_list[j:]])
        return result


def merge_sort(numbers: list[int]):
    if len(numbers) < 2:
        return numbers[:]

    middle = len(numbers) // 2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge_lists(left, right)


if __name__ == '__main__':
    nums = [random.randint(0, 40) for _ in range(10)]
    print(nums)

    print(merge_sort(nums))