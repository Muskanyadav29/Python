def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage:
num = int(input("Enter a number: "))
print("Sum of Digits:", sum_of_digits(num))

