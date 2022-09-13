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

# muy debil
def es_muy_debil(password):
    pattern = re.compile('^[0-9]{0,8}$')
    if pattern.match(password) != None:
        return True
    else: 
        return False

# debil
def es_debil(password):
    pattern = re.compile('^[a-zA-Z]{0,8}$')
    if pattern.match(password) != None:
        return True
    else: 
        return False

# fuerte
def es_fuerte(password):
    pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    if pattern.match(password) != None:
        return True
    else: 
        return False

# muy fuerte
def es_muy_fuerte(password):
    pattern = re.compile("^(?=.*[A-Za-z])(?=.*\d)(?=.*[\W_])[A-Za-z\d\W_]{8,}$")
    if pattern.match(password) != None:
        return True
    else: 
        return False


def validaPwd(password):
    if es_muy_debil(password):
        print("Contraseña muy debil")
    elif es_debil(password):
        print("Contraseña debil")
    elif es_fuerte(password):
        print("Contraseña fuerte")
    elif es_muy_fuerte(password):
        print("Contraseña muy fuerte")


input_password = input("Enter your password: ")
validaPwd(input_password)
