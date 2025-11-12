from rozwiązania.lab5_przed import subset as max_subarray


def test_max_subarray_empty_numbers():
    assert max_subarray([], 5) == 0


def test_max_subarray_count_zero():
    assert max_subarray([1, 5, 6], 0) == 0


def test_max_subarray_count_equals_numbers_len():
    assert max_subarray([1, 5, 6], 3) == 12


def test_max_subarray_count_greater_than_numbers_len():
    assert max_subarray([1, 5, 6], 4) == 12


def test_max_subarray_substring_at_begining():
    assert max_subarray([2, 5, 1, 3, 2, 1, 1, 4, 2, 1, 1], 4) == 11


def test_max_subarray_substring_at_end():
    assert max_subarray([2, 2, 1, 3, 2, 1, 1, 4, 2, 5, 3], 2) == 8


def test_max_subarray_substring_in_middle():
    assert max_subarray([2, 5, 1, 3, 2, 6, 3, 4, 2, 1, 1], 5) == 18
