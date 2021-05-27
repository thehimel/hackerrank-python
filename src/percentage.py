"""
student_marks = {
    'Krishna': [67.0, 68.0, 69.0],
    'Arjun': [70.0, 98.0, 63.0],
    'Malika': [52.0, 56.0, 60.0]
}

A dictionary with name and marks are given.
Return the average of the marks for a specific person.

Input:
Malika

Output:
56.00
"""


def solution(student_marks, name):
    percentage = sum(student_marks[name])/len(student_marks[name])
    # Converting 56.0 to 56.00, 28.0 to 28.00
    return f'{round(percentage, 2):.2f}'


if __name__ == '__main__':
    student_marks = {
        'Krishna': [67.0, 68.0, 69.0],
        'Arjun': [70.0, 98.0, 63.0],
        'Malika': [52.0, 56.0, 60.0]
    }

    query_name = 'Malika'
    print(solution(student_marks, query_name))
