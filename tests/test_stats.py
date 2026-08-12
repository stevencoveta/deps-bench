import pytest

from deps_test.stats import moving_average


def test_basic_window():
    assert moving_average([1, 2, 3, 4], 2) == [1.5, 2.5, 3.5]


def test_window_of_one_is_identity():
    assert moving_average([5, 6, 7], 1) == [5, 6, 7]


def test_full_window():
    assert moving_average([2, 4, 6], 3) == [4.0]


def test_invalid_window_raises():
    with pytest.raises(ValueError):
        moving_average([1, 2], 0)
