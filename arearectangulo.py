# Área de un rectángulo
"""
Pide la entrada del largo(longitud) y ancho(profundidad) de la habitación en metros. 
Devuelve la superficie en metros cuadrados y en yardas cuadradas 
(tomando la referencia de [aquí](https://es.wikipedia.org/wiki/Sistema_anglosaj%C3%B3n_de_unidades)).
'''
¿Longitud de la habitación en metros? 20
¿Profundo de la habitación en metros? 10
Superficie de la habitación en metros cuadrados: 200.0
Superficie de la habitación en yardas cuadradss: 167.225472
'''

Restricciones:
1. Mantener los cálculos separados de la salida.
2. Usa una constante para las conversiones de unidades 
([aquí](https://es.wikipedia.org/wiki/Sistema_anglosaj%C3%B3n_de_unidades))

Retos:
1. Fuerza a que las entradas sean numéricas. Si no son numericas el usuario no podrá continuar.
2. Crea una versión del programa que permita elegir si la entrada va en metros o en yardas.
"""


while True:
    strlargo = input("¿Longitud de la habitación en metros? ")
    try:
        largo = float(strlargo)
    except:
        print("Debes introducir un número.")
        continue
    if largo < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strancho = input("¿Profundidad de la habitación en metros? ")
    try:
        ancho = float(strancho)
    except:
        print("Debes introducir un número.")
        continue
    if ancho < 0:
        print("Debes introducir un número positivo.")
        continue
    break


yarda_metro = 0.9144
sup_metros = largo * ancho
sup_yardas = largo * ancho / yarda_metro ** 2

print(f"\nLongitud = {largo} m")
print(f"Profundidad = {ancho} m")
print(f"\nSuperficie de la habitación en metros cuadrados: {sup_metros} m²")
print(f"Superficie de la habitación en yardas cuadradas: {sup_yardas} yd²")
