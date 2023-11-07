'''
Problem:
Given an integer, n , perform the following conditional actions:

Pseudocode:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''
# PseudoCode: Create a var n with int(), input(). Add conditionals if, else
n = int(input('Enter an integer number: ').strip())

    
# The code `if not n % 2:` checks if the remainder of `n` divided by 2 is 0. If the remainder is 0, it
# means that `n` is an even number. In this case, the code prints 'Weird'.
if not n % 2:
    print('Weird')
    # If n is even and in the inclusive range of 2 to 5, print Not Weird
elif n % 2 == 0 and 2 <= n <= 5:
    print('Not Weird')
    # If n is even and in the inclusive range of 6 to 20, print Weird
elif n % 2 == 0 and 6 <= n <= 20:
    print('Weird')
    # If n is even and greater than 20, print Not Weird
elif n % 2 == 0 and n >= 20:
    print('Not Weird')


# Verifica si un número es par o impar
x = int(input('Enter an integer number: ').strip())

# The code is checking if the remainder of `x` divided by 2 is not equal to 0. If the condition is
# true, it means that `x` is an odd number, so it prints "Es impar" (which means "It's odd" in
# Spanish). If the condition is false, it means that `x` is an even number, so it prints "Es par"
# (which means "It's even" in Spanish).
if not x % 2: #el módulo es igual a 0
    print("Even = Par")
else:
    print("Odd = Impar")