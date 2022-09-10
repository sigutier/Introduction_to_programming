# IVA general por paises

""" Según el pais se aplica un tipo general de IVA u otro. Haz un programa que aplique el tipo de iva adecuado según el pais de origen.

Seguir la siguiente [tabla](https://getquipu.com/blog/wp-content/uploads/2014/08/Artboard-asypv.png). 
El programa debe mostrar la base, el iva aplicado en % y en € y el precio final.

Restricciones:
1. Las cantidades en € deben aparecer ajustadas al céntimo
2. Utilizar una sola instrucción de impresión de resultados """

from utils import ask_float

ivas = {
    "hungria": 27,
    "croacia": 25,
    "dinamarca": 25,
    "suecia": 25,
    "finlandia": 24,
    "rumania": 24,
    "grecia": 23,
    "irlanda": 23,
    "polonia": 23, 
    "portugal": 23,
    "eslovenia": 22,
    "italia": 22,
    "españa": 21,
    "belgica": 21,
    "letonia": 21,
    "lituania": 21,
    "paises bajos": 21,
    "republica checa": 21,
    "austria": 20,
    "bulgaria": 20,
    "eslovaquia": 20,
    "estonia": 20,
    "francia": 20,
    "reino unido": 20,
    "alemania": 19,
    "chipre": 19,
    "malta": 18,
    "luxemburgo": 19
}

pais = input("País de origen: ").lower()
precio = ask_float("Precio: ")

if ivas.get(pais):
  iva = precio * ivas[pais]/100
else:
  iva = 0
  
total = precio + iva

print("Base: {:0.2f}€\nIVA: {}% - {:0.2f}€\nTotal: {:0.2f}€".format(precio, ivas[pais], iva, total) if ivas.get(pais) else "País desconocido")
