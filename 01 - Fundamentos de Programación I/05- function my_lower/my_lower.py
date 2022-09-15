# Crear funcion que convierta un texto a minúsculas

""" Crear funcion que convierta un texto a minúsculas según la definición `myLower(cadena)`

## Restricciones

- Crearla de tal manera que sólo incluya los caracteres alfabéticos
- Crearla en forma de módulo (más detalles [aquí](https://drive.google.com/open?id=1bbnwN0ADgMtjNei0EI94NqXcCA1rKz9a))

# Retos

- Validar que el parámetro sea del tipa adecuado y si no lo es gestionar el error sin que se produzca una excepción. 
Para comprobar si una variable es del tipo esperado utilizar [isinstance](https://docs.python.org/3/library/functions.html) """

def my_lower(str):
    result = ""
    for char in str:
        if ord(char) >= 192 and ord(char) <= 222: # mayusculas con tildes, diéresis, etc
            result += chr(ord(char)+32)
        elif ord(char) >= 65 and ord(char) <= 90: # mayusculas
            result += chr(ord(char)+32)
        else:
            result += char
    return result
