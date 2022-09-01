# Cálculo de la jubilación
"""
Incorpora el año actual al programa. 
Crea un programa que cuente cuantos años faltan para tu jubilación y que te diga el año 
en que te jubilarás. Algo así:

```
¿Cuantos años tienes? 48
¿A qué edad te jubilarás? 67
Te quedan 19 años para jubilarte
Estamos en 2018, te jubilarás en 2037.
```
Restricciones:
1. Convertir las cadenas de entrada en números.
2. Obten el año actual como lo haga python (no vale ponerlo como constante en el programa).

Reto:
Maneja la situación si el programa devuelve un número negativo de modo que diga que 
ya puede jubilarse.
"""

from datetime import datetime

ahora = datetime.now()
año = ahora.year

edadActaul = int(input("¿Cuántos años tiene? "))
edadJubilacion = int(input("¿A qué edad se jubilará? "))

faltan = edadJubilacion - edadActaul
cuando = año + faltan

if(faltan < 0):
    faltan = -faltan
    print("Podría haberse jubilado hace {} año(s).".format(faltan))
elif(faltan == 0):
    print("Podría jubilarse ya.".format(faltan))
else:
    print("Le quedan {} año(s) para jubilarse.".format(faltan))
    print("Estamos en {}, se jubilará en {}.".format(año, cuando))