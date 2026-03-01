import pytest
from grades import calculate_average, get_letter_grade, find_highest_grade, find_lowest_grade, count_passing

# Happy-path-tests
def test_average():
    assert calculate_average([40, 50, 60, 70]) == 55

def test_letter_grade():
    assert get_letter_grade(55) == "P"

def test_highest_grade_is():
    assert find_highest_grade([45, 23, 88, 62]) == 88

def test_lowest_grade_is():
    assert find_lowest_grade([45, 23, 88, 62]) == 23

def test_how_many_passed():
    assert count_passing([45, 23, 88, 62], 50) == 2

# Boundary-tests
def test_get_letter_grade_hd_boundary():
    assert get_letter_grade(85) == "HD"
    assert get_letter_grade(84) == "D"
    assert get_letter_grade(75) == "D"
    assert get_letter_grade(74) == "C"
    assert get_letter_grade(65) == "C"
    assert get_letter_grade(64) == "P"
    assert get_letter_grade(50) == "P"
    assert get_letter_grade(49) == "F"

# Error/edge case tests
def test_calculate_average_empty_list():
    with pytest.raises(ZeroDivisionError):
        calculate_average([])

def test_find_highest_grade_empty_list():
    with pytest.raises(ValueError):
        find_highest_grade([])