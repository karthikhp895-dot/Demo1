# Simple Prime Number Checker in Python

def is_prime(n):
    """Return True if n is a prime number, else False."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    # Check divisors from 3 to sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return false
    return True

# Main program
try:
    num = int(input("Enter a number: "))
    if is_prime(num):
        print(f"{num} is a prime number.")
    else:
        print(f"{num} is not a prime number.")
except ValueError:
    print("Invalid input. Please enter an integer.")
name="harsh"
