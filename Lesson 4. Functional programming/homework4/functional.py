# Корреляция
# ● Контекст
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.

from math import sqrt

def mean(values):
    return sum(values) / len(values)

def pearson(x, y):
    mean_x, mean_y = mean(x), mean(y)
    diff_x = map(lambda xi: xi - mean_x, x)
    diff_y = map(lambda yi: yi - mean_y, y)

    numer = sum(map(lambda xi, yi: xi * yi, diff_x, diff_y))
    denom = sqrt(sum(map(lambda xi: xi ** 2, diff_x))) * sqrt(sum(map(lambda yi: yi ** 2, diff_y)))

    if denominator == 0:
        return 0
    else:
        return numer / denom


arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]

correlation = pearson(arr1, arr2)
print(f"Корреляция Пирсона: {correlation}")