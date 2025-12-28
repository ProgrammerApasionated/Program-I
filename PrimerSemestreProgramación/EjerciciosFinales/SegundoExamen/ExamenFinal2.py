# Examen Final del 2024 (17 junio).

# Datos inventados.
matriz_año_1 = [
    [80, 78, 77, None, None, 75, 74, 73, 72, None],   # Embalse 0
    [None, None, None, None, 63, 64, None, 65, 66, 67],# Embalse 1
    [40, None, None, None, 30, 43, 44, 45, 46, 47], # Embalse 2
    [90, 91, 92, 93, 94, None, None, None, 95, 96] # Embalse 3
]

matriz_ano_2 = [
    [82, 80, 79, None, 78, 77, 76, 75, 74, 73],   # Embalse 0
    [58, 59, None, 60, 61, 62, None, 63, 64, 65],# Embalse 1
    [45, None, None, None, 47, 48, 49, 50, 51, 52], # Embalse 2
    [88, 89, 90, 91, 92, None, None, None, 90, 94] # Embalse 3
]
##                                    PROBLEMA 1
def peor_embalse(matriz_embalse):
    # Cálculo de la fila (Embalse) con el promedio más bajo.
    peor_embal    = None
    peor_promedio = None
    for i in range(len(matriz_embalse)):
        total = 0
        contador_sumas  = 0
        for j in range (len(matriz_embalse[0])):
            if matriz_embalse[i][j] is not None:
                total +=matriz_embalse[i][j]
                contador_sumas += 1
        if contador_sumas > 0:
            promedio = total/ contador_sumas
            if peor_promedio is None or promedio < peor_promedio:
                peor_promedio = round(promedio,2)
                peor_embal = i
    print (f"El peor embalse ha sido el {peor_embal} con un promedio de {peor_promedio}")
def dia_mayor_aumento(matriz1,matriz2):
    # Calculamos el promedio del día y restamos su resultado entre las dos matrices.
    mayor_aumento = None
    dia_mayor     = None
    for j in range (len(matriz1[0])):
        suma1 = 0
        suma2 = 0
        cont1 = 0
        cont2 = 0
        for i in range (len(matriz1)):
            if matriz1[i][j] is not None:
                suma1 += matriz1[i][j]
                cont1 += 1
            if matriz2[i][j] is not None:
                suma2 += matriz1[i][j]
                cont2 += 1
            if cont1 > 0 and cont2 > 0:
                promedio1 = suma1 / cont1
                promedio2 = suma2 / cont2
                diferencia = promedio2 - promedio1
                if diferencia > 0 and (mayor_aumento is None or diferencia > mayor_aumento):
                    mayor_aumento = diferencia
                    dia_mayor = j
    print (f"El dia con la mayor diferencia ha sido el {dia_mayor} con {mayor_aumento}")
    return dia_mayor
def sistema_defectuoso(matriz, t):
    # Buscamos una racha del valor None y añadimos esa balsa a la lista_embalses.
    lista_embalses  = []
    for i in range(len(matriz)):
        longitud = 0
        for j in range (len(matriz[0])):
            if matriz[i][j] is None:
                longitud += 1
                if longitud >= t:
                    lista_embalses.append(i)
                    break
            else:
                longitud = 0
    print (lista_embalses)
    return lista_embalses

dia_mayor_aumento(matriz_ano_2,matriz_año_1)
peor_embalse(matriz_año_1)
peor_embalse(matriz_ano_2)
sistema_defectuoso(matriz_año_1,4)


##                                    PROBLEMA 2
class Deporte:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estudiantes = []
def crear_lista_deportes(nombre_fichero, grado):
    lista_deportes = []
    with open(nombre_fichero, "r") as fichero:
        for linea in fichero:
            linea = linea.strip()
            dni, modalidad, carrera = linea.split("#")
            if carrera != grado:
                continue
            dep_obj = None
            for d in lista_deportes:
                if d.nombre == modalidad:
                    dep_obj = d
                    break
            if dep_obj is None:
                dep_obj = Deporte(modalidad)
                lista_deportes.append(dep_obj)
            dep_obj.estudiantes.append(dni)
    return lista_deportes

