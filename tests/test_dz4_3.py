import pytest
from dz4.dz4_3 import func


@pytest.mark.parametrize(
    ('x', 'result'),
    [
        ([1, 2, 3, 4, 5, 6, 7], True),
        ([1, 2, 3, 4, 5, 5, 6, 7], False),
        ([10, 20, 30], True),
        ("abcd", True),
        ("abcbd", False),
        ([1, 2, "a", "b", "c", "d", 3, 4], True),
        ([1, 1, "a", "b", "c", "d", 3, 4], False),
        ([1, 2, "a", "b", "c", "b", "d", 3, 4], False)
    ]
)
def test(x, result):
    assert func(x) == result