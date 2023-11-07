#__init__.py

#from calculator import suma, color, API_URL
from calculator import (
    suma, 
    color, 
    API_URL
)

#from calculator import API_URL as api
#import calculator

resultado = suma(1, 2)
print(resultado)
print(color)
print(API_URL)
#print(calculator.API_URL)

import requests

r = requests.get('https://api.chucknorris.io/jokes/random')
status = r.status_code
data = r.json()

print(status)
print(data)