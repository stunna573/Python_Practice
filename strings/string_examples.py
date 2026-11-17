"""Examples of useful string operations."""

name = "  Python Practice  "
clean_name = name.strip()

print("Original:", repr(name))
print("Trimmed:", clean_name)
print("Uppercase:", clean_name.upper())
print("Lowercase:", clean_name.lower())
print("Title case:", clean_name.title())
print("Length:", len(clean_name))
print("First character:", clean_name[0])
print("First six characters:", clean_name[:6])
print("Contains 'Practice':", "Practice" in clean_name)

language = "Python"
version = 3
print(f"{language} version {version} is being practised.")
