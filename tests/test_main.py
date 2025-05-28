# tests/test_main.py

from main import multiply


def test_multiply_positive():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(0, 100) == 0


def test_multiply_negative():
    assert multiply(-2, 5) == -10
