"""
https://www.hackerrank.com/challenges/python-tuples/problem

Hash a tuple.

Input:
1 2

Output:
3713081631934410656
"""

if __name__ == '__main__':
    integer_list = [1, 2]
    print(hash(tuple(integer_list)))
