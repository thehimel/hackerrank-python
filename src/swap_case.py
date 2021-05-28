"""
https://www.hackerrank.com/challenges/swap-case/problem

Input:
HackerRank.com presents "Pythonist 2".

Output:
hACKERrANK.COM PRESENTS "pYTHONIST 2".
"""


def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = 'HackerRank.com presents "Pythonist 2".'
    result = swap_case(s)
    print(result)
