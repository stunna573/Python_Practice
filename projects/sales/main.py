"""Demonstrate the sales helper modules."""

from projects.sales.products import product_message
from projects.sales.sales import calculate_total


if __name__ == "__main__":
    print(product_message("Rice", 50))
    print(f"Total sales: ₦{calculate_total(2500, 3):,.2f}")
