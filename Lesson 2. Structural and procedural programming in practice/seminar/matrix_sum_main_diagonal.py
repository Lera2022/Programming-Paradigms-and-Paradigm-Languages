import random


def find_main_sum(matrix: list[list[int]]) -> int:
    return sum(matrix[i][i] for i in range(len(matrix)))


def create_matrix() -> list[list[int]]:
    n = random.randint(3, 7)
    matrix = [[random.randint(0, 15) for i in range(n)] for j in range(n)]
    print(*matrix, sep='\n')
    return matrix


if __name__ == '__main__':
    print(find_main_sum(create_matrix()))
