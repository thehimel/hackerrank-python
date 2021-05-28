"""
https://www.hackerrank.com/challenges/no-idea

Initially happiness = 0.
If your choice is in likes, increment happiness by 1.
Else if your choice is in dislikes, decrement happiness by 1.
return happiness.

Input Format:
n, m
choices
likes
dislikes

Input:
3 2
1 5 3
3 1
5 7

Output:
1
"""


def convert(destination, source):
    for item in source:
        if item.isnumeric():
            destination[item] = '_'


def solution(two, three, four):
    likes = dict()
    convert(likes, three)

    dislikes = dict()
    convert(dislikes, four)

    happiness = 0

    for choice in two:
        if choice.isnumeric():
            try:
                if likes[choice]:
                    happiness += 1
            except Exception:
                try:
                    if dislikes[choice]:
                        happiness -= 1
                except Exception:
                    pass

    return happiness


if __name__ == '__main__':
    one = '3 2'
    two = '1 5 3'
    three = '3 1'
    four = '5 7'
    print(solution(two, three, four))
