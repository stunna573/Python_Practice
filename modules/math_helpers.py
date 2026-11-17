"""Small reusable mathematical helper functions."""


def find_max(first, second):
    """Return the larger of two values."""
    return first if first > second else second


def find_min(first, second):
    """Return the smaller of two values."""
    return first if first < second else second


def digit_sum(number):
    """Return the sum of the digits in a non-negative integer."""
    if number < 0:
        raise ValueError("number must be non-negative")
    return sum(int(digit) for digit in str(number))
