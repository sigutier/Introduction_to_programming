# Validando contraseñas

""" Se trata de crear un programa que pida usuario y contraseña y que valide si coinciden. 
En el caso de que lo hagan devolver un mensaje `Entró en el sistema` y en el contrario `No te conozco, no pasas`

Lo interesante de este programa no es sólo la estructura de if necesarias, sino también la estructura de datos necesaria para almacenar usuarios y sus contraseñas.

Restricciones:
- Utilizar `if/else`
- Hacer el programa sensible a mayúsculas - minúsculas

Retos:
1. Impide que la contraseña se vea. Investiga para ello
2. Utiliza un diccionario en lugar de una tupla de tuplas """

usuarios = (
    ("patata", "1234"),
    ("tomate", "4567"),
    ("manzana", "7890"),
)

strUser = input("User....: ")
strPwd =  input("Password: ")

ix = 0
while ix < len(usuarios) and usuarios[ix][0] != strUser:
  ix += 1
    
if ix == len(usuarios):
  print("No te conozco, no pasas")
else:
  if usuarios[ix][1] == strPwd:
    print("Entró en el sistema")
  else: 
    print("No te conozco, no pasas")
