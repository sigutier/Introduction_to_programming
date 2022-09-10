# Máximo valor

""" Introduce 3 números y muestra el mayor

Restricciones:
1. Impedir continuar si no son números
2. Impedir continuar si no son todos distintos
3. Hacerlo a mano, sin utilizar funciones del lenguaje que te permitan encontrar el mayor

Retos:
1. Intentar hacerlo de manera más eficiente con funciones y estructuras de datos 
1. Modificar el programa para hacerlo con 10 números
2. Modificar el programa para hacerlo con tantos números como el usuario quiera """

from utils import ask_int_negative_included

n1 = ""
n2 = ""
n3 = ""
while n1 == "":
  n1 = ask_int_negative_included("Primer número: ")
    
while n2 == "" or n1 == n2:
  n2 = ask_int_negative_included("Segundo número: ")
    
while n3 == "" or n1 == n3 or n2 == n3:
  n3 = ask_int_negative_included("Tercer número: ")
    
max = None
if n1 > n2:
  if n1 > n3:
    max = n1
  else:
    max = n3
else:
  if n2 > n3:
    max = n2
  else:
    max = n3
    
print("El mayor es: {}".format(max))

# Retos

num = ask_int_negative_included("Escribe un número: ")
