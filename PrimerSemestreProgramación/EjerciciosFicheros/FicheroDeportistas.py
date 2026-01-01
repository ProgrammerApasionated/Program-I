# Ejercicio orientado a leer los datos de Datos.txt
# Datos con el siguiente formato -> Nombre [Actividad -> Valor] Temporada Nivel

class Deportista:
    def __init__(self,nombre,actividad,temporada,nivel):
        self.nombre     = nombre
        self.actividad  = actividad
        self.temporada  = temporada
        self.nivel      = nivel
    def __str__(self):
        return f"{self.nombre} con {self.actividad} en temporada {self.temporada} y nivel {self.nivel}"

# Obtener datos del fichero
def obtener_datos(nombre_fichero):
    lista_deportistas = []
    with open(nombre_fichero, "r") as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea[0] == "#":
                continue
            # Formato de  : Nombre [Actividad -> Valor] Temporada Nivel
            nombre, resto = linea.split(" ", 1)
            inicio = resto.find("[")
            fin = resto.find("]") + 1
            actividad = resto[inicio:fin]
            despues = resto[fin:].strip()
            temporada, nivel = despues.rsplit(" ", 1)
            lista_deportistas.append(Deportista(nombre, actividad, temporada, nivel))
    return lista_deportistas

# Mostrar deportes
def mostrar_deporte(lista):
    for deportista in lista:
        print(f"Deportista: {deportista.nombre}")
        lista_deportes = deportista.actividad.strip("[]").split(", ")
        print("-" * 40)
        for dep in lista_deportes:
            dep = dep.strip('"')
            deporte, valor = dep.split("->")
            print(f" - {deporte.strip()} con valor {valor.strip()}")
        print("-" * 40)

# Convertir actividades a diccionario
def conseguir_dict(deportista):
    lista_deportes = deportista.actividad.strip("[]").split(", ")
    diccionario = {}
    for dep in lista_deportes:
        dep = dep.strip('"')
        deporte, nivel = dep.split("->")
        diccionario[deporte.strip()] = float(nivel.strip())
    return diccionario

# Niveles más altos
def niveles_altos(lista):
    altos = {}
    for dep in lista:
        dic = conseguir_dict(dep)
        for deporte, nivel in dic.items():
            if deporte not in altos or nivel > altos[deporte]:
                altos[deporte] = nivel
    print("Deportes con los niveles más altos: ")
    for dep, nivel in altos.items():
        print(f" - {dep}: {nivel}")
    return altos

# Deportes más practicados
def deportes_mas_practicados(lista):
    contador = {}
    for dep in lista:
        dic = conseguir_dict(dep)
        for deporte in dic.keys():
            contador[deporte] = contador.get(deporte,0) + 1
    print("Cantidad de deportistas por deporte:")
    for dep, cant in contador.items():
        print(f" - {dep}: {cant}")
    return contador

# Añadir datos exactos al fichero
def añadir_datos_exactos(nom_fichero, nombre, deportes, temporada, nivel):
    with open(nom_fichero, "a") as f:
        actividades_str = ", ".join([f"{dep[0]} -> {dep[1]}" for dep in deportes])
        linea = f"{nombre} [{actividades_str}] {temporada} {nivel}\n"
        f.write(linea)
        print(f"Se ha añadido: {linea}")

# EJEMPLO DE USO
datos_actuales = obtener_datos("Datos.txt")
mostrar_deporte(datos_actuales)
niveles_altos(datos_actuales)
deportes_mas_practicados(datos_actuales)
añadir_datos_exactos("Datos.txt", "Julio", [("Basket",7.0),("Pilates",8.0)], "2022", "Medio")