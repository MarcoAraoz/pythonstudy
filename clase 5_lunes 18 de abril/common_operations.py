num_list = []
num_list.append(1)
num_list.append(2)
num_list.append(3)
#print(num_list)
##[1,2,3]

num_list = [1,2,3,4,5,6]
num_list.insert(3,98) #(indice, número)
print(num_list)
##[1,2,3,98,4,5,6]

houses = ["Griffindor", "Hufflepuff", "Ravenclaw", "Sltyherin"]
last_house = houses.pop()
#la funcion pop retorna un resultado
##Slytherin

a =houses.remove("Ravenclaw")
#la función remove no retorna los elementos eliminados

num_list = [1,2,3,4,5,6,7,8]
print(num_list[2:5])


cities = ["London", "Paris", "Los Angeles", "Berlin"]
print(cities.index("London"))

num_list = [20,40,10,50.4, 30, 100, 5]