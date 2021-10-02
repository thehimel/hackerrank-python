"""
https://www.hackerrank.com/challenges/incorrect-regex/

Print True if the string is a valid regex, else print False.
"""

import re


def regex(pattern):
    """Check the pattern.

    :param str pattern: Pattern to check.
    :return bool
    """
    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


def test_regex():
    """Test regex."""
    assert regex("") is True
    assert regex("_._") is True
    assert regex(".*\\+") is True
    assert regex(".*+") is False
