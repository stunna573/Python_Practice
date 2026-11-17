"""Function definitions, arguments, and return values."""


def greet(name="Guest"):
    """Return a friendly greeting."""
    return f"Hello, {name}. Have a great day!"


def multiply(first, second, third=1):
    """Multiply two or three numbers."""
    return first * second * third


def rectangle(length, width):
    """Return the area and perimeter of a rectangle."""
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter


if __name__ == "__main__":
    print(greet())
    print(greet("Sarah"))
    print("Product:", multiply(2, 5, 4))
    area, perimeter = rectangle(5, 3)
    print(f"Area: {area}; perimeter: {perimeter}")
