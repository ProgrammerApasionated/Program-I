# Examen Final del 2025 (15 junio).

ciudades = ["Barcelona", "Castellón", "Bezdead", "Berlin", "Munich"]
temperatura = [[-3,-2,2,3,7,2,3,-8],         # Barcelona
               [3,3,4,6,10,11,2,4],          # Castellón
               [-1,-2,-6,0,2,-2,5,-3],       # Bezdead
               [-4,-3,-2,-2,-3,-4,-2,-1],    # Berlin
               [-1,0,0,-2,-3,0,3,3]]         # Munich

# Comprobación que los datos están correctos.
##for #i in range (len(temperaturas)):
    #print (f"La ciudad {ciudades[i]} tiene temperatura {temperaturas[i]}")

##                                    PROBLEMA 1                                                    ###
def ciudades_con_ola_de_frio(lista_temperaturas, nombre_ciudades,n):
    lista_ciudades_frias = []
    for i in range (len(lista_temperaturas)):
        longitud = 0
        longitud_max = -1
        print (f"La ciudad {nombre_ciudades[i]} está evaluandose")
        for j in range (len(lista_temperaturas[0])):
            if lista_temperaturas[i][j] < 0:
                longitud += 1
            else:
                if longitud_max < longitud:
                    longitud_max = longitud
                longitud = 0
        # Recorremos la matriz y aumentamos la longitud o la reiniciamos para luego evaluarla.
        if longitud_max < longitud:
            longitud_max = longitud
        # En el caso de que hay todas las temperaturas negativas no hay valor de longitud máxima, así que hace falta esta parte.
        if longitud_max >= n:
            lista_ciudades_frias.append(nombre_ciudades[i])
        # Evaluamos si hay más días que el dato que nos da el usuario.
    return lista_ciudades_frias

# Ejemplo para comprobar el funcionamiento de la función
ciudad_fria = ciudades_con_ola_de_frio(temperatura,ciudades,8)
print (ciudad_fria)

def mostrar_ciudades_extremas(matriz_temp, nombre_ciudad, primer_num, segundo_num):
    for dia in range (primer_num,segundo_num + 1):
        temp_max = matriz_temp[0][dia]
        ciudad_max = nombre_ciudad[0]
        temp_min= matriz_temp[0][dia]
        ciudad_min = nombre_ciudad[0]
        # Inicializamos el día con unos valores iniciales de ese día para asumir un máximo. Dentro del for, para que cada día cambie.
        for j in range (len(matriz_temp)):
            if matriz_temp[j][dia] > temp_max:
                temp_max = matriz_temp[j][dia]
                ciudad_max = nombre_ciudad[j]
            elif matriz_temp[j][dia] < temp_min:
                temp_min = matriz_temp[j][dia]
                ciudad_min = nombre_ciudad[j]
        # Evaluamos la condición y asignamos los valores máximos o mínimos.
        print(f"El dia {dia}: mínima de {temp_min} en {ciudad_min} y máxima en {temp_max} en {ciudad_max}.")

# Ejemplo para comprobar su funcionamiento.
# Solo funciona para valores del 0 al 7, debido a que tenemos solo 8 temperaturas en la lista.
mostrar_ciudades_extremas(temperatura, ciudades, 2, 4)


###                                   FIN PROBLEMA 1                                      ###

class Establecimiento:
    def __init__(self, nombre, localidad):
        self.nombre = nombre
        self.localidad = localidad
        self.valoraciones = [0] * 6  # índices 0 a 5

    def añadir(self, estrellas):
        self.valoraciones[estrellas] += 1


###                                   PROBLEMA 2                                          ###

def actualizar_lista_establecimientos(nombre_fichero, lista_establecimientos):
    fichero = open(nombre_fichero)
    for linea in fichero:
        usuario, nombre, localidad, estrellas = linea.strip().split("#")
        estrellas = int(estrellas)
        encontrado = False
        # Inicializamos la variable encontrada y del fichero hemos sacado el usuario, nombre, localidad y estrellas.
        for est in lista_establecimientos:
            if est.nombre == nombre:
                est.añadir(estrellas)
                encontrado = True
                break
        # Si buscando en la lista de establecimientos coincide el nombre de la reseña con el de la clase añade esa estrella que el usuario ha puesto.
        if not encontrado:
            nuevo = Establecimiento(nombre, localidad)
            nuevo.añadir(estrellas)
            lista_establecimientos.append(nuevo)
        # Si no la encuentra crea un establecimiento con las especificaciones que han puesto los usuarios.
    fichero.close()
    # Es esencial cerrar el fichero para no modificar su contenido.

def establecimientos_mejor_valorados(lista_establecimientos, localidad):
    resultado = []
    # Inicializamos una lista con el resultado correcto.
    for est in lista_establecimientos:
        if est.localidad == localidad:
            total = 0
            resto = 0
            for i in range(6):
                total += est.valoraciones[i]
            # Calculamos el total de la cantidad de estrella de la 1-5.
            for i in range(5):
                resto += est.valoraciones[i]
            # Calculamos el total de la cantidad de estrellas de la 1-4.
            cinco_estrellas = est.valoraciones[5]
            # Cantidad de 5 estrellas del establecimiento.
            if total > 100 and cinco_estrellas > resto:
                resultado.append(est.nombre)
    return resultado
            # Si cumple con la condición (100 reseñas y mayoritariamente 5 estrellas) devuelve la lista con el nombre del establecimiento.
    # Si no hay ningún establecimiento que cumpla la condición, se devuelve la lista vacía.