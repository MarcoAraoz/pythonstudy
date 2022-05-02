#Encontrar el promedio de los valores en una lista
# [1,4,9,10,23]
# 9.4

lista = [1,4,9,10,23]
promedio = sum(lista)/len(lista)
print(promedio)

#Excercise 2
#Remover una sublista de una lista
#l1= [1,4,9,10,23]
#l2= [4,9]
#[1, 10, 23]

from typing import List

l1= [1, 4, 9, 10, 23]
l2= [4, 9]

def remove_list(list_1:List[int] ,list_2:List[int]) -> List:
    """
    Remove values from list_1 depends on list_2
    """
    for item in list_2:
        list_1.remove(item)
    return list_1
    
new_list = remove_list(l1, l2)
print(new_list)


#Crear una lista que devuelva los cuadrados de los primeros 
#10 números del rango del 1 al 10
#[1,2,3,4,5,6,7,8,9,10]
#[1,4,9,16,25,36,49,64,81,100]

def gen_cuadrados(n):
    cuadrados = []

    for number in range(1, n +1):
        cuadrados.append(number **2)
    return cuadrados

resultado = gen_cuadrados(10)
print(resultado)

#Crear una lista con todos los numeros pares 
# desde el 0 hasta el 20 y otra con los impares

def listas (n):
    pares = []
    impares = []
    
    for number in range(1, n + 1):
        if number % 2 == 0:
            pares.append(number)
        elif number % 2 != 0:
            impares.append(number)
    return(pares, impares)
     
resultado = listas(20)
print(resultado)