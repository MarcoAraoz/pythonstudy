'''
John quiere configurar un panel que contenga diferentes números con LEDs.
No posee muchos LEDs y no está seguro de si él será capaz de montar el número deseado.

Considerando la configuración de los LEDs de los siguientes números, realice un algoritmo que le ayude a descubrir el número de LEDs necesarios para establecer el valor. (consultar imagen de referencia)

'''


class Leds:
    #definición de variable de clase para almecenar un
    #directorio con la clave refiriendose a los dígitos,
    #y el valor refiriendose a la cantidad de leds 
    #necesarios para formarlos
    num_leds = {
        '0': 6,
        '1': 2,
        '2': 5,
        '3': 5,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 3,
        '8': 7,
        '9': 6
    }
    
    def __init__(self, numero):
        self.numero = str(numero)
        
    def estado_del_objeto(self):
        print('numero {}'.format(self.numero))
        
    def numero_leds(self):
        """
        The function `numero_leds` calculates the total number of LEDs required to display a given number.
        :return: the total number of LEDs required to display the given number.
        """
        leds = 0
        for n in self.numero:
            leds += self.num_leds[n]
        return '{} leds'.format(leds)
    
n = int(input('ingrese un numero 1: '))

for x in range(n):
    numero = input('ingrese un numero 2: ')
    leds = Leds(n)
    leds.estado_del_objeto()
    print(leds.numero_leds())
    leds.estado_del_objeto()
