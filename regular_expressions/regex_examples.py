"""Introductory examples using Python\'s regular-expression module."""

import re

text = (
    "Python is a general-purpose programming language. "
    "It first appeared in 1991."
)

numbers = re.findall(r"\d+", text)
print("Numbers:", numbers)

lines = "PHP is popular.\nSQL is useful.\nPython is versatile."
three_letter_starts = re.findall(r"^\w{3}", lines, flags=re.MULTILINE)
print("Three-character line starts:", three_letter_starts)

phrase = "Computer Languages"
vowels = [match.group() for match in re.finditer(r"[aeiou]", phrase, flags=re.IGNORECASE)]
print("Vowels:", vowels)
