# Hola, mundo
"""
Hacer un programa que pida el nombre y te salude por tu nombre.

Restricciones:
Mantener entrada, salida y concatenación separados.

Retos:
1. Escribir el programa sin usar variables.
2. Escribir un programa que devuelva diferentes tipos de saludos a diferentes tipos de persona.
"""

nombre = input("¿Cómo te llamas? ")
saludo = "Hola, " + nombre + "!"
print(saludo)



# RETO 1

print("Hola, " + input("¿Cómo te llamas? ") + ". ¿Cómo estás?")



# RETO 2

import random
saludos = ("Hola,", "Buenas,", "¿Qué tal?,", "¿Qué pasa?,")

nombre = input("¿Cómo te llamas? ")

nSaludo = random.randint(0,3)

print(saludos[nSaludo], nombre)
