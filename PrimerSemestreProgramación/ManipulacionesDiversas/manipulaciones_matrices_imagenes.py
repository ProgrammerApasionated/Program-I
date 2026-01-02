# Ejercicio de práctica de matrices de imágenes.
# Funciones orientadas a cambiar una imagen.

def aclarar_matriz (matriz , valor ) :
    fila    = len (matriz)
    columna = len (matriz[0])
    for i in range (fila) :
        for j in range (columna):
            matriz[i][j] += valor
    return matriz

def invertir_matriz (matriz):
    fila    = len (matriz)
    columna = len (matriz[0])
    for i in range (fila):
        for j in range (columna):
            matriz[i][j] = 255 - matriz[i][j]
    return matriz
def poner_diagonal_0 (matriz):
    fila    = len (matriz)
    columna = len (matriz[0])
    for i in range (fila):
        for j in range (columna):
            if j > i:
                matriz[i][j] = 0
    return matriz

def suma_matriz_superior(matriz):
    fila    = len (matriz)
    columna = len (matriz[0])
    suma_total = 0
    for i in range (fila):
        for j in range (columna):
            if j > i: # Con < para sumar los elementos inferiores
                suma_total += matriz[i][j]
    return suma_total

def suma_columnas(matriz): # Suma solo la primera columna
    columna = len (matriz[0])
    suma = 0
    for j in range (columna):
        suma += matriz[0][j]
    return suma

def invertir_fila_por_columna(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_invertida = []
    for j in range(columnas):
        nueva_fila = []
        for i in range(filas):
            nueva_fila.append(matriz[i][j])
        matriz_invertida.append(nueva_fila)
    return matriz_invertida