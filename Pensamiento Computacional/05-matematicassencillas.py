# Operaciones aritméticas
"""
Escribe un programa que pida dos números y que devuelva su suma, resta, producto y división.

Restricciones:
Convertir las cadenas de entrada en números.
Separar convenientemente la entrada, transformación de cadena en números y salida separados.
Crea una única sentencia de salida con los saltos de línea adecuados (sólo un print).

Retos:
Controla que las entradas sean números de forma que el programa no avance si no se introduce un número.
No permitas introducir números negativos.
"""

while True:
    strnum1 = input("Ingresa primer número: ")
    try:
        num1 = float(strnum1)
    except:
        print("Error. Debes introducir un número.")
        continue
    if num1 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strnum2 = input("Ingresa segundo número: ")
    try:
        num2 = float(strnum2)
    except:
        print("Error. Debes introducir un número.")
        continue

    if num2 < 0:
        print("Debes introducir un número positivo.")
        continue
    break

print("{} + {} = {}\n{} - {} = {}\n{} * {} = {}\n{} / {} = {}\n ".format(num1, num2, num1+num2, num1, num2, num1-num2, num1, num2, num1*num2, num1, num2, num1/num2))
