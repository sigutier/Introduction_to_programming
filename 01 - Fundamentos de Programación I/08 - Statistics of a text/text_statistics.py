# Modulo de estadísticas de un texto
""" 
Crear un módulo con las siguientes funciones:
- contarCaracteres(texto)
- contarPalabras(texto)
- contarVocales(texto)
- contarConsonantes(texto)

## Restricciones:
- Cada función devolverá el valor numérico de lo que cuenta.
- Si el módulo se ejecuta directamente (sin ser importado por otro programa deberá listar todos los valores de un texto en forma de tabla tabulada)

## Retos:
- Crear otros contadores como
  - contar signos de puntuacion fijando los mismos por ejemplo en los siguientes `.,;:¡!¿?()[]-_`
  - contar un carácter determinado con la función contar(texto, 'r') 
"""

def count_characters(text):
  return len(text)

def count_words(text):
  return len(text.split())

def count_vowels(text):
	vowels = 0
	for letter in text:
		if letter.lower() in "aeiouáéíóúàèìòùäëïöüâêîôû":
			vowels += 1
	return vowels

def count_consonants(text):
  consonants = 0
  for letter in text:
    if letter.lower() in "bcdfghjklmnñpqrstvwxyz":
      consonants += 1
  return consonants

def count_signs(text):
  signs = 0
  for letter in text:
    if letter in ".,;:¡!¿?()[]-_":
      signs += 1
  return signs

def count(text, char):
  i = 0
  for letter in text:
    if letter == char:
      i += 1
  return i

text = "Hola, mundo. ¿Como están?"

print("Characters:", count_characters(text))
print("Words:", count_words(text))
print("Vowels:", count_vowels(text))
print("Consonants:", count_consonants(text))
print("Signs:", count_signs(text))
print("Determined character:", count(text, 'o'))
