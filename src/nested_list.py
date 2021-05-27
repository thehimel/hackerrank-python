"""
https://www.hackerrank.com/challenges/nested-list

Given a multi dimensional array with name and score.

Get the person with the second highest score.
If there are multiple persons available with the same score,
sort and print the names.

Input:
students = [
    ['Harry', 37.21],
    ['Berry', 37.21],
    ['Tina', 37.2],
    ['Tuli', 37.2],
    ['Akriti', 41],
    ['Shiva', 41],
    ['Harsh', 39]
]

Output:
Berry
Harry

Observation:
Multiple students can have same max score.
"""


def solution(students):
    scores = [student[1] for student in students]

    scores.sort()
    lowest = scores[0]

    # Fetch the score that is greater than the lowest
    for score in scores:
        if score > lowest:
            second_lowest = score
            break

    if not second_lowest:
        second_lowest = lowest

    # Get a list of names with the second lowest score.
    names = [student[0] for student in students if student[1] == second_lowest]

    # Sort the list of names
    return sorted(names)


if __name__ == '__main__':
    students = [
        ['Harry', 37.21],
        ['Berry', 37.21],
        ['Tina', 37.2],
        ['Tuli', 37.2],
        ['Akriti', 41],
        ['Shiva', 41],
        ['Harsh', 39]
    ]

    names = solution(students)
    for name in names:
        print(name)
