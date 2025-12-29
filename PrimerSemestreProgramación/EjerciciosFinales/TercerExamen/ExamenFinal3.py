# Examen final del 2023 (16 de enero).

# Datos inventados.

produccion = [
    [5.2, 6.1, 0.0, 0.0, 0.0, 4.8],  # Panel 0
    [4.9, 5.5, 5.7, 5.6, 5.8, 6.0],  # Panel 1
    [0.0, 0.0, 0.0, 1.2, 1.5, 1.7],  # Panel 2
    [6.0, 6.3, 6.5, 6.4, 6.2, 6.1]   # Panel 3
]

##                                    PROBLEMA 1

def produccion_diaria(matriz_prod):
    # Queremos calcular la producción diaria total (Calcular el sumatorio de cada columna) y poner los resultados en una lista.
    lista_totales = []
    fila    = len(matriz_prod)
    columna = len(matriz_prod[0])
    for dia in range(columna):
        total_dia = 0
        for panel in range(fila):
            total_dia += matriz_prod[panel][dia]
            if panel == fila - 1:
                print (f"El dia {dia} ha tenido una producción total de {total_dia}")
                lista_totales.append(total_dia)
    return lista_totales
def peor_día(matr_prod):
    # Queremos calcular usando la función anterior el mínimo de los valores dentro de la lista (En caso de empate elegimos el último(poner el = en la condición)).
    lista = produccion_diaria(matriz)
    peor = 0
    for i in range(len(lista)):
        if lista[i] <= lista[peor]:
            peor = i
    print (f"De la lista de totales {lista} el peor día ha sido el {peor}")
    return peor
def defectuoso(matriz,num_panel,a):
    # Queremos calcular usando una función anterior una racha de días donde un panel concreto (una fila) cumple una racha de no cumplir un umbral concreto "a".
    dias = len(matriz[0])
    racha = 0
    max_racha = 0
    for fila in range(dias):
        if matriz[num_panel][fila] == 0:
            racha += 1
        else:
            if racha > max_racha:
                max_racha = racha
            racha = 0
    if racha > max_racha:
        max_racha = racha
    return max_racha > a

def panel_mas_rentable(matrix):
    # Queremos calcular el panel con el total de energía mayor (fila con el mayor sumatorio).
    fila     = len (matrix)
    columna  = len (matrix[0])
    max_total = None
    panel_max = None
    for panel in range(fila):
        total_panel = 0
        for dia in range(columna):
            total_panel += matrix[panel][dia]
        if max_total is None or max_total < total_panel:
            max_total = total_panel
            panel_max = panel
    print (f"El panel con el máximo total es el {panel_max} con un total de {max_total}")
    return panel_max
# Por pura estética y prueba del funcionamiento he puesto unos prints innecesarios, perfectamente todos los prints se podrían quitar.



##                                    PROBLEMA 2
# Datos con esta estructura -> SIP#CódigoCentroSalud#Enfermedad, donde Enfermedad in [Gripe Común, Gripe A, Covid-19].
class CentroSalud:
    def __init__(self,codigo):
        self.codigo      = codigo
        self.gripe_comun = 0
        self.gripe_A     = 0
        self.covid19     = 0
# Por pura estética voy a hacer la función __str__ para poder enseñar como se ve la clase.
    def __str__(self):
        return f"El centro de salud {self.codigo} tiene {self.gripe_comun} enfermos de gripe común, {self.gripe_A} de gripe A y {self.covid19} de covid"

def crear_lista(nombre):
    lista = []
    with open(nombre) as fichero:
        for linea in fichero:
            sip, codigo, enfermedad = linea.strip().split("#")
            encontrado = None
            for centro in lista:
                if centro.codigo == codigo:
                    encontrado = centro
                    break
            if encontrado is None:
                encontrado = CentroSalud(codigo)
                lista.append(encontrado)
            if enfermedad == "Gripe común":
                encontrado.gripe_comun += 1
            elif enfermedad == "Gripe A":
                encontrado.gripe_A += 1
            else:
                encontrado.covid19 += 1
    return lista

def centro_con_mas_incidencia(lista, enfermedad):
    max_casos = 0
    mejor = None
    for centros in lista:
        if enfermedad == "Gripe común":
            casos = centros.gripe_comun
        elif enfermedad == "Gripe A":
            casos = centros.gripe_A
        else:
            casos = centros.covid19
        if casos > max_casos:
            max_casos = casos
            mejor = centros.codigo
    if max_casos == 0:
        return None
    return mejor


# Ejemplos de uso
#produccion_diaria(produccion)
#peor_día(produccion)
#defectuoso(produccion,3,4)
#panel_mas_rentable(produccion)