Several versions are provided below, each with different efficiency trade-offs.

**Version 1: Basic (Inefficient for large numbers)**

This version is straightforward and easy to understand.  It's efficient for smaller numbers but becomes slow for very large numbers.

```python
def is_prime(n):
  """Checks if a number is a prime number. Inefficient for large numbers."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  i = 5
  while i * i <= n:
    if n % i == 0 or n % (i + 2) == 0:
      return False
    i += 6
  return True

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime(num):
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")

```

**Version 2: Optimized (More efficient)**

This version incorporates optimizations to improve performance for larger numbers.

```python
import math

def is_prime_optimized(n):
  """Checks if a number is a prime number. More efficient than Version 1."""
  if n <= 1:
    return False
  if n <= 3:
    return True
  if n % 2 == 0 or n % 3 == 0:
    return False
  for i in range(5, int(math.sqrt(n)) + 1, 6):
    if n % i == 0 or n % (i + 2) == 0:
      return False
  return True

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime
if is_prime_optimized(num):
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")
```

**Version 3: Using the `sympy` library (For very large numbers)**

The `sympy` library provides highly optimized primality testing functions, ideal for very large numbers.  You'll need to install it first (`pip install sympy`).

```python
import sympy

# Get input from the user
num = int(input("Enter a number: "))

# Check if the number is prime using sympy
if sympy.isprime(num):
  print(f"{num} is a prime number")
else:
  print(f"{num} is not a prime number")
```

Choose the version that best suits your needs based on the expected size of the numbers you'll be testing.  For most everyday purposes, Version 2 offers a good balance of readability and efficiency.  For extremely large numbers, Version 3 using `sympy` is recommended.  Version 1 is primarily for illustrative purposes to show a simpler, less efficient approach. Remember to handle potential errors like non-integer inputs in a production environment.