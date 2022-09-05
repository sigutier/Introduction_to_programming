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

# Restricciones y Reto 1:

while True:
    strprecio1 = input("Primer precio: ")
    try:
        precio1 = float(strprecio1)
    except:
        print("Debes introducir un número.")
        continue
    if precio1 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
        strcant1 = input("Primera cantidad: ")
        try:
            cant1 = float(strcant1)
        except:
            print("Debes introducir un número.")
            continue
        if cant1 < 0:
            print("Debes introducir un número positivo.")
            continue
        break

while True:
    strprecio2 = input("Segundo precio: ")
    try:
        precio2 = float(strprecio2)
    except:
        print("Debes introducir un número.")
        continue
    if precio2 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strcant2 = input("Segunda cantidad: ")
    try:
        cant2 = float(strcant2)
    except:
        print("Debes introducir un número.")
        continue
    if cant2 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strprecio3 = input("Tercer precio: ")
    try:
        precio3 = float(strprecio3)
    except:
        print("Debes introducir un número.")
        continue
    if precio3 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strcant3 = input("Tercera cantidad: ")
    try:
        cant3 = float(strcant3)
    except:
        print("Debes introducir un número.")
        continue
    if cant3 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

subtotal = 0
subtotal += precio1*cant1
subtotal += precio2*cant2
subtotal += precio3*cant3

tasa = subtotal * 0.055

total = subtotal + tasa

print("Subtotal: {}".format(subtotal))
print("Tasas: {}".format(tasa))
print("Total: {}".format(total))


# Reto 2:

lista_compras = []

while True:
    strprecio = input("Precio: ")
    if strprecio == "":
        break
    try:
        precio = float(strprecio)
        if precio < 0:
            print("Debes introducir un número positivo.")
            continue
        while True:
            strcant = input("Cantidad: ")
            try:
                cant = float(strcant)
                if cant < 0:
                    print("Debes introducir un número positivo.")
                    continue
                compra = {'precio':precio, 'cantidad':cant}
                lista_compras.append(compra)
                break
            except:
                print("Debes introducir un número.")
                continue
    except:
        print("Debes introducir un número.")
        continue

print(lista_compras)

subtotal = 0
for compra in lista_compras:
    subtotal +=  compra['precio'] * compra['cantidad']


tasa = subtotal * 0.055

total = subtotal + tasa

print("Subtotal: {}".format(subtotal))
print("Tasas: {}".format(tasa))
print("Total: {}".format(total))
