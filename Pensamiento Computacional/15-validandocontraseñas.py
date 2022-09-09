# Validando contraseñas

""" Se trata de crear un programa que pida usuario y contraseña y que valide si coinciden. 
En el caso de que lo hagan devolver un mensaje `Entró en el sistema` y en el contrario `No te conozco, no pasas`

Lo interesante de este programa no es sólo la estructura de if necesarias, sino también la estructura de datos necesaria para almacenar usuarios y sus contraseñas.

Restricciones:
- Utilizar `if/else`
- Hacer el programa sensible a mayúsculas - minúsculas

Retos:
1. Impide que la contraseña se vea. Investiga para ello.
2. Utiliza un diccionario en lugar de una tupla de tuplas """

import getpass

users = [
  {'user': "patata", 'password': "1234"},
  {'user': "tomate", 'password': "4567"},
  {'user': "manzana", 'password': "7890"}
]

str_user = input("User: ")
str_pwd =  getpass.getpass("Password: ")

is_user_present = False
is_password_valid = False

for user in users:
  if user['user'] == str_user:
    is_user_present = True
    if user['password'] == str_pwd:
      is_password_valid = True

if is_user_present == True and is_password_valid == True:
  print("Entró en el sistema")
else:
  print("No te conozco, no pasas")
