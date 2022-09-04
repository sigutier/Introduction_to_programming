# Aplicando impuestos
"""
Haz un programa que aplique un impuesto de 5,5% sobre tres precios introducidos por el usuario. 
Deben introducirse también el número de ejemplares de producto de cada precio que se compran. 
Se debe imprimir el subtotal sin tasas, la tasa y la suma de ambos.

Restricciones:
1. Manten separadas las partes de entrada, salida y proceso de tu programa.

Retos:
1. Comprobar que la entrada sea numérica e impedir continuar si no es así.
2. Permitir que el programa tenga un número indeterminado de productos y cantidades de entrada.
"""

while True:
    strprimerprecio = input("Primer precio: ")
    try:
        primerprecio = float(strprimerprecio)
    except:
        print("Debes introducir un número.")
        continue
    if primerprecio < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strsegundoprecio = input("Segundo precio: ")
    try:
        segundoprecio = float(strsegundoprecio)
    except:
        print("Debes introducir un número.")
        continue
    if segundoprecio < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strtercerprecio = input("Tercer precio: ")
    try:
        tercerprecio = float(strtercerprecio)
    except:
        print("Debes introducir un número.")
        continue
    if tercerprecio < 0:
        print("Debes introducir un número positivo.")
        continue
    break

