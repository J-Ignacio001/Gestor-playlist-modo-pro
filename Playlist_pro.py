import random
import json
import os

nombres = []
autores = []
generos = []

def menu():
    print("\n==============================")
    print("\t.-:Menu:-.")
    print("==============================")
    print("1.- Agregar cancion")
    print("2.- Ver canciones disponibles")
    print("3.- Eliminar una cancion")
    print("4.- Buscar canciones")
    print("5.- Recomendar canciones aleatoria")
    print("6.- Salir del programa \n")


def cargar_datos ():
    if os.path.exists("lista.json"):
        with open("lista.json", "r") as archivo:
            datos = json.load(archivo)
            generos.extend(datos["generos"])
            nombres.extend(datos["nombres"])
            autores.extend(datos["autores"])

def guardar_datos():
    datos = {"generos": generos, "nombres":nombres, "autores":autores}
    with open("lista.json", "w") as archivo:
        json.dump(datos, archivo, indent=4)

def agregar_cancion ():
    genero = input("Ingrese el genero de la cancion: ")
    nombre = input("Ingrese el nombre de la cancion: ")
    autor = input("Ingrese el autor de la cancion: ")
    
    generos.append(genero)
    nombres.append(nombre)
    autores.append(autor)
    guardar_datos()

    print("\nCancion agregada exitosamente!")
    print(f"{nombre} - {autor}")


def ver_cancion ():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas anteriormente.")
    else:
        print("\n--- Lista de canciones ---")
        for i in range(len(nombres)):
            print(f"{i + 1}. {generos[i]}: {nombres[i]} - {autores[i]}")

def buscar_cancion ():
    print("1.- Buscar cancion por su genero: ")
    print("2.- Buscar cancion por su nombre: ")
    decision = int(input("Ingrese un numero: "))

    if decision == 1:
        search = input("Ingrese el genero de la cancion: ")
        encontrado = False

        print(f"\n--- Canciones de {search}---")
        for i in range(len(nombres)):
            if generos[i].lower() == search.lower():
                print(f"{nombres[i]} - {autores[i]}")
                encontrado = True
        if encontrado == False:
            print("\nNo hay canciones registradas anteriormente.")

    elif decision == 2:
            search = input("Ingresa el nombre de la cancion: ")
            encontrado = False
        
            for i in range(len(nombres)):
                if nombres[i].lower() == search.lower():
                    print("\n--- Cancion encontrada! ---")
                    print(f"{generos[i]}: { nombres[i]} - {autores[i]}")
                    encontrado = True
            if encontrado == False:
                print("\nNo hay canciones registradas anteriormente.")
    else:
        print("\nOpcion no valida")
    
def eliminar ():
    search = input("Ingresa el nombre de la cancion a eliminar: ")
    encontrado = False

    for i in range(len(nombres)):
        if nombres[i].lower() == search.lower():
            print("\n--- Cancion Eliminada ---")
            print(f"{nombres[i]} - {autores[i]}")

            nombres.pop(i)
            autores.pop(i)
            generos.pop(i)
            guardar_datos()
            encontrado = True
            break

    if encontrado == False:
        print("\nCancion inexistente. Intente de nuevo.")
def recomendar_canciones():
    recomendar = input("Ingrese el genero de su agrado: ")
    posiciones = []

    for i in range(len(generos)):
        if generos[i].lower() == recomendar.lower():
            posiciones.append(i)
    if len(posiciones) == 0:
        print("\nNo hay canciones de ese genero.")
    else:
        i = random.choice(posiciones)
        print("\n---Recomendaciones---")
        print(f"{nombres[i]} - {autores[i]}")
cargar_datos( )
validar = 1

while validar !=0:
    menu()
    opcion = int(input("Eliga una opcion (1-6): "))
    if opcion == 1:
        agregar_cancion()
    elif opcion == 2:
        ver_cancion()
    elif opcion == 3:
        eliminar()
    elif opcion == 4:
        buscar_cancion()
    elif opcion == 5:
        recomendar_canciones()
    elif opcion == 6:
        print("Saliste del programa.")
        validar = 0
    else:
        print("Error, numeros no validos. Vuelva a intentar")
