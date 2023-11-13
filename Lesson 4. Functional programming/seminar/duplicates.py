import random
from collections import Counter


def find_duplicates(numbers: list[int]) -> list[int]:
    counts = Counter(numbers)
    print(counts)
    return list(filter(lambda x: counts.get(x) > 1, counts))


arr = [random.randint(0, 5) for _ in range(15)]
print(arr)

print(find_duplicates(arr))
