"""Examples of common Python data types and type conversion."""

name = "Ada"
age = 21
height = 1.68
is_learning = True

print(f"Name: {name} ({type(name).__name__})")
print(f"Age: {age} ({type(age).__name__})")
print(f"Height: {height} ({type(height).__name__})")
print(f"Learning Python: {is_learning} ({type(is_learning).__name__})")

# input() returns text, so convert it when a number is needed.
number_text = "42"
number = int(number_text)
print(f"Converted number plus 8: {number + 8}")
