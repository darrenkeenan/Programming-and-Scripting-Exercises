# Darren Keenan 2018-02-10
# Exercise 3 - Collatz

n = 17

while n != 1:
    if n % 2 == 0:
        n = n // 2
        print(n)
    elif n % 2 == 1:
        n = n * 3 + 1
        print(n) 

        
