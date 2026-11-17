"""Working with dictionaries and a list of dictionaries."""

students = [
    {"name": "Kayode", "score": 50},
    {"name": "Joshua", "score": 12},
    {"name": "Chidera", "score": 30},
    {"name": "SpongeBob", "score": 80},
]

attendance_bonus = 14
for student in students:
    total = student["score"] + attendance_bonus
    print(f'{student["name"]}: {total} total points')
