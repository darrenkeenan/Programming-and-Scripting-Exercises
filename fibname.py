# Ian McLoughlin
# A program that displays Fibonacci numbers.

def fib(n):
  """This function returns the nth Fibonacci number."""
  i = 0
  j = 1
  n = n - 1

  while n >= 0:
    i, j = j, i + j
    n = n - 1
  
  return i

# Test the function with the following value.
x = 185
ans = fib(x)
print("Fibonacci number", x, "is", ans)


# My surname is Keenan
# The first letter K is number 75
# The last letter n is number 110
# Fibonacci number 185 is 205697230343233228174223751303346572685



Ord() - returns an integer representing Unicode code point for the given Unicode character.
