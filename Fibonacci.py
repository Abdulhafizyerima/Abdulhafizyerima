from functools import lru_cache

@lru_cache

def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Print the nth Fibonacci number
for n in range(1, 300):
    print("The", n, "Fibonacci number is:", fibonacci(n))
