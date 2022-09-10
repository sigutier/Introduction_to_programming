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

unidades = input("¿Las unidades de entrada son en metros o en yardas?: ")

if unidades == "metros":
    while True:
        strlargo_m = input("¿Longitud de la habitación en metros? ")
        try:
            largo_m = float(strlargo_m)
        except:
            print("Debes introducir un número.")
            continue
        if largo_m < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    
    while True:
        strancho_m = input("¿Profundidad de la habitación en metros? ")
        try:
            ancho_m = float(strancho_m)
        except:
            print("Debes introducir un número.")
            continue
        if ancho_m < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    yarda_metro = 0.9144
    sup_metros = largo_m * ancho_m
    sup_yardas = largo_m * ancho_m / yarda_metro ** 2

    print(f"\nLongitud = {largo_m} m")
    print(f"Profundidad = {ancho_m} m")

elif unidades == "yardas":
    while True:
        strlargo_yd = input("¿Longitud de la habitación en yardas? ")
        try:
            largo_yd = float(strlargo_yd)
        except:
            print("Debes introducir un número.")
            continue
        if largo_yd < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    
    while True:
        strancho_yd = input("¿Profundidad de la habitación en yardas? ")
        try:
            ancho_yd = float(strancho_yd)
        except:
            print("Debes introducir un número.")
            continue
        if ancho_yd < 0:
            print("Debes introducir un número positivo.")
            continue
        break

    metro_yarda = 1.0936
    sup_metros = largo_yd * ancho_yd / metro_yarda ** 2
    sup_yardas = largo_yd * ancho_yd

    print(f"\nLongitud = {largo_yd} yd")
    print(f"Profundidad = {ancho_yd} yd")

print(f"\nSuperficie de la habitación en metros cuadrados: {sup_metros:.2f} m²")
print(f"Superficie de la habitación en yardas cuadradas: {sup_yardas:.2f} yd²")
