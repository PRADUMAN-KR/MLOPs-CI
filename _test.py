import pytest


def calculate_square_and_cube(number):
    return number ** 2, number ** 3

def test_square_and_cube():
    number = 4
    expected_square = 16
    expected_cube = 64

    square, cube = calculate_square_and_cube(number)

    assert square == expected_square, f"Test Failed: Expected square of {number} to be {expected_square}, got {square}"
    assert cube == expected_cube, f"Test Failed: Expected cube of {number} to be {expected_cube}, got {cube}"
