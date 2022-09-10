# Pintando el techo
"""
5 litros de pintura dan para pintar 100 metros cuadrados de techo. 
Teniendo esto en cuenta haz un programa que diga cuantos botes de 5 litros de pintura 
hay que comprar para pintar un techo de anchura y profundidad informada por el usuario (en metros). 
Devuelve el número de botes suficiente y por supuesto en números enteros.

```
Necesitarás 12 litros para pintar 240 metros cuadrados de techo.

Debes comprar 3 botes de pintura.
```

Restricciones:
1. Utiliza una constante para calcular la conversión botes de pintura/metros de techo.
2. Asegurate de comprar un número entero de botes de pintura suficiente (el siguiente número entero) pero no de más.

Retos:
1. Revisar que la entrada sean números positivos. Si no es así no dejar que el usuario continue.
2. Hacer el cálculo para habitación redonda.
3. Hacer el cálculo para habitación en forma de L.
"""

# 5 l -- 100 mc
# 0.05 l -- 1 mc

# Restricciones 1 y 2 y Reto 1:

litrospormetro = 0.05

while True:
    strLon = input("Ancho del techo: ")
    try:
        lon = float(strLon)
    except:
        print("Debes introducir un número entero.")
        continue
    if lon < 0:
        print("Debes introducir un número positivo.")
        continue
    break

while True:
    strProf = input("Largo del techo: ")
    try:
        prof = float(strProf)
    except:
        print("Debes introducir un número entero.")
        continue
    if prof < 0:
        print("Debes introducir un número positivo.")
        continue
    break


area = lon * prof

litros = area * litrospormetro
botes = litros // 5
botes = int(botes)

botes += 1 if litros % 5 > 0 else 0

print("Necesitarás {} litro(s) para pintar {} metros cuadrados de techo.".format(round(litros, 2), round(area, 2)))
print("Debes comprar {} bote(s) de pintura.".format(botes))


# Reto 2:

litrospormetro = 0.05

while True:
    strradio = input("Radio de la habitación: ")
    try:
        radio = float(strradio)
    except:
        print("Debes introducir un número entero.")
        continue
    if radio < 0:
        print("Debes introducir un número positivo.")
        continue
    break

pi = 3.14
areacirculo = pi * radio ** 2

litros = areacirculo * litrospormetro
botes = litros // 5
botes = int(botes)

botes += 1 if litros % 5 > 0 else 0

print("Necesitarás {} litro(s) para pintar {} metros cuadrados de techo.".format(round(litros, 2), round(areacirculo, 2)))
print("Debes comprar {} bote(s) de pintura.".format(botes))