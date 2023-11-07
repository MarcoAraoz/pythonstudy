'''
-Crear clase con nombre
-Crear constructor con el nombre de la clase instanciada y almacenada en una variable
-Añadir Atributos de la clase
'''

# Crear clase con nombre.


class Personaje:
    # Añadir Atributos (variables) de la clase (ABSTRACCIÓN)
    nombre = 'default'
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    # Añadir método constructor
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    # Estado del objeto
    def estadoDelObjeto(self):
        print("\n{} cuenta con \n{} de fuerza,\n{} de inteligencia,\n{} de defensa, \n{} puntos de vida".format(
            self.nombre, self.fuerza, self.inteligencia, self.defensa, self.vida))

    # Definición de Métodos
    def subir_nivel(self, fuerza: int = 0, inteligencia: int = 0, defensa: int = 0) -> int:
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + defensa

    def esta_vivo(self):
        return self.vida > 0

    def morir(self):
        self.vida = 0
        print(self.nombre, 'ha muerto')

    def daño(self, enemigo):
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        daño = self.daño(enemigo)
        enemigo.vida = enemigo.vida - daño
        
        print(self.nombre, "ataca a", enemigo.nombre,
              "y le hace", daño, "de daño")
        if enemigo.esta_vivo():
            print('La vida de', enemigo.nombre, 'es:', enemigo.vida)
        else:
            enemigo.morir()


# Crear variable para almacenar el método
# constructor de la clase instanciada
# mi_personaje = Personaje('Toth', 10, 1, 5, 100)
# print(mi_personaje.nombre)
# print(mi_personaje.defensa)
# mi_personaje.estadoDelObjeto()

# mi_personaje.subir_nivel(10, 1, 5)
# mi_personaje.estadoDelObjeto()

# print(mi_personaje.esta_vivo())

# mi_personaje.morir()
# mi_personaje.estadoDelObjeto()

# mi_personaje = Personaje('Or', 10, 1, 5, 100)
# mi_enemigo = Personaje('Janos', 8, 5, 3, 5)
# mi_personaje.estadoDelObjeto()
# mi_enemigo.estadoDelObjeto()
# print(mi_personaje.daño(mi_enemigo))

# mi_personaje.atacar(mi_enemigo)
# mi_enemigo.estadoDelObjeto()


# Clase guerrero creada y con Herencia de la Superclase Personaje
class Guerrero(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):

        # The line `super().__init__(nombre, fuerza, inteligencia, defensa, vida)` is calling the
        # constructor of the superclass (Personaje)
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada

    def cambiar_arma(self):
        opcion = int(input(
            'Elige un arma: \n (1) Acero Valyrio, Daño 8. \n (2) Matadragones, Daño 10\n').strip())
        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print('Arma no existente, elije de nuevo!')

    def estadoDelObjeto(self):
        super().estadoDelObjeto()
        print('{} de espada'.format(self.espada))

    def daño(self, enemigo):
        return self.fuerza*self.espada - enemigo.defensa


# guts = Guerrero('Guts', 20, 10, 10, 100, 5)
# guts.cambiar_arma()
# guts.estadoDelObjeto()
# print(guts.espada)
# guts.daño(mi_personaje)
# print(mi_personaje.defensa)


class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    def estadoDelObjeto(self):
        super().estadoDelObjeto()
        print('{} de libro mágico'.format(self.libro))
    
    def daño(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa
    
def combate(jugador_1, jugador_2):
    turno = 0
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print("\nTurno", turno)
        print(">>> Acción de ", jugador_1.nombre,":", sep="")
        jugador_1.atacar(jugador_2)
        print(">>> Acción de ", jugador_2.nombre,":", sep="")
        jugador_2.atacar(jugador_1)
        turno = turno + 1
    if jugador_1.esta_vivo():
        print("\nHa ganado", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("\nHa ganado", jugador_2.nombre)
    else:
        print("\nEmpate")
        
jugador= Personaje('Jugador', 20, 15, 10, 100)
gamb= Guerrero('Gamb', 20, 10, 4, 100, 4)
magus = Mago('Magus', 5, 15, 4, 100, 3)
# jugador.atacar(gamb)
# gamb.atacar(magus)
# magus.atacar(jugador)
# jugador.estadoDelObjeto()
# gamb.estadoDelObjeto()
# magus.estadoDelObjeto()

combate(gamb, magus)
