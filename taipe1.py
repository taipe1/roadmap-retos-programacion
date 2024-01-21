"""
EJERCICIO:
 * - Muestra ejemplos de creación de todas las estructuras soportadas por defecto en tu lenguaje.
 * - Utiliza operaciones de inserción, borrado, actualización y ordenación..
"""
#string
cadena = 'Cadena de Muestra'
print(cadena)
print(cadena[0])
print(cadena[0:3])
print(cadena[0:10:2])
print(cadena[-1])
print(cadena[::-1])
print(cadena*3)
print(len(cadena))
print(cadena.upper())
print(cadena.lower())
print('de' in cadena)
print('CASITA' not in cadena)
print(cadena.split(' '))
print(cadena.replace('Muestra', 'Prueba'))
#listas
lista = [1,2,3,4,5]
print(len(lista))
print(6 in lista)
print(lista[0])
print(lista[0:3])
print(min(lista))
print(max(lista))
print(sum(lista))
print(lista*3)
print(lista.append(6))
#tuplas
tuplas = (1,6,3,11,5)
print(4 in tuplas)
print(min(tuplas))
print(max(tuplas))
print(sum(tuplas))
print(sorted(tuplas))
#diccionarios
diccionario = {'nombre':'Juan','edad':30,'ciudad':'Madrid'}
diccionario2 = {'apellido':'Perez'}
print(diccionario['nombre'])
del(diccionario['edad'])
print(diccionario)
print(30 in diccionario.values())
print(diccionario.keys())
print(diccionario.items())
print(diccionario.get('nombre'))
diccionario2 = diccionario.copy()
print(diccionario2)
#conjuntos
conjuntos = {1,2,3,4,5}
conjuntos2 = {3,4,5,6,7}	
print(conjuntos.union(conjuntos2))
print(conjuntos.intersection(conjuntos2))
print(conjuntos & conjuntos2)
print(conjuntos.difference(conjuntos2))
print(conjuntos.symmetric_difference(conjuntos2))



"""
Crea una agenda de contactos por terminal.
 * - Debes implementar funcionalidades de búsqueda, inserción, actualización
 *   y eliminación de contactos.
 * - Cada contacto debe tener un nombre y un número de teléfono.
 * - El programa solicita en primer lugar cuál es la operación que se quiere realizar,
 *   y a continuación los datos necesarios para llevarla a cabo.
 * - El programa no puede dejar introducir números de teléfono no númericos y con más
 *   de 11 dígitos (o el número de dígitos que quieras).
 * - También se debe proponer una operación de finalización del programa.
"""

agenda = []

def opciones(opcion):
  if opcion == 1:
    llenar_agenda(agenda) 
    print("\n")
  elif opcion == 2:
    mostrar_agenda(agenda)
    print("\n")
  elif opcion == 3:
    busqueda_agenda(agenda) 
    print("\n")
  elif opcion == 4:
    insertar_contacto()
    print("\n")
  elif opcion == 5:
    actualizar_contacto()
    print("\n")
  elif opcion == 6:
    borrar_contacto()
    print("\n")
  elif opcion == 7:
    salir()
  else:
    print("Opción inválida")
    menu()
  menu()
  
def llenar_agenda(agenda):
  for i in range(0,int(input("Ingrese la cantidad de contactos: "))):
    nombre = input("nombre: ")
    telefono = validar_telefono(input("telefono1: "))
    agenda.append([nombre,telefono])
  return (agenda)

def validar_telefono(telefono):
  while not telefono.isnumeric() or len(telefono) > 9:
    print("El número de teléfono debe ser numérico y tener menos de 9 dígitos")
    telefono = input("telefono2: ")
    return telefono
  return telefono

def mostrar_agenda(agenda):
  if( len(agenda) != 0):
    for i in range(len(agenda)):
      print(f'Nombre: {agenda[i][0]} - Telefono: {agenda[i][1]}')

  else:
    print('No hay elementos en la agenda')
  
def busqueda_agenda(agenda):
  print("Ingrese el nombre del contacto a buscar: ")
  nombre = input("nombre: ")
  if( len(agenda) != 0):
    for i in range(len(agenda)):
      if agenda[i][0] == nombre:
        print(f'El contacto {nombre} se encuentra en la posición {i}') 
        break
      print('No se encontro el contacto')
      break
  else:
    print('No hay elementos en la agenda')
  
def insertar_contacto():
  print("Ingrese los datos")
  agenda.append([input("nombre: "),input("telefono: ")])
  print('Contacto insertado!!')

def actualizar_contacto():
  print("Ingrese el nombre del contacto a actualizar: ")
  nombre = input("nombre: ")
  for i in range(len(agenda)):
    if agenda[i][0] == nombre:
      agenda[i][0] = input("nombre: ")
      agenda[i][1] = input("telefono: ")
      print('Contacto actualizado!!')
      
def borrar_contacto():
  print("Ingrese el nombre del contacto a borrar: ")
  nombre = input("nombre: ")
  for i in range(len(agenda)):
    if agenda[i][0] == nombre:
      agenda.pop(i)
      print('Contacto borrado!!')

def salir():
  print("Saliendo del programa...")
  exit()

def menu():
  print("1. Crear Agenda")
  print("2. Mostrar Agenda")
  print("3. Buscar contacto")
  print("4. Insertar contacto")
  print("5. Actualizar contacto")
  print("6. Borrar contacto")
  print("7. Salir")
  opcion = int(input("Ingrese una opción: "))
  opciones(opcion)
  

menu()
