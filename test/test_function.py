from functions import sum

def test_sum():
    assert sum(1, 2) == 3
    assert sum(3.14, 2.71) == 5.85
    assert sum(-1, 1) == 0
    assert sum(0, 0) == 0
    assert sum(10, -5) == 5
    assert sum(-10, 5) == -5
    assert sum(1.5, 2.5) == 4.0
    assert sum(-1.5, -2.5) == -4.0
    assert sum(1e10, 2e10) == 3e10
    assert sum(-1e10, -2e10) == -3e10
    assert sum(1e-10, 2e-10) == 3e-10
    