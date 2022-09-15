# Función que traduzca números a ordinal

""" Crear una función que tenga como parámetro un número entero y que si este está entre el 1 y el 12 (incluidos) devuelva como resultado su ordinal, es decir, `'primero'`, `'segundo'`,... `'duodécimo'`, en cualquier otro caso debe devolver una cadena vacía.

## Restricciones

- Crear el programa como un [módulo](https://colab.research.google.com/drive/1bbnwN0ADgMtjNei0EI94NqXcCA1rKz9a#scrollTo=zOpDqBcy9o1Y). 
    De forma que si se ejecuta como main muestre la tabla de las doce traducciones
- La tabla de las doce traducciones debe estar perfectamente alineada. Sirva esto como ejemplo:
```
 01 - primero
 02 - segundo
 ...
10 - décimo
11 - undécimo 
12 - duodécimo
``` """

def ordinal_numbers(num):
    if isinstance(num, int) == False:
        raise Exception('The "width" parameter is not be of type int')
    ordinals = ('', 'primero', 'segundo', 'tercero', 'cuarto', 'quinto', 'sexto', 
        'septimo', 'octavo', 'noveno', 'décimo', 'undécimo', 'duodécimo')
    if num > 0 and num <= 12:
        return ordinals[num]
    else:
        return ''

if __name__ == '__main__':
    for i in range(1,13):
        print("{:2} -> {:2}".format(i, ordinal_numbers(i)))
