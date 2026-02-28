import pytest
from grades import calculate_average, get_letter_grade, find_highest_grade, find_lowest_grade, count_passing

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