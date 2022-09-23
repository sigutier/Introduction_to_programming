# Listando códigos ascii

""" Crear un programa que devuelva los códigos ASCII de los carácteres desde el 32 al 127.

## Restricciones
- Formatear la salida en cuatro columnas perfectamente alineadas. 
Puedes ayudarte con [format](https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3) 
y [print](https://docs.python.org/3/library/functions.html#print)

## Retos
- Crear un modulo con una función que imprima la tabla de asciis tal cual se muestra arriba y que lo haga directamente 
si no se ejecuta desde otro programa (lo hace como main [texto del enlace]
(https://colab.research.google.com/drive/1bbnwN0ADgMtjNei0EI94NqXcCA1rKz9a#scrollTo=zOpDqBcy9o1Y)) """

def print_ascii():
    j = 0
    for i in range(32, 128):
        char = "'{}'".format(chr(i))
        if i == 127:
            char += " "
        print("{}: {:3d}".format(char, i), end='\t')
        if j % 4 == 3:
            print("")
        j += 1

if __name__ == '__main__':
    print_ascii()
