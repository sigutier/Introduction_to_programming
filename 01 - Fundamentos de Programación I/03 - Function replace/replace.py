
# Crear funcion replace
""" Crear una función que tome una cadena y remplace el caracter de una posición dada por otro según la definición 

```
 myReplace(cadena, posicion, nuevoValor)
```

Restricciones:
- Teniendo en cuenta que en python una cadena es realmente una tupla de caracteres (inmutable, no se puede modificar 
    ni su longitud, ni su contenido) deberás valorar crear una nueva cadena con el resultado y devolverla.
- Crear un módulo reutilizable. Para hacerlo correctamente (incluyendo la distinción entre utilizarlo como módulo o como main 
    - no visto aún en clase - mira [aquí](https://drive.google.com/open?id=1bbnwN0ADgMtjNei0EI94NqXcCA1rKz9a))

Posible solución:
Hay varias soluciones, voy a plantear la de fuerza bruta, iterar la cadena hasta encontrar la posición y entonces modificarla. 
También se podría hacer con subcadenas (ver [aquí](https://colab.research.google.com/drive/1gAt1VSmkb-V9enz4Oqf76yYG3L0jebKC#scrollTo=AlXm72CkJcRa)) 
utilizando los accesos de python a listas y tuplas. Sería más rápido y elegante. Esa solución os la dejo a vosotros

Retos:
- Crear la función dada como solución con un for
- Crear una función que no indique la posición sino con esta firma `myReplace(cadena, viejoCaracter, nuevoCaracter)` 
    y que lo haga para todas las ocurrencias de `viejoCaracter`. """

def my_replace_index(str, position, replace_char):
    result = ""
    for i in range(0, len(str)):
        if position == i:
            result += replace_char
        else:
            result += str[i]
        
    return result

def my_replace_char(str, char, replace_char):
    result = ""
    for i in range(0, len(str)):
        if str[i] == char:
            result += replace_char
        else:
            result += str[i]
        
    return result
