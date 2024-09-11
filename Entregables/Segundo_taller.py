import os, string, random

# 1. Calculadora Básica: Crea una función para cada operación básica (suma, resta,
# multiplicación, división) que acepte dos argumentos y devuelva el resultado.
# Implementa una función principal que solicite al usuario números y la operación a
# realizar, utilizando las funciones creadas.

def sum(x,y):
  return x + y

def res(x,y):
  return x - y

def div(x,y):
  if y == 0:
    return 'No puedes dividir un número por 0'
  else:
    return f'La división es: {x / y}'

def mul(x,y):
  return x * y

def calculadora_basica():
  os.system('clear')
  print('Calculadora basica\n')
  print('1. suma')
  print('2. restar')
  print('3. división')
  print('4. multiplicación')
  print('0 exit')
  
  option = int(input('Ingrese una opción: '))
  
  if option == 0:
    return
  
  x = float(input('Ingrese el valor de x: '))
  y = float(input('Ingrese el valor de y: '))
  
  if option == 1:
    print('La suma es: ', sum(x,y))
  elif option == 2:
    print('La resta es: ', res(x,y))
  elif option == 3:
    print(div(x,y))
  else:
    print('La multiplicación es: ', mul(x,y))
  input('Presiona enter para continuar')

# 2. Filtrado de Lista: Desarrolla una función que reciba una lista de números y devuelva
# solo aquellos que sean pares. Utiliza un bucle y condicionales dentro de la función.

def filtrado_de_lista():
  os.system('clear')
  lista = input('Ingrese la lista (1 2 3 4 5):').split()
  for i in lista:
    if (int(i) % 2 == 0):
      print(i, 'es primo.')
  input('Presiona enter para continuar')

# 3. Transformación de Listas con Map y Lambda: Escribe un script que utilice map y una
# función lambda para convertir todas las temperaturas de una lista de grados Celsius
# a Fahrenheit.

def transf_map_lambda():
  os.system('clear')
  temperaturas = input('Ingrese la temperaturas en C° (12 14.5): ').split()
  
  nuevas_temperaturas = list(map(lambda tem: float(tem) * 9/5 + 32, temperaturas))
  
  print('Temperaturas en Fahrenheit: ', nuevas_temperaturas)
  input('Presiona enter para continuar')

# Sistema de Calificaciones: Implementa una función que reciba una lista de
# calificaciones numéricas y devuelva una lista con las calificaciones convertidas a
# letras (A, B, C, D, F) según el rango en el que se encuentren.

def convertir_notas(nota):
  nota = int(nota)
  if nota <= 1:
    return 'F'
  elif nota <= 2:
    return 'D'
  elif nota <= 3:
    return 'C'
  elif nota <= 4:
    return 'B'
  else: return 'A'

def sistema_de_calificaciones():
  os.system('clear')
  notas = input('Ingrese las notas (3.5 4.4 3): ').split()

  letras_notas = list(map(convertir_notas, notas))
  
  print('Las notas son: ', letras_notas)
  input('Presiona enter para continuar')

# Conteo de Palabras: Crea una función que reciba una cadena de texto y retorne un
# diccionario con el conteo de cuántas veces aparece cada palabra. Considera ignorar
# mayúsculas y signos de puntuación.

def quitar_signos_puntuacion(palabra):
  palabra = palabra.replace(',','')
  palabra = palabra.replace('!','')
  palabra = palabra.replace('¡','')
  palabra = palabra.replace('.','')
  palabra = palabra.replace('?','')
  palabra = palabra.replace('¿','')
  palabra = palabra.replace(':','')
  palabra = palabra.replace('"','')
  palabra = palabra.replace("'",'')
  palabra = palabra.replace('(','')
  palabra = palabra.replace(')','')
  palabra = palabra.replace('-','')
  palabra = palabra.replace('_','')
  return palabra.casefold()

def conteo_de_palabras():
  os.system('clear')
  cadena = input('Ingrese la cadena de texto: ').split()
  
  palabras = {}
  for i in cadena:
    palabra = quitar_signos_puntuacion(i)
    if palabras.get(palabra) == None:
      palabras[palabra] = 1
    else: 
      palabras[palabra] +=1
  
  print('Palabras reconocidas: ', palabras)
  input('Presiona enter para continuar')

# Función de Búsqueda: Desarrolla una función que busque un elemento dado dentro
# de una lista y devuelva su índice si lo encuentra o -1 si no está presente. No utilices
# métodos predefinidos como .index().

def buscar_elemento(lista, elemento, indice):
  for i in lista:
    if elemento == i:
      return f'El elemento {i} esta en el indice {indice}'
    indice += 1
  
  return f'El elemento {elemento} no esta, indice: -1'

def funcion_de_busqueda():
  os.system('clear')
  lista = input('Ingrese la lista (Hola 1 tres): ').split()
  elemento = input('Ingrese el elemento a buscar: ')
  
  print(buscar_elemento(lista, elemento, 0))
  input('Presiona enter para continuar')

# Validación de Paréntesis: Escribe una función que tome una cadena de solo
# paréntesis ( y ) y determine si la secuencia es válida (cada paréntesis abierto tiene un
# correspondiente paréntesis cerrado).

def validacion_de_parentesis():
  os.system('clear')
  entrada = input('Ingrese la cadena de texto: ')
  
  parentesis = 0
  for i in entrada:
    if i == '(':
      parentesis += 1
    elif i == ')':
      parentesis -= 1

    if (parentesis < 0):
      print('La secuencia de paréntesis es inválida')
      input('Presiona enter para continuar')
      return
    
  print('La secuencia de paréntesis es válida')
  input('Presiona enter para continuar')

