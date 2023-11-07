#POO
# OBJETO, es algo que tiene comportamientos 
# y datos asociados (propiedades y métodos)

# Persona
##Propiedades: Datos (Edad, Nombre, Ciudad, color de piel, estatura) -> Informacion
##Métodos: Comportamientos (Despierta, Come, Paga impuestos) -> Acciones


#CLASES
# Creacion - Instancia - Destruccion
class ClassName:
    pass

#OBJETOS instanciados
a = ClassName()
b = ClassName()


class Employee:
    ID = 353545
    salary = 2500
    department = "Recursos Humanos"

empleado = Employee()
print(empleado.ID)
print(empleado.salary)
print(empleado.department)

empleado_2 = Employee()
empleado_2.ID = 43434
empleado_2.salary =400
empleado_2.department = "tech"
print(empleado_2.ID)
print(empleado_2.salary)
print(empleado_2.department)

empleado_3 = Employee()
empleado_3.date_birth = "1995-04-23"
empleado_3.salary = 4545
print(empleado_3.date_birth)
print(empleado_3.salary)