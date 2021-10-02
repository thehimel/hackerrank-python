"""
https://www.hackerrank.com/challenges/exceptions/

Given 2 numbers a and b, return z = a // b.
a, b, z are integers.

Catch the exceptions.
"""


def divide(left, right):
    """Divide left by right.

    :param str left: Dividend.
    :param str right: Divisor.
    :return: quotient or exception information.
    """
    try:
        return int(left) // int(right)
    except (ZeroDivisionError, ValueError) as exception:
        return f"{exception.__class__.__name__}: {exception}"


def test_divide():
    """Test divide."""
    assert divide('3', '1') == 3
    assert divide('3', '1') == "ZeroDivisionError: integer division or modulo by zero"
    assert divide('3', '$') == "ValueError: invalid literal for int() with base 10: '$'"
