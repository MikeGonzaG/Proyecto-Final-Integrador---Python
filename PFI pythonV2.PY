from rich.console import Console
from rich.text import Text

# Crear una instancia de Console para usar en los prints
console = Console()

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
    console.print("🚀 Cargando Datos...", style="yellow")
    
    nombre = input("🎮 Ingrese el nombre del juego: ")
    año = int(input("📅 Ingrese el año de salida del juego: "))
    Genero = input("🎯 Ingrese el genero del juego EJ(Shooter, Estrategia, etc): ")
    Plataformas = input("💻 Ingrese la plataforma donde se juega EJ(PC, Xbox, PlayStation 5, ETC): ")
    Numero_de_Jugadores = int(input("👥 Ingrese la cantidad de jugadores: "))
    Online = input("🌐 Ingrese si puede jugar online (si/no): ").strip().lower() == "sí"
    
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
    console.print("✅ El juego ha sido cargado exitosamente", style="green")

def mostrar_juegos():
    console.print("📜 Mostrando Datos de los juegos...", style="cyan")
    for juego in juegos:
        console.print(f"🎮 id: {juego['id']} - Nombre del juego: {juego['Nombre']} - Año de Lanzamiento: {juego['Año de lanzamiento:']} - Género: {juego['Genero']} - Plataformas: {juego['Plataformas']} - Número de jugadores: {juego['Numero de Jugadores']} - Online: {'Sí' if juego['Tiene Juego Online:'] else 'No'}", style="white")

def editar_numero_jugadores():
    console.print("✏️ Editando número de jugadores...", style="yellow")
    mostrar_juegos()
    id_a_editar = int(input("📝 Ingrese el ID del juego a editar: "))

    juego_a_editar = None
    for juego in juegos:
        if juego["id"] == id_a_editar:
            juego_a_editar = juego
            break  # Salir del bucle si encontramos el juego

    if juego_a_editar is None:
        console.print("❌ ID no encontrado.", style="red")
        return

    # Modificar el número de jugadores
    nuevo_numero_de_jugadores = int(input("👥 Ingrese el nuevo número de jugadores: "))
    juego_a_editar["Numero de Jugadores"] = nuevo_numero_de_jugadores
    console.print(f"✅ El número de jugadores del juego '{juego_a_editar['Nombre']}' ha sido actualizado a {nuevo_numero_de_jugadores}.", style="green")

def eliminar_juego():
    console.print("🗑️ Eliminando juego...", style="yellow")
    mostrar_juegos()  
    id_a_borrar = int(input("🗑️ Ingrese el ID del juego a borrar: "))

    juego_a_borrar = None
    for juego in juegos:
        if juego["id"] == id_a_borrar:
            juego_a_borrar = juego
            break

    if juego_a_borrar is None:
        console.print("❌ El ID no existe.", style="red")
        return

    # Eliminar el juego de la lista
    juegos.remove(juego_a_borrar)
    console.print(f"✅ El juego '{juego_a_borrar['Nombre']}' ha sido eliminado.", style="green")

def buscar_juego_por_nombre():
    console.print("🔍 Buscando juego por nombre...", style="yellow")
    nombre_a_buscar = input("🔍 Ingrese el nombre a buscar: ").strip().lower()  # Convierte a minúsculas para hacer la búsqueda más flexible
    juegos_encontrados = []

    for juego in juegos:
        if nombre_a_buscar in juego["Nombre"].lower():  # Usamos lower() para que la búsqueda no sea sensible a mayúsculas/minúsculas
            juegos_encontrados.append(juego)

    if len(juegos_encontrados) == 0:
        console.print("❌ No encontramos el juego", style="red")
        return
    
    for juego in juegos_encontrados:
        console.print(f"🎮 id: {juego['id']} - Nombre del juego: {juego['Nombre']} - Año de Lanzamiento: {juego['Año de lanzamiento:']} - Género: {juego['Genero']} - Plataformas: {juego['Plataformas']} - Número de jugadores: {juego['Numero de Jugadores']} - Online: {'Sí' if juego['Tiene Juego Online:'] else 'No'}", style="white")

def reporte_juegos_sin_jugadores():
    console.print("📉 Reporte juegos sin jugadores...", style="yellow")
    cantidad_juegos_sin_jugadores = int(input("📊 Ingrese la cantidad de jugadores a partir de la cual se considera que el juego no tiene jugadores activos: "))
    
    juego_sin_jugadores = {}
    
    for juego in juegos:
        if juego["Numero de Jugadores"] <= cantidad_juegos_sin_jugadores:
            juego_sin_jugadores[juego["id"]] = juego

    if len(juego_sin_jugadores) == 0:
        console.print("❌ No hay juegos sin jugadores activos.", style="red")  # Mensaje de error en rojo
        return

    for id, juego in juego_sin_jugadores.items():
        console.print(f"🎮 id: {juego['id']} - Nombre del juego: {juego['Nombre']} - Año de Lanzamiento: {juego['Año de lanzamiento:']} - Género: {juego['Genero']} - Plataformas: {juego['Plataformas']} - Número de jugadores: {juego['Numero de Jugadores']} - Online: {'Sí' if juego['Tiene Juego Online:'] else 'No'}", style="white")

def enter_para_continuar():
    input("⏳ Presiona Enter para continuar...")

# MENU PRINCIPAL
opcion = "esto es para ingresar al bucle"

while opcion != "0":
    # PRINT OPCIONES
    console.print("""
    🌟 BIENVENIDO A LA APP DE INVENTARIO PARA TUS VIDEOJUEGOS 🎮 FAVORITOS, INGRESE UN NÚMERO DEPENDIENDO DE LA OPCIÓN DESEADA:
    1 - Cargar Juego
    2 - Mostrar Juegos
    3 - Editar Número de Jugadores en un juego
    4 - Eliminar Juego
    5 - Buscar Juego por Nombre
    6 - Reporte de Juegos sin Jugadores
    0 - Salir
    """, style="cyan")

    opcion = input("Ingrese una opción: ")
    
    # CARGA DE JUEGO
    if opcion == "1":        
        cargar_juegos()
    # MUESTRA DE JUEGO
    elif opcion == "2":
        mostrar_juegos()
    # EDITAR JUEGO
    elif opcion == "3":
        editar_numero_jugadores()
    # ELIMINAR JUEGO
    elif opcion == "4":
        eliminar_juego()
    elif opcion == "5":
        buscar_juego_por_nombre()
    elif opcion == "6":
        reporte_juegos_sin_jugadores()

    # SALIR
    elif opcion == "0":
        console.print("🙏 Gracias por usar la APP", style="green")
    else:
        console.print("❌ Opción incorrecta, intente de nuevo", style="red")

    if opcion != "0":
        enter_para_continuar()
