total = 0
print("Enter 10 numbers:")
for i in range(10):
    num = float(input(f"Number {i+1}: "))
    total += num
average = total / 10
print(f"\nThe average of the 10 numbers is: {average}")
