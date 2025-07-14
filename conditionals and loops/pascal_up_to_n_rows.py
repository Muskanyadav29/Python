def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))
rows = int(input("Enter the number of rows for Pascal's Triangle: "))
for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(combination(i, j), end=" ")
    print()
