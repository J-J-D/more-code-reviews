import pytest
from functions.palindrome_number import palindrome_number

def test_returns_true_for_99():
    # Arrange
    n = 99

    # Act
    answer = palindrome_number(99)

    # Assert
    assert answer == True


def test_returns_true_for_151():
    # Arrange
    n = 151

    # Act
    answer = palindrome_number(n)

    # Assert
    assert answer == True


def test_returns_false_for_123():
    # Arrange
    n = 123

    # Act
    answer = palindrome_number(123)

    # Assert
    assert answer == False
