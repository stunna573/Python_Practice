"""Handling common errors and defining a custom exception."""


class InvalidMarksError(ValueError):
    """Raised when a mark is outside the allowed range."""


def calculate_average(first_mark, second_mark):
    """Calculate the average of two marks from 0 to 100."""
    for mark in (first_mark, second_mark):
        if not 0 <= mark <= 100:
            raise InvalidMarksError("Marks must be between 0 and 100.")
    return (first_mark + second_mark) / 2


def safe_divide(numerator, denominator):
    """Divide two numbers, raising a clear error for a zero denominator."""
    if denominator == 0:
        raise ZeroDivisionError("The denominator cannot be zero.")
    return numerator / denominator


if __name__ == "__main__":
    try:
        print("Average:", calculate_average(78, 86))
        print("Division:", safe_divide(10, 2))
    except (InvalidMarksError, ZeroDivisionError) as error:
        print("Could not complete calculation:", error)
    else:
        print("Calculations completed successfully.")
    finally:
        print("Example finished.")
