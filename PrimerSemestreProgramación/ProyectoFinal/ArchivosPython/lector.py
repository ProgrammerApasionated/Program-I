# Parte del proyecto que lee el fichero de texto, saca la información y la mete en diccionarios.

def leer_fichero(nombre):
    """
    Lee un fichero de texto y devuelve una lista de diccionarios.
    Cada línea tiene este formato:
    fecha#pasos#horas_sueño#calorias#distancia
    """
    ruta = "../Datos/" + nombre
    lista_dias = []
    with open (ruta, "r") as fichero:
        for linea in fichero:
            dia, pasos, horas_dormidas, calorias, distancia = linea.strip().split("#")
            diccionario = {
                "fecha": dia,
                "pasos": int(pasos),
                "sueño": float(horas_dormidas),
                "calorias": int(calorias),
                "distancia": float(distancia),
            }
            lista_dias.append(diccionario)
    return lista_dias


def añadir_dia_fichero(nombre_fichero):
    """
    Pide al usuario los datos de un día, los convierte al formato correcto
    y los añade directamente al fichero de texto.
    Devuelve el diccionario del día añadido.
    """
    print("Introduce los datos del nuevo día:\n")
    fecha = input("Fecha (YYYY-MM-DD): ")
    pasos = int(input("Pasos: "))
    sueño = float(input("Horas de sueño: "))
    calorias = int(input("Calorías: "))
    distancia = float(input("Distancia (km): "))
    dia = {
        "fecha": fecha,
        "pasos": pasos,
        "sueño": sueño,
        "calorias": calorias,
        "distancia": distancia
    }
    linea = f"{fecha}#{pasos}#{sueño}#{calorias}#{distancia}\n"
    ruta = "../Datos/" + nombre_fichero
    with open(ruta, "a") as f:
        f.write(linea)
    print("\n✔ Día añadido correctamente al fichero.\n")
    return dia

leer_fichero("Datos.txt")