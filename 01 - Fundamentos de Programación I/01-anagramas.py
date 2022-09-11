# Anagramas

""" Crear un programa que indique si una cadena es un anagrama de otra (mismos carácteres en orden diferente). Ejemplo

```
Primera cadena: otra
Segunda cadena: rota

"otra" y "rota" son anagramas
```

Restricciones:
1. Hacerlo con la función `esAnagrama`
2. Ambas palabras deben tener la misma longitud

Reto:
1. Hacerlo sin las facilidades de manejo de cadenas de python """

def esAnagrama(palabra1, palabra2):
    # Convertimos ambas a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()
    # Luego convertimos las cadenas a arreglos, porque vamos a ordenarlas pero es más sencillo ordenar un arreglo
    palabra1_arreglo = list(palabra1)
    palabra2_arreglo = list(palabra2)
    # Las ordenamos
    palabra1_arreglo.sort()
    palabra2_arreglo.sort()
    # Convertir de vuelta a cadena
    palabra1_ordenada = "".join(palabra1_arreglo)
    palabra2_ordenada = "".join(palabra2_arreglo)
    # Y finalmente comprobar si son iguales
    return palabra1_ordenada == palabra2_ordenada


cadena1 = "Nacionalista"
cadena2 = "Altisonancia"
es_anagrama = esAnagrama(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")

# Solicitar al usuario las cadenas
cadena1 = input("Primera palabra: ")
cadena2 = input("Segunda palabra: ")
es_anagrama = esAnagrama(cadena1, cadena2)
if es_anagrama:
    print(f"{cadena1} es anagrama de {cadena2}")
else:
    print(f"{cadena1} NO es anagrama de {cadena2}")
