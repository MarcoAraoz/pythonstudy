#Existen patrones de diseño

# Patrón Decorador:
## Decorar algo, es decir, agregar funcionalidad a una función.

def a_function():
    return "1+1"

value = a_function()
print(value)
# "1+1"

def another_function(func):
    #print(func,__name__, "es el nombre de la función")
    def other_function():
        val = f"El resultado de {func()} es: {eval(func())}"
        return val
    return other_function

uso_de_decorator = another_function(a_function)
print(uso_de_decorator())