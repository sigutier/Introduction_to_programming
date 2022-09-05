# Calculando el interés compuesto
""" 
Introduciremos aquí los exponentes. En préstamos o inversiones a largo plazo se suele utilizar más el interes compuesto que el simple ([diferencias entre ambos](https://youtu.be/DjS7B63QgDU)). 
Se trata ahora de escribir un programa que calcule el interés compuesto sobre un capital a lo largo del tiempo.

El programa ha de pedir el **capital inicial**, el **interes anual**, el **número de años de la inversión** y el número de veces que se calcula en interés en el año. La fórmula a aplicar es:

    A = P(1 + \frac{r}{n})^{nt}

donde 
- P es el capital inicial
- r el interes anual
- t los años que dura la inversión (o préstamo)
- n el número de veces que se acumula el interés por año (por ejemplo 12 si es mensual)
- A es la cantidad al final de la inversión,

Así, para:
- 1500 € de capital inicial
- 4,3% de interes
- 6 años de duración del préstamo 
- Se calcula el interés al trimestre (4 periodos por año)

El programa debería devolver

```
1500.00 € invertidos al 4.3% durante 6 años con 4 periodos de imposición por año se transforman en 1938.84 €
```

Restricciones:
1. El interés se introduce como % no como tanto por uno (15 en lugar de 0.15)
2. Asegurar que las cantidades en euros estén ajustadas al céntimo

Retos:
1. Impedir que el usuario siga con el proceso si no introduce valores numéricos correctos
2. Hacer una versión del programa que actúe al revés. Conociendo el tipo de interés, los años y periodos de imposición y 
    sabiendo que suma total se quiere conseguir el programa debe indicar el capital inicial a invertir. """


strCapital = input("Capital principal...........: ")
strInteres = input("Interés anual...............: ")
strAños =    input("Años de imposición..........: ")
strPeriodo = input("Periodos de imposición anual: ")

capital = float(strCapital)
interes = float(strInteres)/100
años = int(strAños)
periodo = int(strPeriodo)

final = capital *(1 + interes/periodo)**(periodo * años)

print("{:.2f} € invertidos al {:.2f}% durante {} años con {} periodos de imposición por año se transforman en {:.2f} €".format(capital, interes*100, años, periodo, final))
