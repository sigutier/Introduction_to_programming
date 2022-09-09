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

def ask_price(prefix_price = ""):
    while True:
        strprice = input(prefix_price + " precio: ")
        try:
            price = float(strprice)
        except:
            print("Debes introducir un número.")
            continue
        if price < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    return price


def ask_quantity(prefix_quantity = ""):

    while True:
        str_quantity = input(prefix_quantity + " cantidad: ")
        try:
            quantity = float(str_quantity)
        except:
            print("Debes introducir un número.")
            continue
        if quantity < 0:
            print("Debes introducir un número positivo.")
            continue
        break
    return quantity


price1 = ask_price("Primer")
quantity1 = ask_quantity("Primera")

price2 = ask_price("Segundo")
quantity2 = ask_quantity("Segunda")

price3 = ask_price("Tercer")
quantity3 = ask_quantity("Tercera")


subtotal = 0
subtotal += price1 * quantity1
subtotal += price2 * quantity2
subtotal += price3 * quantity3

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
