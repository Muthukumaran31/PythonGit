#Python - Find the factorial of a number

def factorial(n):
  """
  This function calculates the factorial of a non-negative integer.
  """
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)

# Example usage
number = 5
result = factorial(number)
print(f"The factorial of {number} is: {result}")


