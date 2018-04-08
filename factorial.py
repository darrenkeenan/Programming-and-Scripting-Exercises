# Darren Keenan 2018-03-20
# Exercise 6 - Factorial


def factorial(i):
    if i <= 1:
        return 1
    else:
        i = i * factorial(i - 1)
    return i

print("factorial of 5 is:", factorial(5))    
print("factorial of 7 is:", factorial(7))
print("factorial of 10 is:", factorial(10))

# factorial of 5 is 120
# factorial of 7 is 5040
# factorial of 10 is 3628800
