# Centrar cadena en terminal

""" Crear una función que añada espacios por delante a una cadena hasta dejarla centrada en la terminal. 
Para ello se utilizarán como parámetros la cadena y la anchura en caracteres del terminal.

Restricciones:
- No se deben añadir espacios por detrás de la cadena

Retos:
- Controlar que los parámetros son del tipo adecuado, es decir, cadena es un string y anchura un entero. 
Utilizando la documentación de python podemos ver que se puede validar el tipo de una variable utilizando la funcion predefinida isinstance()
[ver aquí](https://docs.python.org/3/library/functions.html) """

import os

def center(string, width):
    if isinstance(string, str) == False:
        raise Exception('The "string" parameter is not be of type str')
    if isinstance(width, int) == False:
        raise Exception('The "width" parameter is not be of type int')
    
    spaces = (width - len(string)) // 2
    result = spaces * " " + string

    return result

input_string = input("Enter the string you want to center: ")
calculated_width = os.get_terminal_size().columns

print(center(input_string, calculated_width))
