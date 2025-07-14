base = float(input("Enter the base number: "))
exponent = int(input("Enter the exponent (non-negative integer): "))
result = 1
for _ in range(exponent):
    result *= base
print(f"{base} raised to the power of {exponent} is: {result}")
