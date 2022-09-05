# Cálculo de interés simple

""" Crear un programa que calcule el interés simple, teniendo en cuenta que se calcula con la siguiente fórmula:

    A = P · (1 + rt) $

donde 'A' es la cantidad ganada, 'P' la cantidad invertida, 'r' el interes y 't' los años transcurridos desde el inicio de la inversión

```
Tras X años de inversión al Y %, su cantidad debe ser T
```


Restricciones:
1. La tasa de interés debe introducirse como porcentaje y no decimal, es decir 15 y no 0,15
2. La inversión debe redondearse al céntimo
3. La salida debe formatearse como divisa (€)

Retos:
1. Valida que las entradas sean numéricas y que el usuario no pueda continuar si no introduce un número.
2. Modifica el programa para que imprima el valor de la inversión cada año de la misma hasta llegar al valor pedido. """


strQ = input("Cantidad invertida: ")
strA = input("Años transcurridos: ")
strI = input("Interés anual: ")

Q = round(float(strQ), 2)
A = float(strA)
I = float(strI)/100

ganancia = Q * (1 + I * A)

print("Tras {} años de inversión al {:.2f}%, su cantidad debe ser {:.2f}€".format(A, I*100, ganancia))

