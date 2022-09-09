# Conversor de temperatura

""" Crear un programa que convierta temperatura de Fahrenheita a Celsius y viceversa. El programa pedirá que tipo de conversión queremos y la mostrará.

Las fórmulas de conversión son:

>$ C = (F - 32) · \frac{5}{9} $

>$ F = (C · \frac{9}{5}) + 32 $

Restricciones:
1. Se puede elegir el tipo de conversión en mayúsculas o minúsculas
2. Reducir el número de sentencias al mínimo y no repetir prints 

Retos:
1. Asegurar que las entradas son numéricas
2. Modificar el programa para que acepte grados Kelvin """

from utils import ask_float

mode = input("Temperatura de entrada en Fahrenheit o Celsius (F/C/K)").upper()
temp = ask_float("Valor de la temperatura: ")

strOUT1 = ""
strOUT2 = ""
output1 = 0
output2 = 0

if mode == 'F':
  strIN = 'F'
  strOUT1 = 'C'
  output1 = (temp - 32) * 5/9
  strOUT2 = 'K'
  output2 = (temp - 32) * 5/9 + 273.15
elif mode == 'C':
  strIN = 'C'
  strOUT1 = 'F'
  output1 = (temp * 9/5) + 32
  strOUT2 = 'K'
  output2 = (temp + 273.15)
elif mode == 'K':
    strIN = 'K'
    strOUT1 = 'C'
    output1 = (temp - 273.15)
    strOUT2 = 'F'
    output2 = (temp - 273.15) * 9/5 + 32

print("\n{:.2f} º{} son {:.2f} º{} y {:.2f} º{}".format(temp, strIN, output1, strOUT1, output2, strOUT2))
