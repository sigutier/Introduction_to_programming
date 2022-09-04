# Concatenando cadenas
"""
Crear un programa que pida nombre, verbo, adverbio y adjetivo y con ellos construya una historia. 
Utilizar una plantilla con los huecos donde colocar el nombre, el verbo, el adverbio y el adjetivo. 
Eligiendo bien la plantilla la frase puede resultar absurda y hasta graciosa.

Restricciones:
1. Utilizar un solo print en el programa.
2. Hacer una versión utilizando sustitucion.

Retos:
1. Introducir más datos para complicar y aumentar la historia
2. Construye una historia del estilo de los libros de *Construye tu propia aventura* 
    de forma que la historia derive según se elija una u otra opción.
"""

# Sin función de sustitución

historia = "Mi 0 1 debe 2 3."

nombre = input("Introduce un nombre: ")
verbo =  input("Introduce un verbo: ")
adjetivo =  input("Introduce un adjetivo: ")
adverbio =  input("Introduce un adverbio: ")

i = 0
frase = ""

while i < len(historia):
  car = historia[i]
  
  if car == "0":
    frase = frase + nombre
  elif car == "1":
    frase = frase + adjetivo
  elif car == "2":
    frase = frase + verbo
  elif car == "3":
    frase = frase + adverbio
  else:
    frase = frase + car
    
  i = i + 1

print(frase)


# Usando format

historia = "Mi {} {} debe {} {}."

nombre = input("Introduce un nombre: ")
verbo =  input("Introduce un verbo: ")
adjetivo =  input("Introduce un adjetivo: ")
adverbio =  input("Introduce un adverbio: ")

print(historia.format(nombre, adjetivo, verbo, adverbio))



# Retos

print("CREA TU HISTORIA LOCA")

modo = input("¿Quires una historia corta o larga? ")

if modo == "corta":
  historia = "Mi {} {} debe {} {}."
  print("Ingresa las palabras que te solicitamos a continuación:\n") 

  nombre = input("Nombre: ")
  verbo =  input("Verbo: ")
  adjetivo =  input("Adjetivo: ")
  adverbio =  input("Adverbio: ")

  print("\nESTA ES LA HISTORIA QUE HAS CREADO:")
  print(historia.format(nombre, adjetivo, verbo, adverbio))

elif modo == "larga":
  print("Ingresa las palabras que te solicitamos a continuación:\n") 
  pal1 = input("Emoción: ")
  pal2 = input("Color: ")
  pal3 = input("Tiempo: ")
  pal4 = input("Ropa: ")
  pal5 = input("Adjetivo en plural: ")
  pal6 = input("Calzado en plural: ")
  pal7 = input("Verbo: ")

  print("\nESTA ES LA HISTORIA QUE HAS CREADO:")
  print(f"Un día me levanté y me sentía {pal1}, y sabía que iba a ser un día especial.")
  print(f"El cielo era {pal2} y el clima era {pal3}, por lo que salí de la cama,")
  print(f"me puse mi {pal4} y mis {pal5} {pal6}, y estaba listo para {pal7}.")