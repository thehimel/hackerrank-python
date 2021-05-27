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


def solution(two, three, four):
    choices = two.split()
    likes = three.split()
    dislikes = four.split()
    happiness = 0

    for choice in choices:
        if choice in likes:
            happiness += 1
        elif choice in dislikes:
            happiness -= 1

    return happiness


if __name__ == '__main__':
    one = '3 2'
    two = '1 5 3'
    three = '3 1'
    four = '5 7'
    print(solution(two, three, four))
