"""Common list operations."""

cars = ["Ford", "Tesla", "Mercedes-Benz", "BMW"]
print("First car:", cars[0])
print("Last car:", cars[-1])
print("First two:", cars[:2])

cars.append("Toyota")
cars.insert(1, "Honda")
removed = cars.pop(2)
print("Removed:", removed)
print("Updated cars:", cars)
