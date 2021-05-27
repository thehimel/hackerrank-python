"""
https://www.hackerrank.com/challenges/list-comprehensions

Input:
x, y, z = 1, 1, 2
n = 3

Output:
[
    [0, 0, 0], [0, 0, 1], [0, 0, 2],
    [0, 1, 0], [0, 1, 1], [1, 0, 0],
    [1, 0, 1], [1, 1, 0], [1, 1, 2]
]

Explanation:
intermediate list:
[
    [0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1],
    [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0],
    [1, 1, 1], [1, 1, 2]
]

Sub lists that doesn't sum to n = 3 is the output.
"""


def solution(x, y, z, n):
    return [[i, j, k] for i in range(x+1)
            for j in range(y+1) for k in range(z+1)
            if i + j + k != n]


if __name__ == '__main__':
    x, y, z = 1, 1, 2
    n = 3
    print(solution(x, y, z, n))
