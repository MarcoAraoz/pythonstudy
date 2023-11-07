'''
Context:
There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better
than the average student in your class.

Problem:
You receive an array with your peers' test scores.
Now calculate the average and compare your score.
Return True if you're better, else False.

Note:
Your points are not included in the array of your class's points. For calculating the average point you may add your point to the given array!

PseudoCode:
-Def Function with two arguments: class_scores(list), your_scores(number).

-Sum the indexes in class_scores list: create a var to store the sum

-Calculate the average of all elements in class_scores adding(+) your_score value and divide between the number of elements(len) in.

-Compare the average result with your scores.

'''
# PseudoCode:
# -Def Function with two arguments: class_points(list), your_score(number).
def better_than_average(class_points: list=[], your_score: int=0) -> bool:
    # -Sum the indexes in class_scores list: create a var to store the sum
    sum_points = sum(class_points)
# -Calculate the average of all elements in class_scores adding(+) your_score value and divide between the number of elements(len) in.
    average = (sum_points + your_score) / (len(class_points) + 1)
# -Compare the average result with your scores.
    return your_score > average


result = better_than_average([41, 75, 72, 56, 80, 82, 81, 33], 50)
print(result)


def better_than_average(class_points, your_points):
    return your_points > (sum(class_points)/len(class_points))

###

# def better_than_average(class_points, your_points):
#     # Calcula la suma de las puntuaciones de tus compañeros.
#     total_points = sum(class_points)
#     print(total_points)
#     # Calcula el promedio sumando tu puntuación a la suma total
#     # y dividiéndolo por el número de estudiantes más uno.
#     average = (total_points + your_points) / (len(class_points) + 1)
#     print(average)
#     # Compara tu puntuación con el promedio
#     return your_points > average


# Ejemplo de uso:
# class_scores = [85, 90, 78, 92, 88]
# class_scores = [2, 3]
# your_score = 95
# your_score = 5
# result = better_than_average(class_scores, your_score)
# print(result)  # Debería imprimir True en este caso

# better_than_average([2, 3], 5)
