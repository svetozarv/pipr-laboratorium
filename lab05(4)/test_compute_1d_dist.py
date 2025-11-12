from lab5_przed import compute_1d_dist as compute_1d_dist
import pytest


def test_compute_1d_dist_the_same():
    assert compute_1d_dist(10, 2, 2) == 0


def test_compute_1d_dist_normal():
    assert compute_1d_dist(10, -3, 5) == 8


def test_compute_1d_dist_around():
    assert compute_1d_dist(11, -5, 8) == 10


def test_compute_1d_dist_border():
    assert compute_1d_dist(11, -11, 11) == 1


def test_compute_1d_dist_coordinate_out_of_range_1():
    with pytest.raises(ValueError) as e:
        compute_1d_dist(11, -12, 11)
    assert str(e.value) == "Coordinate out of range."


def test_compute_1d_dist_coordinate_out_of_range_2():
    with pytest.raises(ValueError) as e:
        compute_1d_dist(11, -2, 12)
    assert str(e.value) == "Coordinate out of range."
