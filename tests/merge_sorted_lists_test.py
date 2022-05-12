import pytest
from functions.merge_sorted_lists import merge_sorted_lists

def test_for_1_and_2():
    # Arrange
    l1 = [1]
    l2 = [2]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2]


def test_for_2_and_1():
    # Arrange
    l1 = [2]
    l2 = [1]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2]


def test_for_1_2_3_and_4_5_6():
    # Arrange
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2, 3, 4, 5, 6]
