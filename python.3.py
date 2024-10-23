'''lista1 = [1,2,3,4]

tupla1 = (1,2,3,4)

print("Valor de la lista")
print(lista1)

print("Valor de la tupla")
print(tupla1)

lista1[0] = 10
print("Valor de la lista")
print(lista1)

lista1[0] = 10
print("Valor de la tupla")
print(tupla1)

dic1 = {}

nombre = input("introduce el nombre del nuevo contacto: ")
telefono = input(f"introduce el teléfno de {nombre}")

dic1[nombre] = telefono

print("Esta es tu agenda")
print(dic1)

print("Vamos a modificar el teléfono de un contacto: ")
nombre_busqueda = input("Dame el nombre del contacto que quieres cambiar: ")
telefono_nuevo = input("dame el nueo número de teléfono: ")

dic1[nombre_busqueda] = telefono_nuevo

print(dic1)'''

'''lista_reproduccion = []
#Permitir al usuario introducir nombres de candiones

cancion = input('Ingresa nombre de una cancion: ')
while cancion != "fin":
    lista_reproduccion.append(cancion)
    cancion =input('Ingresa nombre de una cancion: ').lower()

print (lista_reproduccion)

for i in range(len(lista_reproduccion)):
    print(f"{i}.- {lista_reproduccion[i]}")

cancion_a_reproducir = int(input("Dime el número de canción que quieres escuchar: "))

print (f"Estas escuchado: {lista_reproduccion[cancion_a_reproducir]}")'''

'''Contactos = {}

while True:
    nombre = input("Ingresa nombre del contacto o fin para terminar: ")
    if nombre == "fin":
        break
    telefono = input(f"Ingresa el número de telefono de {nombre}:")
    Contactos[nombre] = telefono
    
for nombre in Contactos:
    print(f"-{nombre}:{telefono}")

Contactos_a_buscar = input("Nombre del contacto: ")
print (f"Numero de telefono de: {Contactos_a_buscar} es :{Contactos[Contactos_a_buscar]}")'''

