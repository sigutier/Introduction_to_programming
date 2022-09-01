# Contando caracteres
"""
El programa pedirá una cadena de caracteres y devolverá el número de caracteres.

Restricciones:
1. Asegurate de que devuelve la cadena original.
2. Utiliza la función específica de python para resolverlo.

Retos:
1. Si el usuario no introduce nada, el programa le conminará a que escriba algo.
2. Hazlo sin utilizar la función específica de python.

"""

# Restricciones 1 y 2

str = input("Inserta una cadena de caracteres: ")

print("La cadena '" + str + "' tiene", len(str), "caracteres.")
print("La cadena '{}' tiene {} caracteres.".format(str, len(str)))


# Retos

cadena = input("Inserta una cadena de caracteres: ")

while(cadena == ""):
    cadena = input("Debes introducir al menos un caracter: ")

str = cadena
i = 0
while(str != ""):
    str = str[1:]
    i += 1

if(i == 1):
    print("La cadena '{}' tiene {} caracter.".format(cadena, i))
else:
    print("La cadena '{}' tiene {} caracteres.".format(cadena, i))
