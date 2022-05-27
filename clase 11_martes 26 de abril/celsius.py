class Celsius:
    def __init__(self, temperature:float = 0) -> None:
        self.temperature = temperature

    def to_farenheit(self) -> float:
        return (self.temperature * 1.8) + 32

grade = Celsius(37)
#print(grade.to_farenheit())
##98.60000000000001


#Usando Getters y Setters
class Celsius:
    def __init__(self, temperature:float =0) -> None:
        self.set_temperature(temperature)

    def to_farenheit(self) -> float:
        return (self.__temperature * 1.8) + 32

    def set_temperature(self, temperature:float) -> None:
        print("Dentro de la funcion")
        if temperature < -273.15:
            raise ValueError("Temperature below -273 is not possible")
        self.__temperature = temperature

    def get_temperature(self) -> float:
        return self.__temperature

    def create_argument(self):
        self.nuevo = 111

#Instancia  - Destruye
human = Celsius(37)
print(human.get_temperature())
#37

print(human.to_farenheit())
#98.60000000000001

print(human.set_temperature(-200))
#None

print(human.get_temperature())
#-200

human.create_argument()
print(human.nuevo)
#111