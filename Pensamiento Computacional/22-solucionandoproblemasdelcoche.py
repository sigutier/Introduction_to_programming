# Solucionando problemas del coche

""" Hacer un programa que siga el siguiente arbol de decisiones para dar con el diagnóstico del problema de nuestro coche.


<img src="https://docs.google.com/uc?export=download&id=1oLZHlV8GXIT2LpkPTxOoybOCZ1lmYzQ1" height="500">

Por ejemplo:
```
¿Arranca? S
¿Suena un clic-clic? S

Entonces:
Reemplaza la batería
```

Restricciones:
1. Realiza las preguntas relevantes según las respuestas del usuario """

str_resp = input("Responde a las siguientes preguntas con S/N:\n¿Arranca? ").lower()
solucion = "El coche está bien"
if str_resp == 's':
  str_resp = input("¿Suena un clic-clic? ").lower()
  if str_resp == 's':
    solucion = "Reemplaza la batería"
  else: 
    str_resp = input("¿Se enciende el coche pero no arranca? ").lower()
    if str_resp == 's':
      solucion = "Revisa las bujías"
    else:
      str_resp = input("¿Arranca el coche y luego se cala? ").lower()
      if str_resp == 's':
        str_resp = input("¿Tiene el coche inyección de combustible? ").lower()
        if str_resp == 's':
          solucion = "Lleve el coche al taller"
        else:
          solucion = "Abre y cierra el starter"
else:
  str_resp = input("¿Están los bornes de la batería corroídos? ").lower()
  if str_resp == 's':
    solucion = "Limpia los bornes y arranca de nuevo"
  else:
    solucion = "Reemplaza los cables y arranca de nuevo"

print("Entonces:\n", solucion)


## Reto:
# Investigar sobre árboles de decisión y como codificarlo sin hacerlo a capón como arriba
class Node:
  def __init__(self, message: str, si = None, no = None):
    self.si = si
    self.no = no
    self.message = message

root_node = Node(
  "¿Arranca?",
  Node(
    "¿Suena un clic-clic?",
    Node(
      "Reemplaza la batería"
    ),
    Node(
      "¿Se enciende el coche pero no arranca?",
      Node(
        "Revisa las bujías"
      ),
      Node(
        "¿Arranca el coche y luego se cala?",
        Node(
          "¿Tiene el coche inyección de combustible?",
          Node("Lleve el coche al taller"),
          Node("Abre y cierra el starter"),
        ),
        Node(
          "El coche está bien"
        )
      ),
    ),
  ),
  Node(
    "¿Están los bornes de la batería corroídos?",
    Node("Limpia los bornes y arranca de nuevo"),
    Node("Reemplaza los cables y arranca de nuevo")
  )
)
print("Responde a las siguientes preguntas con S/N:")

current_node = root_node
while current_node.si != None and current_node.no != None:
  str_resp = input(current_node.message + ' ').lower()
  if str_resp == 's':
    current_node = current_node.si
  elif str_resp == 'n':
    current_node = current_node.no
  else:
    print("La respuesta debe ser S/N")

print(current_node.message)
