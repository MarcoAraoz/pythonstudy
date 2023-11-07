#Ejercicio 1

from tkinter import N
from unittest import result


brackets = "[[[[]]][][][]"
check = 0


for bracket in brackets:
    if bracket == "[":
        check += 1
    
    elif bracket == "]":
        check -= 1
    
    if check < 0:
        check == 0

print(check == 0)
#False


#Ejercicio 2
##Computes the sum of the first and the last digits of any integer
### 249 11

n = 249
last = n % 10

first = n

while first >= 10:
    first //= 10

result = first + last

print(result)