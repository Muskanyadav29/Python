n = int(input("Enter the number of rows (half of the diamond height): "))
for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))
