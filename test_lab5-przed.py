from lab5_przed import *
import pytest

def test_subset():
    assert subset("123456789", 3) == "789"
    assert subset("94385744444", 3) == "789"
    assert subset("94385744444", 1) == "9"
    assert subset("12345", 5) == "12345"


def test_subset_corner():
    assert subset("", 0) == 0

def test_distance():
    with pytest.raises(ValueError):
        distance(5, (6, 3), (2, 1))