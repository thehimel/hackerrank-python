"""
https://www.hackerrank.com/challenges/python-division/problem

Task
The provided code stub reads two integers a and b from STDIN.

Add logic to print 2 lines. The 1st line should contain the result of integer
division (//). The 2nd line should contain the result of float division (/).

No rounding or formatting is necessary.

Input Format
The first line contains the first integer, a.
The second line contains the second integer, b.

Output Format
Print the two lines as described above.

Sample Input
4
3

Sample Output
1
1.33333333333
"""

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(f'{a//b}\n{a/b}')
