import pytest
from functions.two_sum import twoSum
import pytest
from functions.two_sum import twoSum

def test_returns_0_1_for_2_7_11_15_with_target_9():
    # Arrange
    n = [2, 7, 11, 15]
    t = 9

    # Act
    answer = twoSum(n, t)

    # Assert
    assert answer == [0, 1]


def test_returns_1_2_for_3_2_4_with_target_6():
    # Arrange
    n = [3, 2, 4]
    t = 6

    # Act
    answer = twoSum(n, t)

    # Assert
    assert answer == [1, 2]


def test_returns_0_1_for_3_3_with_target_6():
    # Arrange
    n = [3, 3]
    t = 6

    # Act
    answer = twoSum(n, t)

    # Assert
    assert answer == [0, 1]