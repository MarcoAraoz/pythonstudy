#Scopes
animal= 'León' #Variable Global -> Tiene alcance en todo el programa y puede ser usada en Bloques(Funciones, Ciclos, Condiciones, etc.)

def print_animal():
    global animal
    animal='Ballena'
    
    animal='Cocodrilo' #Variable Local -> Su alcance es de únicamente de Bloque
    print(animal)
    print(id(animal)) #Cocodrilo 1801416390064
    
print_animal()
print(animal)
print(id(animal)) #Cocodrilo 1801416390064