# Lista inicial de juegos
juegos = [
    {
        "id": 1,
        "Nombre": "Counter strike 2",
        "Año de lanzamiento:": 2023,
        "Genero": "Shooter",
        "Plataformas": "PC",
        "Numero de Jugadores": 1400000,
        "Tiene Juego Online:": True
    },
    {
        "id": 2,
        "Nombre": "Valorant",
        "Año de lanzamiento:": 2020,
        "Genero": "Shooter",
        "Plataformas": "PC",
        "Numero de Jugadores": 16352647,
        "Tiene Juego Online:": True
    },
    {
        "id": 3,
        "Nombre": "Flappy Bird",
        "Año de lanzamiento:": 2013,
        "Genero": "Arcade",
        "Plataformas": "IOS, Android",
        "Numero de Jugadores": 0,
        "Tiene Juego Online:": False 
    }
]

siguiente_id = 4  # El siguiente id debe ser 4 porque ya hay un juego con id 3

# FUNCIONES
def cargar_juegos():
    global siguiente_id
    print("Cargando Datos...")
    
    nombre = input("ingrese el nombre del juego: ")
    año = int(input("ingrese el año de salida del juego: "))
    Genero = input("Ingrese el genero del juego EJ(Shooter, Estrategia, etc): ")
    Plataformas = input("ingrese la plataforma donde se juega EJ(PC, Xbox, PlayStation 5, ETC): ")
    Numero_de_Jugadores = int(input("ingrese la cantidad de jugadores: "))
    Online = input("ingrese si puede jugar online (si/no): ").strip().lower() == "sí"
    
    # Crear un nuevo juego
    nuevo_juego = {
        "id": siguiente_id,
        "Nombre": nombre,
        "Año de lanzamiento:": año,
        "Genero": Genero,
        "Plataformas": Plataformas,
        "Numero de Jugadores": Numero_de_Jugadores,
        "Tiene Juego Online:": Online
    }
    
    # Incrementar el siguiente id
    siguiente_id += 1

    juegos.append(nuevo_juego)
    print("El juego ha sido cargado exitosamente ")

def mostrar_juegos():
    print("Mostrando Datos")
    for juego in juegos:
        print(f"id: {juego['id']} - Nombre del juego: {juego['Nombre']} - Año de Lanzamiento: {juego['Año de lanzamiento:']} - Genero: {juego['Genero']} - Plataformas: {juego['Plataformas']} - Numero de jugadores: {juego['Numero de Jugadores']} Online: {juego['Tiene Juego Online:']}")

def editar_numero_jugadores():
    print("Editando numero de jugadores...")
    mostrar_juegos()
    id_a_editar = int(input("Ingrese el ID del juego a editar: "))

    juego_a_editar = None
    for juego in juegos:
        if juego["id"] == id_a_editar:
            juego_a_editar = juego
            break  # Salir del bucle si encontramos el juego

    if juego_a_editar is None:
        print("ID no encontrado.")
        return

    # Modificar el número de jugadores
    nuevo_numero_de_jugadores = int(input("Ingrese el nuevo numero de jugadores: "))
    juego_a_editar["Numero de Jugadores"] = nuevo_numero_de_jugadores
    print(f"El numero de jugadores del juego '{juego_a_editar['Nombre']}' ha sido actualizado a {nuevo_numero_de_jugadores}.")

def eliminar_juego():
    print("Eliminando juego...")
    mostrar_juegos()  
    id_a_borrar = int(input("Ingrese el ID del juego a borrar: "))

    juego_a_borrar = None
    for juego in juegos:
        if juego["id"] == id_a_borrar:
            juego_a_borrar = juego
            break

    if juego_a_borrar is None:
        print("El ID no existe.")
        return

    # Eliminar el juego de la lista
    juegos.remove(juego_a_borrar)
    print(f"El juego '{juego_a_borrar['Nombre']}' ha sido eliminado.")


def buscar_juego_por_nombre():
    print("Buscando juego por nombre...")
    nombre_a_buscar = input("Ingrese el nombre a buscar: ").strip().lower()  # Convierte a minúsculas para hacer la búsqueda más flexible
    juegos_encontrados = []

    for juego in juegos:
        if nombre_a_buscar in juego["Nombre"].lower():  # Usamos lower() para que la búsqueda no sea sensible a mayúsculas/minúsculas
            juegos_encontrados.append(juego)

    if len(juegos_encontrados) == 0:
        print("No encontramos el juego")
        return
    
    for juego in juegos_encontrados:
        print(f"id: {juego['id']} - Nombre del juego: {juego['Nombre']} - Año de Lanzamiento: {juego['Año de lanzamiento:']} - Genero: {juego['Genero']} - Plataformas: {juego['Plataformas']} - Numero de jugadores: {juego['Numero de Jugadores']} Online: {juego['Tiene Juego Online:']}")

def reporte_juegos_sin_jugadores():
    print("Reporte juegos sin jugadores...")
    cantidad_juegos_sin_jugadores = int(input("Ingrese la cantidad de jugadores a partir de la cual se considera que el juego no tiene jugadores activos: "))
    
    juego_sin_jugadores = {}
    
    for juego in juegos:
        if juego["Numero de Jugadores"] <= cantidad_juegos_sin_jugadores:
            juego_sin_jugadores[juego["id"]] = juego

    if len(juego_sin_jugadores) == 0:
        print("El juego no tiene jugadores activos")
        return

    for id, juego in juego_sin_jugadores.items():
        print(f"id: {juego['id']} - Nombre del juego: {juego['Nombre']} - Año de Lanzamiento: {juego['Año de lanzamiento:']} - Genero: {juego['Genero']} - Plataformas: {juego['Plataformas']} - Numero de jugadores: {juego['Numero de Jugadores']} Online: {juego['Tiene Juego Online:']}")



def enter_para_continuar():
    input("Enter para continuar...")

# MENU PRINCIPAL
opcion = "esto es para ingresar al bucle"

while opcion != "0":
    # PRINT OPCIONES
    print("""
    BIENVENIDO A LA APP DE INVENTARIO PARA TUS VIDEOJUEGOS FAVORITOS, INGRESE UN NUMERO DEPENDE DE LA OPCION DESEADA:
              1 - Cargar Juego
              2 - Mostrar Juego
              3 - Editar numero de jugadores en un juego
              4 - Eliminar Juego
              5 - Buscar juego por nombre
              6 - Reporte de juegos sin jugadores
              0 - Salir
    """)
    opcion = input("ingrese una opcion ")
    
    # CARGA DE JUEGO
    if opcion == "1":        
        cargar_juegos()
    # MUESTRA DE JUEGO
    elif opcion == "2":
        mostrar_juegos()
    # EDITAR JUEGO
    elif opcion == "3":
        editar_numero_jugadores()
    #ELIMINAR JUEGO
    elif opcion == "4":
        eliminar_juego()
    elif opcion == "5":
        buscar_juego_por_nombre()
    elif opcion =="6":
        reporte_juegos_sin_jugadores()

    # SALIR
    elif opcion == "0":
        print("Gracias por usar la APP")
    else:
        print("Opcion incorrecta, intente de nuevo")
    if opcion != "0":
        enter_para_continuar()


