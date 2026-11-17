"""Product-related helper functions."""


def product_message(name, quantity):
    """Return a readable message about a product quantity."""
    if quantity < 0:
        raise ValueError("Quantity must not be negative.")
    return f"{name} has been added with {quantity} items."
