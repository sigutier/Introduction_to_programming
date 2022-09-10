# Indice de masa corporal

""" Craer un programa que calcule el indice de masa corporal de una persona según la fórmula 

> $ IMC = \frac{peso}{altura^2}$ 

Si el índice de masa corporal está entre 18,5 y 15 el peso se considera normal. Por encima se considera sobrepeso, por debajo delgadez.

Haz un programa que pida ambos datos, devuelva tu índice de masa corporal e indique si estás por encima o por debajo de la normalidad

Restricciones:
Impedir que el programa continúe si se introducen datos no numéricos """

from utils import ask_float

peso = ask_float("Peso(kg): ")
altura = ask_float("Altura(m): ")

imc = peso/altura**2

print("Tu índice de masa corporal es {:.2f}.".format(imc))
if imc < 15:
  print("Estas muy delgado, quizás deberías visitar a tu médico.")
elif imc > 18.5:
  print("Tienes sobrepeso, quizás deberías visitar a tu médico.")
else:
  print("Estas en tu peso ideal.")
