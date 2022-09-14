# Fortaleza de una contraseña

""" Crea un programa que determine la complejidad de una contraseña en base a las siguientes reglas:

1. Una contraseña muy débil contiene sólo números y su longitud es menor de 8 carácteres
2. Una contraseña  débil contiene sólo letras y su longitud es menor de 8 carácteres
3. Una contraseña es fuerte si contiene letras y al menos un número y tiene al menos 8 carácteres de longitud
4. Una contraseña es muy fuerte si tiene letras, números y caracteres especiales con al menos 8 carácteres de longitud

Restricciones:
1. Crear una función `validaPwd` que devuelva un valor que evaluado por otro programa determine si la contraseña es 
    muy débil, débil, fuerte o muy fuerte. No devuelvas una cadena, debe servir para otros lenguajes.
2. Utilizar una sentencia de salida única """

import re

# muy débil
def is_very_weak(password):
    pattern = re.compile('^[0-9]{0,8}$')
    if pattern.match(password) != None:
        return True
    else: 
        return False

# débil
def is_weak(password):
    pattern = re.compile('^[a-zA-Z]{0,8}$')
    if pattern.match(password) != None:
        return True
    else: 
        return False

# fuerte
def is_strong(password):
    pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    if pattern.match(password) != None:
        return True
    else: 
        return False

# muy fuerte
def is_very_strong(password):
    pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$")
    if pattern.match(password) != None:
        return True
    else: 
        return False

def validaPwd(password):
    if is_very_weak(password):
        print("Your password is very weak.")
    elif is_weak(password):
        print("Your password is weak.")
    elif is_strong(password):
        print("Your password is strong.")
    elif is_very_strong(password):
        print("Your password is very strong.")

input_password = input("Enter your password: ")
validaPwd(input_password)
