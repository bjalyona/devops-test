import pytest

from main import plus, minus
@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (5, 5, 10),
        (18, -5, 13),
    ]
)

def test_plus(x, y, result):
    assert plus(x, y) == result


@pytest.mark.parametrize(
    ('x', 'y', 'result'), [
        (10, 5, 5),
        (6, -5, 11),
    ]
)
def test_minus(x, y, result):
    assert minus(x, y) == result