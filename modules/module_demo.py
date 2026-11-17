"""Import and use functions from a local module."""

from modules.math_helpers import digit_sum, find_max, find_min


if __name__ == "__main__":
    print("Maximum:", find_max(349, 856))
    print("Minimum:", find_min(498, 596))
    print("Digit sum of 894:", digit_sum(894))
