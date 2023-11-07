# for n in range(2, 10):
#     # print(n)
#     for x in range(2, n):
#         print(n, x)
#         if n % x == 0:
#             # print(n,x, n%x == 0)
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         # loop fell through without finding a factor
#         print(n, 'is a prime number')
        
# number = int(input('Enter an integer: '))

# for test_factor in range(1, number+1):
#     # print(test_factor, number+1)
#     if number % test_factor == 0:
#         print(test_factor)

for i in range(1, 12):
    for j in range(1, i):
        print(i, j)
        if i * j == 28:
            print(f"Se encontró 28 ({i} * {j})")
            break  # Rompe solo el bucle interno
    else:
        # loop fell through without finding a factor
        print(i, 'is a prime number')