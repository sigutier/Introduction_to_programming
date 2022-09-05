# Tasa autonómica

""" Construye un programa que aplique una tasa a un precio en función de donde se aplique. 
Así si la provincia en la que se aplica es 'VA' (Valencia) se debe incrementar el precio en un 5,5%. 
En otro caso no se aplicará esta tasa. La salida debe ser distinta en función de la provincia, así:
- Si el precio es 10 €

```
- Provincia = 'VA':
        El subtotal es 10.00€
        La tasa es 0.55€
        El total es 10.55€

- Provincia != 'VA':
        El total es 10.00€
```

Restricciones:
- Implementar este programa usando sólo un `if` sin usar `else`
- Las cifras en € deben estar redondeadas al céntimo
- Utiliza una sola sentencia print para dar el resultado

Retos:
1. Permitir al usuario introducir su provincia en mayúsculas, minúsculas o mixto. """

strPrecio =    input("Precio...: ")
strProvincia = input("Provincia: ")

total = float(strPrecio)
strTotal = ""

if strProvincia == 'VA':
  tasa = total * 0.055
  strTotal = "El subtotal es {:.2f}€\nLa tasa es {:.2f}€\n".format(total, tasa)
  total = total + tasa

strTotal = strTotal + "El total es {:.2f}€".format(total)
print(strTotal)
