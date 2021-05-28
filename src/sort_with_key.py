"""
https://www.hackerrank.com/challenges/python-sort-sort/problem

Input:
5 3 -> n x m Matrix
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1 -> k value, based on which you need to sort.

Output:
7 1 0
10 2 5
6 5 9
9 9 9
1 23 12

https://docs.python.org/3/howto/sorting.html

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)   # sort by age
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
"""
from operator import itemgetter


def solution(data, k):
    return sorted(data, key=itemgetter(k))


if __name__ == '__main__':
    k = 1
    data = [
        '10 2 5',
        '7 1 0',
        '9 9 9',
        '1 23 12',
        '6 5 9'
    ]

    for i, item in enumerate(data):
        # Return list by splitting the text and coverting to int.
        data[i] = list(map(int, item.split()))

    data = solution(data, k)

    for row in data:
        row = list(map(str, row))
        print(' '.join(row))
