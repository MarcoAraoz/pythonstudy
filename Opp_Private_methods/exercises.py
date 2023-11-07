# Exercise 1
# Implementa la clase Student y completa las siguienetes tareas

class Student:
# Task 1
# Implementa las siguiente propiedades privadas:
        
# name (Nombre)
# roll_number (Numero de lista)

    
    def __init__(self, name: str = None, roll_number: int = None) -> None:
        self.__name = name
        self.__roll_number = roll_number
    
    def get_name(self) -> str:
        return self.__name
    
    def set_name(self, name: str) -> None:
        self.__name = name
    
    def get_roll_number(self) -> str:
        return self.__roll_number
    
    def set_roll_number(self, roll_number: int) -> None:
        self.__roll_number = roll_number
              
# Incluye los siguientes metodos para 
# obtener y setear las propiedades privadas

## get_name()
Marco = Student('Marco', 28)
print("Before setting: ", Marco.get_name())

## set_name()
Marco.set_name('Marco Antonio')
print("After setting: ", Marco.get_name())


## get_roll_number()
print("Before setting: ", Marco.get_roll_number())

## set_roll_number()
Marco.set_roll_number(29)
print("After setting: ", Marco.get_roll_number())