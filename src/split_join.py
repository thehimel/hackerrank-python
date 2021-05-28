"""
https://www.hackerrank.com/challenges/python-string-split-and-join/problem

>>> a = "this is a string"
>>> a = a.split(" ") # a is converted to a list of strings.
>>> print a
['this', 'is', 'a', 'string']

>>> a = "-".join(a)
>>> print a
this-is-a-string

Input:
this is a string

Output:
this-is-a-string
"""


def split_and_join(line):
    return '-'.join(line.split())


if __name__ == '__main__':
    line = 'this is a string'
    result = split_and_join(line)
    print(result)
