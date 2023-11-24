# *args retorna argumentos almacenados en Tupla (,)

# def suma(*args: int) -> None:
#     print(type(args)) #<class 'tuple'>
#     return sum(args)

# resultado= suma(15, 30, 50)
# print(f'La suma de los elmementos es: {resultado}')


# **kwargs retorna argumentos almacenados en diccionarios

# def conectar_bd(**kwargs):
#     print(type(kwargs)) #<class 'dict'>
#     print(kwargs)

# conectar_bd(nombre_bd='generico', usuario='root', password= '123456', port=5102)
    
def conectar_bd(**kwargs):
    print(kwargs)
    nombre= kwargs.get('nombre_bd', 'default')
    user= kwargs.get('usuario', 'default')
    password= kwargs.get('password', 'default')
    port= kwargs.get('port', 'default')
    dir_bd= kwargs.get('dir_bd', 'default')
    print(f'Conectado en la BD: {nombre},\n en el puerto: {port},\n en la IP: {dir_bd}')
    
# db1= conectar_bd(nombre_bd='genérica', usuario='root', password= '123456', port=5102, randomData= '1563')
# db2= conectar_bd(nombre_bd='asdf')


#Multiples parámetros y kwargs
def suma_y_multiplicacion(p1, p2, *args):
    print(p1)
    print(p2)
    print(args)

suma_y_multiplicacion(5,6,1,2,3,4,5)