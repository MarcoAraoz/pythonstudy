#file = open("/dog_breeds.txt")
reader = open("dog_breeds.txt")

##Cada que se abre un archivo por seguridad se
##debe indicar su cierre:

#Método 1

#try:
#   preocesar el archivo
#finally
#   reader.close()

#Método usando context

# with open('/dog_breeds.txt') as reader:
#     #procesamos el archivo
#     pass

with open("dog_breeds.txt", 'r') as reader:
    #print(reader.read())
    #print(reader.readlines())
    # lines = reader.readlines()
    # for line in lines:
    #     print(line, end="")
    dog_breeds = reader.readlines()
    
with open("dog_breeds.txt", 'w') as writer:
    for breed in reversed(dog_breeds):
        writer.write(breed)
        #print(breed)
        pass

import csv

# with open("employee_birthday.csv") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=",")
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0:
#             columns = ",".join(row)
#             print(f"los nombres de las columnas son {columns}")
#             line_count += 1
#         else:
#             print(f"\t{row[0]} works in the {row[1]} department, and was born in {row[2]}")
#             line_count += 1
# print(f"Se procesaron {line_count} lines")


with open("employee_birthday.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        #print(row)
        pass
    
import pandas as pd

df = pd.read_csv("employee_birthday.csv")
print(df)



    