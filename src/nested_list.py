"""
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
    scores = []
    for student in students:
        scores.append(student[1])

    scores.sort()
    lowest_score = scores[0]

    # Fetch the score that is greater than the lowest_score
    for score in scores:
        if score > lowest_score:
            second_lowest_score = score
            break

    if not second_lowest_score:
        second_lowest_score = lowest_score

    # Get a list of names with the second lowest score.
    names = []
    for student in students:
        name = student[0]
        score = student[1]
        if score == second_lowest_score:
            names.append(name)

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
