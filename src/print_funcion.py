"""
https://www.hackerrank.com/challenges/python-print/

Read integer n from STDIN.

Without using any string methods, print the following:
123...n

Note that "..." represents the consecutive values in between.

Example
Input
n = 5

Output
12345

Constraints
1 <= n <= 150


Output Format

Print the list of integers from 1 through n as a string, without spaces.

Sample Input
3

Sample Output
123
"""

if __name__ == '__main__':
    n = int(input())
    # for (i=1; i<=n; i++)
    for i in range(1, n+1):
        print(i, end='')
