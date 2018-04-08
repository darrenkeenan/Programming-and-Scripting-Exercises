# Darren Keenan 2018-02-27
# Exercise 4 - Project Euler 5

# What is the smallest number divisible by 1 to 20

def divisibleby1to20(n):
  for i in range(1, 21):
      if n % i != 0:
          return False 
  return True

n = 1
while True:
     if divisibleby1to20(n):
         break
     n += 1
print(n)

# The smallest number divisible by 1 to 20 = 232792560
