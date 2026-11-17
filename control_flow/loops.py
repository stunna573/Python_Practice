"""For-loop and while-loop examples."""

print("A for loop over a range:")
for number in range(1, 6):
    print(number)

print("\nA for loop over a list:")
students = ["John", "Mary", "Ali", "Reuben"]
for student in students:
    print(f"{student} is present")

print("\nA while-loop countdown:")
countdown = 3
while countdown >= 0:
    print(countdown)
    countdown -= 1
print("Finished!")
