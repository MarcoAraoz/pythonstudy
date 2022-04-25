#Encontrar el promedio de los valores en una lista
# [1,4,9,10,23]
# 9.4



# lista = [1,4,9,10,23]
# suma = sum(lista)/len(lista)
# print(suma)

#Excercise 2
#Remover una sublista de una lista
l1= [1,4,9,10,23]
l2= [4,9]
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



