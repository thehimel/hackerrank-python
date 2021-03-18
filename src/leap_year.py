""""
https://www.hackerrank.com/challenges/write-a-function

Write a function to find if a year is leap year.
"""


def is_leap(year):
    return year % 4 == 0 and (
        year % 100 != 0 or (year % 100 == 0 and year % 400 == 0))


assert is_leap(1990) is False
assert is_leap(2004) is True
assert is_leap(2008) is True
assert is_leap(2024) is True
assert is_leap(2036) is True
assert is_leap(2038) is False
assert is_leap(2000) is True

# year = int(input())
# print(is_leap(year=year))
