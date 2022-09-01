# Repartiendo pizza
"""
Escribir un programa que sabiendo cuantas personas hay en una reunión y cuantas pizzas 
se han comprado, queriendo que cada persona tenga una porción de cada pizza. 
La pizza sólo puede dividirse en un número par de porciones.

```
¿Número de personas? 7
¿Número de pizzas? 3

7 personas con 3 pizzas
Cada persona toma 3 piezas
Sobran 3 porciones
```

Retos: 
1. Asegurar que la entrada es numerica, positiva y entera. En otro caso impedir que el usuario continue.
2. Escribir los mensajes de salida con formato singular/plural adecuado.
3. Crear un programa que diga cuantas pizzas hay que comprar preguntando personas y porciones de pizza 
que quieren tomar. Recuerda que las pizzas siempre se dividen en un número par de porciones.
"""

# Reto 1

while True:
    strPerson = input("¿Cuántas personas son? ")
    try:
        personas = int(strPerson)
    except:
        print("Debes introducir un número entero.")
        continue
    if personas <= 0:
        print("Debes introducir un número positivo y mayor que cero.")
        continue
    break

while True:
    strPizzas = input("¿Cuántas pizzas han comprado? ")
    try:
        pizzas = int(strPizzas)
    except:
        print("Debes introducir un número entero.")
        continue
    if pizzas <= 0:
        print("Debes introducir un número positivo y mayor que cero.")
        continue
    break


if personas % 2 == 1:
  porciones = personas + 1
else:
  porciones = personas

print("\n")

# Reto 2

if personas == 1 and pizzas == 1 and ((porciones * pizzas) % personas) < 1:
    print("{} persona toma {} pizza.".format(personas, pizzas))
    print("Esta persona toma {} porcion.".format(pizzas))
    print("No sobra ninguna porcion.")
elif personas == 1 and pizzas > 1 and ((porciones * pizzas) % personas) < 1:
    print("{} persona toma {} pizzas.".format(personas, pizzas))
    print("Esta persona toma {} porciones.".format(pizzas))
    print("No sobra ninguna porcion.")
elif personas > 1 and pizzas == 1 and ((porciones * pizzas) % personas) < 1:
    print("{} personas toman {} pizza.".format(personas, pizzas))
    print("Cada persona toma {} porcion.".format(pizzas))
    print("No sobra ninguna porcion.")
elif personas > 1 and pizzas == 1 and ((porciones * pizzas) % personas) == 1:
    print("{} personas toman {} pizza.".format(personas, pizzas))
    print("Cada persona toma {} porcion.".format(pizzas))
    print("Sobra {} porcion.".format((porciones * pizzas) % personas))
else:
    print("{} personas toman {} pizzas.".format(personas, pizzas))
    print("Cada persona toma {} porciones.".format(pizzas))
    print("Sobran {} porciones.".format((porciones * pizzas) % personas))

print("\n")

# Reto 3

while True:
    strPerson = input("¿Cuántas personas son? ")
    try:
        personas = int(strPerson)
    except:
        print("Debes introducir un número entero.")
        continue
    if personas <= 0:
        print("Debes introducir un número positivo y mayor que cero.")
        continue
    break

while True:
    strPorciones = input("¿Cuántas porciones quieren tomar? ")
    try:
        porciones = int(strPorciones)
    except:
        print("Debes introducir un número entero.")
        continue
    if porciones <= 0:
        print("Debes introducir un número positivo y mayor que cero.")
        continue
    break

if personas % 2 == 1:
  pizzas = personas + 1
else:
  pizzas = personas

print("Número de pizzas a comprar = {}".format(porciones))