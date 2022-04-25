#Ciclo for
for i in range(1,11):
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")


float_list = [ 2.5, 16.42, 10.77, 8.3, 34.21]
count_greater = 0

for num_float in float_list:
    if num_float > 10:
        count_greater += 1

#print(count_greater)