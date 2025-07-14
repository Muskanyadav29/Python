text = input("Enter a string: ")
letters = 0
digits = 0
special_chars = 0
for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1
    else:
        special_chars += 1
print("\nCharacter counts:")
print(f"Letters: {letters}")
print(f"Digits: {digits}")
print(f"Special characters: {special_chars}")
