import csv
#from encodings import utf_8
import pprint

# Reading the csv file and printing the title and id of each course.
with open("catalog.csv", encoding= "utf_8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    courses = []
    for row in csv_reader:
        courses.append({
            "title": row["CPNT_TITLE"],
            "id": row["CPNT_ID"]
        })

# Reading the csv file and printing the student and id of each course.
with open("complete.csv", encoding= "utf_8") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    users = []
    for row in csv_reader:
        users.append({
            "student": row["STUD_ID"],
            "id": row["CPNT_ID"]
        })

# Replacing the id of the course with the title of the course.
for user in users:
    for course in courses:
        if user['id'] == course['id']:
            user['id'] = course['title']

lista_resultados = []

# Grouping the students by their id.

from itertools import groupby
groups = []
uniquekeys = []
for k, g in groupby(
    # Sorting the users by their student id.
    sorted(users, key=lambda x: x["student"]),
lambda x: x["student"]
):
    groups.append(list(g))
    uniquekeys.append(k)
# Creating a dictionary with the student as the key 
# and the courses as the value.
new_dict = {str(i): j for i, j in zip(uniquekeys, groups)}

# Iterating through the dictionary 
# and assigning the value of each key to the variable list_dict.
for k in new_dict:
    list_dict = new_dict[k]
    key_items = []

# Deleting the student key from the dictionary 
# and appending the id key to the list key_items.
    for i in list_dict:
        del i["student"]
        key_items.append(i["id"])
        del i["id"]
# Assigning the value of the key_items list to the key k
# of the new_dict dictionary.
    new_dict[k] = key_items
    
# Creating a new dictionary with the student 
# as the key and the courses as the value.
resultado = []
for user_key in new_dict.keys():
    resultado.append(
        {"email": user_key,
         "courses": new_dict[user_key]
        }
    )    

pprint.pprint(resultado)