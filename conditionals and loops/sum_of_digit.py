num = int(input("Enter a number: "))
num = abs(num)
digit_sum = 0
while num > 0:
    digit = num % 10        # Get the last digit
    digit_sum += digit      # Add it to the sum
    num //= 10              # Remove the last digit
print("Sum of digits:", digit_sum)
