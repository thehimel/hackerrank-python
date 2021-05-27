"""
https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

Find the runner-up score.

Input Format

The first line contains n. The second line contains an array of n integers
each separated by a space.

Input:
5
2 3 6 6 5

Output:
5

Explanation:
Given list is [2, 3, 6, 6, 5]. The maximum score is 6, second maximum is 5.
Hence, we print 5 as the runner-up score.

Observation:
There can be multiple elements with the maximum score.
Thus, only arr.sort()[-2] doesn't work.
"""


def solution(arr):
    # Sort the array in reverse order.
    arr.sort(reverse=True)

    # First element is the maximum score.
    max_score = arr[0]

    # When you find an item which is smaller than max_score
    # that is the runner-up score. And break the loop there.
    for item in arr:
        if item < max_score:
            runner_up = item
            break

    # If no item is found that is smaller than the maximum score
    # Then, runner up also got the same score.
    if runner_up is None:
        runner_up = max_score

    return runner_up


if __name__ == '__main__':
    arr = [2, 3, 6, 6, 5]
    runner_up = solution(arr)
    print(runner_up)
