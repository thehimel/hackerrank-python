"""
https://www.hackerrank.com/challenges/matrix-script/problem

Input:
['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']

output:
This is Matrix# %!

Observation:
matrix = [
    ['T', 's', 'i'],
    ['h', '%', 'x'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['i', 'r', '!']
]
"""
import re


def solution(input_matrix):
    matrix = [[char for char in item] for item in input_matrix]

    sentence = str()
    columns = len(matrix[0])
    rows = len(matrix)

    # Iterate over the matrix vertically
    for col in range(columns):
        for row in range(rows):
            sentence += matrix[row][col]

    return re.sub(r"(?<=\w)([^\w]+)(?=\w)", " ", sentence)


input_matrix = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
print(solution(input_matrix))
