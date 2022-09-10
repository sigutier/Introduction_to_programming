# De número a mes

""" Hacer un programa que traduzca los números del 1 al 12 a los meses del año. Hacerlo con if - elif.

Restricciones:
1. Dejar una única instrucción de salida

Retos:
1. Sustituir la selección con una estructura de datos complejos
2. Hacer el mismo programa en más de un idioma (a elegir por el usuario) """

from utils import ask_int

numero_mes = ask_int("Mes número: ")

if numero_mes == 1:
  mes = "Enero"
elif numero_mes == 2:
  mes = "Febrero"
elif numero_mes == 3:
  mes = "Marzo"
elif numero_mes == 4:
  mes = "Abril"
elif numero_mes == 5:
  mes = "Mayo"
elif numero_mes == 6:
  mes = "Junio"
elif numero_mes == 7:
  mes = "Julio"
elif numero_mes == 8:
  mes = "Agosto"
elif numero_mes == 9:
  mes = "Septiembre"
elif numero_mes == 10:
  mes = "Octubre"
elif numero_mes == 11:
  mes = "Noviembre"
elif numero_mes == 12:
  mes = "Diciembre"
else:
  mes = "Desconocido"

print(mes)


# Retos
numero_mes = ask_int("Mes número: ")
idioma = input("Elige un idioma (español/ingles): ").lower()
meses = [['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre'],
    ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']]

if numero_mes > 0 and numero_mes < 13:
    if idioma == "español":
        print(meses[0][numero_mes - 1])
    elif idioma == "ingles":
        print(meses[1][numero_mes - 1])
else:
    print("Mes desconocido")
