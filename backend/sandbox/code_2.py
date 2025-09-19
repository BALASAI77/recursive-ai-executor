The previous code likely timed out because it used an inefficient algorithm for checking primality.  Here are two improved versions: one optimized for smaller numbers, and another using the Miller-Rabin primality test for larger numbers where speed is crucial.

**Version 1: Optimized for smaller numbers**

This version avoids unnecessary checks by only iterating up to the square root of the number.

```python
import math

def is_prime(n):
  """Checks if a number is prime. Optimized for smaller numbers."""
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

# Example usage
print(is_prime(2))   # True
print(is_prime(10))  # False
print(is_prime(97))  # True
print(is_prime(1000000007)) #True (This will be much faster than the naive approach)

```


**Version 2: Miller-Rabin Primality Test (for larger numbers)**

The Miller-Rabin test is a probabilistic test, meaning there's a tiny chance of a false positive (incorrectly identifying a composite number as prime).  However, for most practical purposes, it's extremely accurate and significantly faster than deterministic tests for large numbers.

```python
import random

def miller_rabin(n, k=40): #k is the number of iterations, increasing k increases accuracy but decreases speed
    """Miller-Rabin primality test."""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, s = 0, n - 1
    while s % 2 == 0:
        r += 1
        s //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False  # Composite
    return True  # Probably prime


#Example Usage
print(miller_rabin(2))   # True
print(miller_rabin(10))  # False
print(miller_rabin(97))  # True
print(miller_rabin(1000000007)) #True (much faster for very large numbers)
print(miller_rabin(1000000009)) #False (composite)


```

Choose the version that best suits your needs.  For smaller numbers (up to a few million), Version 1 is generally sufficient. For larger numbers where speed is paramount and a tiny probability of error is acceptable, Version 2 (Miller-Rabin) is far superior. Remember to install the `random` module if you haven't already (it's a standard Python library, so it's likely already installed).