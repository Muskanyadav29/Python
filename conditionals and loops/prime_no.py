print("Prime numbers between 1 and 100:")

for num in range(2, 101):  # Start from 2 since 1 is not prime
    is_prime = True        # Assume number is prime
    
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            is_prime = False
            break
    
    if is_prime:
        print(num, end=" ")
