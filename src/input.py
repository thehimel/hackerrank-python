"""
https://www.hackerrank.com/challenges/input/problem

Input format:
x k
P(x)

Output format:
return True if P(x) = k, else return False.

Input:
1 4
x**3 + x**2 + x + 1

Output:
True

Explanation:
1**3 + 1**2 + 1 + 1 = 4
"""


def solution(x_k, equation):
    # First item
    x, k = int(x_k[0]), int(x_k[-1])  # noqa: F841

    # Evaluating string equation
    return eval(equation) == k


if __name__ == '__main__':
    x_k = '1 4'
    equation = 'x**3 + x**2 + x + 1'
    print(solution(x_k, equation))
