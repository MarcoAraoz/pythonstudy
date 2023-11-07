# greeting = 'Hello'
# print(greeting)

users = {
    'Hans': 'active',
    'Éléonore': 'inactive',
    'Wario': 'active'
}

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

        # print(users)

# Strategy: Create a new collection
active_users = {}

for user, status in users.items():
    if status == 'active':
        active_users[user] = status
        # print(active_users)

a, b = 4, 2

if b != 0:
    # print(a/b)
    pass


# Decrementa x en 1 unidad si es mayor que cero
x = 5
x -= 1 if x > 0 else x
print(x)
