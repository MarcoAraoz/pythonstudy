# Find the first and last number from an INT
# n = int(input('Escriba un valor numérico: '))

# last = n % 10
# first = n

# while first >= 10:
#     first = first // 10

# print(first)
# print(last)
# print(last + first)

# Balanceo de corchetes

# brackets = input('inserte un grupo de corchetes: ')

# open_count = 0

# bracket = 0

# while bracket < len(brackets):
#     if brackets[bracket] == '[':
#         open_count += 1
#     elif brackets[bracket] == ']':
#         open_count -= 1
#     if open_count < 0:
#         break
#     bracket += 1
# if open_count == 0:
#     print('Está balanceado')
# else:
#     print('No está balanceado')

# Arbol de Asteríscos
# x = int(input('Número de asteriscos iniciales: '))
# z = int(input('Número de espacios iniciales: '))

# while z > 0:
#    # The is printing a pattern of spaces and asterisks.
#     print(' ' * z + '*' * x + ' ' * z)
#     x += 2
#     z -= 1

# Iteración en cadena de texto
# text = "Python"
# i = 0
# while i < len(text):
#     print(text[:i + 1])
#     i += 1

# Fibonacci Sequence


while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")