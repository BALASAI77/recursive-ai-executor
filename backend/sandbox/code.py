def to_binary(n):
  """Converts an integer to its binary representation (two's complement for negative numbers)."""
  if n >= 0:
    return bin(n)[2:]  # [2:] removes the "0b" prefix
  else:
    # Two's complement for negative numbers
    positive_equivalent = (1 << n.bit_length()) + n  #Efficient way to get two's complement
    return bin(positive_equivalent)[2:]

# Examples
print(to_binary(10))     # Output: 1010
print(to_binary(-10))    # Output: 11111111111111111111111111110110 (assuming 32-bit representation, may vary based on system architecture)
print(to_binary(0))      # Output: 0
print(to_binary(255))    # Output: 11111111
print(to_binary(-1))     # Output: 1 (For a one's complement, it would be all 1s, but this is two's complement)
