"""Conditional statements and branching."""

age = 20
is_student = True

if age < 18:
    discount = 0.20 if is_student else 0.10
    print(f"Junior discount: {discount:.0%}")
elif age >= 75:
    print("Senior discount")
else:
    print("Regular price")

score = 87
if score >= 70:
    print("Result: Pass")
elif score >= 50:
    print("Result: Resit")
else:
    print("Result: Fail")
