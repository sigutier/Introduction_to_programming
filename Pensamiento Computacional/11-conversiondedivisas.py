# Conversión de divisas

""" Crear un programa que pase de dolares a euros. El programa pedirá la tasa de cambio de dolares a euros 
(cuantos euros se necesitan para tener un dolar). El programa debe devolver lo siguiente:
```
X dolares a una tasa de cambio de Y
Total €
```

Restricciones:
1. Asegúrate de que la entrada se redondea al centavo.
2. Utiliza una única sentencia de salida.

Retos:
1. Crea un diccionario de tasas de conversión y pregunta por paises, no por monedas. """

strDolares = input("Dolares: ")
strTasa = input("Valor de cambio Dolar a Euro: ")

dolares = round(float(strDolares), 2)
tasa = float(strTasa)

euros = round(dolares * tasa, 2)

print("{} dolares a una tasa de cambio {}\n{} €".format(dolares, tasa, euros))

