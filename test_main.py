"""
this module tests the plus and minus functions
"""

import pytest

from main import plus, minus, multiply


@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (5, 5, 10),
        (18, -5, 13),
    ]
)
def test_plus(x, y, result):
    """test plus function"""
    assert plus(x, y) == result


@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (10, 5, 5),
        (6, -5, 11),
    ]
)
def test_minus(x, y, result):
    """test plus function"""
    assert minus(x, y) == result


@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (10, 5, 50),
        (4, 4, 16),
    ]
)
def test_multiply(x, y, result):
    """test plus function"""
    assert multiply(x, y) == result
    