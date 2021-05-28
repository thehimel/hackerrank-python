"""
https://www.hackerrank.com/challenges/whats-your-name/problem

Input:
Ross
Taylor

Output:
Hello Ross Taylor! You just delved into python.
"""


def print_full_name(first, last):
    print(f'Hello {first} {last}! You just delved into python.')


if __name__ == '__main__':
    first_name, last_name = 'Ross', 'Taylor'
    print_full_name(first_name, last_name)
