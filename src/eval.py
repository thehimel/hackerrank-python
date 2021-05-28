"""
https://www.hackerrank.com/challenges/python-eval

>>> eval("9 + 5")
14
>>> x = 2
>>> eval("x + 3")
5

>>> type("len")
<type 'str'>

Sample Input
print(2 + 3)

Sample Output
5
"""


def solution(command):
    eval(command)


if __name__ == '__main__':
    command = 'print(2 + 3)'
    solution(command)
