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
        #(["abcd", 1, 2, 3], True),
        #([]"abcbd", 1, 2, 3], False),
        #({"abcd", 1, 2, 2}, False),
        #({"abcdb", 1, 3, 3}, False)
        
    ]
)
def test(x, result):
    assert func(x) == result