"""
https://www.hackerrank.com/challenges/python-string-formatting/problem

Given 2 integers start and end.
For start to end, print Decimal, Octal, Hexadecimal (capitalized), Binary representations of each number.
"""


def print_formatted(end, start=1):
    pad = len(bin(end))-2
    for num in range(start, end+1):
        print(f"{num: >{pad}} {oct(num)[2:]: >{pad}} {hex(num).upper()[2:]: >{pad}} {bin(num)[2:]: >{pad}}")


def test_print_formatted(capsys):
    print_formatted(end=16, start=15)
    captured = capsys.readouterr()
    expected = "   15    17     F  1111\n   16    20    10 10000\n"
    assert captured.out == expected
