# Calculando la media

""" Crear un programa que calcule la media de un conjunto de valores introducido por el usuario. Si el usuario entra 0 (cero) se considerará el final de la entrada de valores y se procederá a calcular la media. 

Restricciones:
1. El cero no se debe incluir en el cálculo de la media
2. Si el primer valor introducido es un cero el programa mostrará un mensaje de error
3. Mantener separadas la entrada, salida y proceso dentro del programa.
4. Si el valor introducido no es numérico volver a pedirlo """

list_numbers = []
is_first = True
while True:
    str_number = input("Ingresa un número: ")
    try:
        number = float(str_number)
    except:
        print("Debes introducir un número.")
        continue
    if is_first == True and number == 0:
        print("Error. Debes introducir un número diferente de cero.")
    else:
        is_first = False
        if number == 0:
            break
        else:
            list_numbers.append(number)
print(list_numbers)

def compute_mean(list):
    sum = 0
    mean = 0
    for i in range(0, len(list)):
        sum += list[i]
        
    mean = sum / len(list)
    return mean

print("La media es:", compute_mean(list_numbers))
