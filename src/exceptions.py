"""
https://www.hackerrank.com/challenges/exceptions/

Given 2 numbers a and b, return z = a // b.
a, b, z are integers.

Catch the exceptions.
"""


def divide(dividend, divisor):
    """Divide dividend by divisor.

    :param str dividend: Dividend.
    :param str divisor: Divisor.
    :return: quotient or exception information.
    """
    try:
        return int(dividend) // int(divisor)
    except (ZeroDivisionError, ValueError) as exception:
        return f"{exception.__class__.__name__}: {exception}"


def test_divide():
    """Test divide."""
    assert divide('3', '1') == 3
    assert divide('3', '1') == "ZeroDivisionError: integer division or modulo by zero"
    assert divide('3', '$') == "ValueError: invalid literal for int() with base 10: '$'"
