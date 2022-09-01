# Imprimiendo comillas
"""
Construir un programa que pida una cita y un autor y devuelva una única cadena con la cita entre comillas y el autor.

Restricciones:
1. No usar format ni % ni fstring. Hacerlo concatenando cadenas y escapando caracteres.
"""

cita = input("Escribe una cita célebre: ")
autor = input("¿Quién es el autor? ")

print( "\"" + cita + "\", " + autor)