# Ordenamiento Personalizado: Implementa una función que ordene una lista de
# tuplas (nombre, edad) primero por edad y luego por nombre (ambos en orden
# ascendente). Puedes usar la función sort o sorted con parámetros personalizados.

def ordenamiento_personalizado():
  os.system('clear')
  lista = [
    ("franki", 18),
    ("jhan", 20),
    ("juan", 15),
    ("carlos", 22),
    ("maria", 19),
    ("andres", 21),
    ("camila", 17),
    ("julian", 23),
    ("sofia", 16),
    ("daniel", 25),
    ("lucia", 18),
    ("miguel", 20),
    ("valentina", 22),
    ("diego", 24),
    ("laura", 19),
    ("sebastian", 21),
    ("carolina", 23),
    ("santiago", 18),
    ("paula", 20),
    ("alejandro", 22)
  ]
  
  lista.sort(key=lambda i: i[1])
  print('Lista ordenada por edad: ', lista)
  lista.sort(key=lambda i: len(i[0]))
  print('Lista ordenada por nombre: ', lista)
  input('Presiona enter para continuar')

# Generador de Contraseñas: Crea una función que genere una contraseña aleatoria
# que consista en una combinación de letras mayúsculas, minúsculas, números y
# símbolos. La longitud de la contraseña debe ser un parámetro de la función.

def generar_contrasenia(longitud, usar_caracteres_especiales, usar_numeros):
  caracteres = string.ascii_letters

  if usar_caracteres_especiales:
      caracteres += string.punctuation

  if usar_numeros:
      caracteres += string.digits

  contrasenia = ''.join(random.choice(caracteres) for _ in range(longitud))

  return contrasenia

def inputs():
  longitud = int(input("Ingresa la longitud de la contraseña: "))
  usar_caracteres_especiales = input("¿Quieres usar caracteres especiales? (y/n): ").lower() == 'y'
  usar_numeros = input("¿Quieres usar numeros? (y/n): ").lower() == 'y'

  return longitud, usar_caracteres_especiales, usar_numeros

def generador_de_contrasenia():
  os.system('clear')
  longitud, usar_caracteres_especiales, usar_numeros = inputs()

  contrasenia = generar_contrasenia(longitud, usar_caracteres_especiales, usar_numeros)
  print(f"Contraseña generada: {contrasenia}")

# Gestión de Agenda Telefónica: Desarrolla un programa que utilice funciones para
# permitir al usuario agregar, buscar, eliminar y mostrar todos los contactos de una
# agenda telefónica almacenada en un diccionario.

def agregar_contacto(agenda):
  nombre = input('Ingrese el nombre: ')
  telefono = input('Ingrese el número: ')
  
  if agenda.get(nombre):
    print('Nombre existente')
  else:
    agenda[nombre] = telefono
    print('Contacto agregado')
  
def eliminar_contacto(agenda):
  nombre = input('Ingrese el nombre a borrar: ')
  
  if agenda.get(nombre):
    agenda.pop(nombre)
    print('Contacto eliminado')
  
def buscar_contacto(agenda):
  nombre = input('Ingrese el nombre a buscar: ')
  
  if (agenda.get(nombre)):
    print('Contacto: ',agenda.get(nombre))
  else: print('Contacto no encontrado')

def gestion_de_agenda_telefonica():
  os.system('clear')
  agenda = {
    'franki': '3225350892',
    'carlos': '3011053762'
  }
  
  option = -1
  while option != 0:
    print('Agenda telefonica')
    print('1. Agregar contacto')
    print('2. Eliminar contacto')
    print('3. Buscar contacto')
    print('0. Exit')
    
    option = int(input('Ingrese su opción: '))
    
    if option == 1:
      agregar_contacto(agenda)
    elif option == 2:
      eliminar_contacto(agenda)
    elif option == 3:
      buscar_contacto(agenda)
    else:
      print('Opcion invalida')

# Funcion para imprimir el menu de la función principal
def menu():
  os.system('clear')
  print("1. Operaciones Básicas (Calculadora)")
  print("2. Filtrado de Lista por Números Pares")
  print("3. Conversión de Temperaturas de Celsius a Fahrenheit")
  print("4. Sistema de Calificaciones a Letras")
  print("5. Conteo de Palabras en una Cadena")
  print("6. Búsqueda de Elemento en Lista")
  print("7. Validación de Secuencia de Paréntesis")
  print("8. Ordenamiento Personalizado de Lista de Tuplas")
  print("9. Generador de Contraseñas Aleatorias")
  print("10. Gestión de Agenda Telefónica")
  print("0. Salir del Programa")

# Funcion principal
def main():
  option = -1
  while(option != 0):
    menu()
    option = int(input('Ingrese una opción: '))
    
    if option == 0:
      print('Adios')
    elif option == 1:
      calculadora_basica()
    elif option == 2:
      filtrado_de_lista()
    elif option == 3:
      transf_map_lambda()
    elif option == 4:
      sistema_de_calificaciones()
    elif option == 5:
      conteo_de_palabras()
    elif option == 6:
      funcion_de_busqueda()
    elif option == 7:
      validacion_de_parentesis()
    elif option == 8:
      ordenamiento_personalizado()
    elif option == 9:
      generador_de_contrasenia()
    elif option == 10:
      gestion_de_agenda_telefonica()
    else:
      os.system('clear')
      print('Opción no valida')

if __name__ == '__main__':
  main()