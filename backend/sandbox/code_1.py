Several ways exist to check for prime numbers in Python. Here are a few options, with varying levels of optimization:

**Option 1: Basic (Inefficient for large numbers)**

This approach checks divisibility from 2 up to `n-1`.  It's simple but slow for large numbers.

```python
def is_prime_basic(n):
  """Checks if a number is prime (basic, inefficient for large n)."""
  if n <= 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

# Example usage
print(is_prime_basic(2))   # True
print(is_prime_basic(15))  # False
print(is_prime_basic(97))  # True
```

**Option 2: Optimized (Checks up to the square root)**

A significant optimization:  We only need to check divisibility up to the square root of `n`. If a number has a divisor greater than its square root, it must also have a divisor smaller than its square root.

```python
import math

def is_prime_optimized(n):
  """Checks if a number is prime (optimized)."""
  if n <= 1:
    return False
  if n == 2:
    return True
  if n % 2 == 0:
    return False
  for i in range(3, int(math.sqrt(n)) + 1, 2):  # Only odd numbers
    if n % i == 0:
      return False
  return True

# Example usage
print(is_prime_optimized(2))   # True
print(is_prime_optimized(15))  # False
print(is_prime_optimized(97))  # True
print(is_prime_optimized(1000000007)) #True (much faster than basic for large numbers)

```

**Option 3: Using the `sympy` library (for very large numbers)**

For extremely large numbers, the `sympy` library provides highly optimized primality testing functions.

```python
import sympy

def is_prime_sympy(n):
  """Checks if a number is prime using the sympy library."""
  return sympy.isprime(n)

# Example usage
print(is_prime_sympy(2))   # True
print(is_prime_sympy(15))  # False
print(is_prime_sympy(97))  # True
print(is_prime_sympy(1000000007)) #True (very fast for even extremely large numbers)

```

Choose the option that best suits your needs.  For most everyday purposes, `is_prime_optimized` provides a good balance of speed and simplicity.  For extremely large numbers, use `is_prime_sympy`.  Avoid `is_prime_basic` unless you're dealing with very small numbers, due to its poor performance for larger inputs.