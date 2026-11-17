"""Functions for basic sales calculations."""


def calculate_total(price, quantity):
    """Return the total cost for a quantity of items."""
    if price < 0 or quantity < 0:
        raise ValueError("Price and quantity must not be negative.")
    return price * quantity
