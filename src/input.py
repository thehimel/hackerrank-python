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

Input:
2 15
x**4 - x + 1

Output:
True

Explanation:
2**4 - 2 + 1 = 15
"""


def solution(xk, equation):
    # Get a list of 2 numbers after the split
    xk = list(map(int, xk.split()))
    x, k = xk[0], xk[1]  # noqa: F841

    # Evaluating string equation
    return eval(equation) == k


if __name__ == '__main__':
    xk = '2 15'
    equation = 'x**4 - x + 1'
    print(solution(xk, equation))
