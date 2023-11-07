# Implementar una clase - Student - va tener cuatro propiedas
# y dos metodos
# Todos estos metodos y propiedas deberian ser publicos

from typing import Union
import math


class Student:
# 1. Implementa un constructor que inicialize
# name, phy, chem, bio
    def __init__(self, name: str, phy: Union[int, float], chem: Union[int, float], bio: Union[int, float]) -> None:
        """
        The function takes in three parameters. It then assigns the values of
        these parameters to the attributes of the same name
        """
         
        self.name = name
        self.phy = phy
        self.chem = chem
        self.bio = bio
    
# 2. Implementa un metodo total_obtained() in la clase estudiante
# que calcule el total de los resgisros estudiante
    def total_obtained(self):
        self.suma = self.phy + self.chem + self.bio
        return self.suma
    
# 3. Calcular el porcentaje si el valor total es 100 (promedio)
    def total(self):
        return self.total_obtained() / 300 * 100
    
    
mark = Student('mark', 80, 90, 40)
mark.total_obtained()

#print(mark.total_obtained())
#print(mark.total())

# name = Mark
# phy = 80
# chem = 90
# bio = 40
#obj.total_obtained() = 210
#puntaje máximo = 300

## Ejercicio 2
## Generar clase Rectangulo para saber perimetro
## y saber el area

class Rectangulo:
    
    def __init__(self, base: Union[int, float], altura: Union[int, float]) -> None:
        """
        This function takes in two numbers and sets 
        them as the base and altura of the object.
        """
        self.base = base
        self.altura = altura
        
    def perimetro(self):
        """
        return: The sum of the sides of the rectangle.
        """
        self.suma_lados = (self.base * 2) + (self.altura * 2)
        return self.suma_lados
    
    def area(self):
        self.multiply = self.base * self.altura
        return self.multiply
    
rectangulo_per = Rectangulo(12, 23)
rectangulo_per.perimetro
print(rectangulo_per.perimetro())

rectangulo_area = Rectangulo(12, 23)
rectangulo_area.area
print(rectangulo_area.area())
