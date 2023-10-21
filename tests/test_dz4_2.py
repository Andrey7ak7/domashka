import pytest
from dz4.dz4_2 import f


@pytest.mark.parametrize(
    ('n', 'result'),
    [
        (5, 120),
        (4, 24),
        (1, 1),
        (0, 1),
        (-5, "не существует")

    ]
)
def test(n, result):
    assert f(n) == result