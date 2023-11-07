# Задача №2
# Написать точно такую же процедуру, но в декларативном стиле

import random


def main():
    arr = [random.randint(0, 150) for _ in range(30)]
    print(arr)
    arr.sort()
    print(arr)


if __name__ == '__main__':
    main()
