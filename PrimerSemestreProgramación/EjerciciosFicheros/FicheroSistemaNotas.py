# Existen 3 formas para abrir un fichero
#                           PRIMERA                           #

fichero = open("PruebaFicheros.txt", "r")
linea = fichero.readline()
while linea != '':
    print(linea.rstrip())
    linea = fichero.readline()
fichero.close()
#                           SEGUNDA                           #
fichero = open("PruebaFicheros.txt", "r")
for linea in fichero:
    print (linea.rstrip())
fichero.close()
#                           TERCERA                           #
with open ("PruebaFicheros.txt", "r") as fichero:
    for linea in fichero:
        print (linea.rstrip())
# Para poder partir la información se utiliza el método .strip y el .split para partir la información en variables.
# Creamos una clase para poder almacenar la información más eficientemente.
class Estudiante:
    def __init__(self,nombre,notas,semestre,curso):
        self.nombre   = nombre
        self.notas    = notas
        self.semestre = semestre
        self.curso    = curso
    def __str__(self):
        return f"El alumno [{self.nombre}] del curso [{self.curso}] del semestre [{self.semestre}] tiene {self.notas} como calificaciones."

# Ejercicio: Obtener mediante un fichero de texto una serie de datos y hacer unos cálculos con ellos.
# Con una estructura de Nombre ["Asignatura -> Nota"] Semestre Curso
# Buscamos mostrar la información, sacar las mejores notas y sacar la media de cada estudiante.

def obtener_info(nombre_fichero):
    lista_estudiantes = []
    with open (f"{nombre_fichero}", "r") as archivo:
        for oracion in archivo:
            if oracion[0] != "#":
                nombre, resto = oracion.strip().split(" ", 1)
                # Partimos la frase en dos partes
                inicio_notas = resto.find("[")
                fin_notas = resto.find ("]") + 1
                # La suma es necesaria para incluir también el "]" como valor
                notas = resto[inicio_notas:fin_notas]
                # Buscamos el comienzo de la lista de notas y el final, finalmente lo asignamos a notas.
                despues = resto[fin_notas:].strip()
                semestre, curso = despues.split(" ",1)
                # Y el resto del fin de notas hasta el final lo partimos en las dos variables que necesitamos.
                nuevo_estudiante = Estudiante (nombre, notas, semestre, curso)
                lista_estudiantes.append(nuevo_estudiante)
        return lista_estudiantes

def enseñar_notas_por_alumno (lista_estudiantes):
    for estudiante in lista_estudiantes:
        print (f"Las notas del estudiante {estudiante.nombre} son :")
        notas_limpias = estudiante.notas.strip("[]")
        # Quitamos los corchetes a las notas
        lista_notas = notas_limpias.split(", ")
        # Quitamos la coma a las notas
        lista_notas = [nota.strip('""') for nota in lista_notas]
        # Y creamos una lista con las notas sin las comillas. (Uso de comillas especiales -> '' para quitar las comillas normales -> "")
        valores = [float(nota.split("->")[1].strip()) for nota in lista_notas]
        # Separamos cada nota en asignatura y valor numérico usando '->'.
        # Ejemplo: Mates -> 9.8 -> asignatura = "Mates", valor = 9.8
        media = sum(valores)/len(valores)
        media = round(media, 2)
        # Sacamos la media y la redondeamos con dos decimales.
        print ("_" * 40)
        for nota in lista_notas:
            print (f" - {nota}")
        print (f" - Media: {media}")
        print ("_" * 40)
        # Finalmente enseñamos las notas
def obtener_diccionario_notas(estudiante):
    lista_notas = estudiante.notas.strip("[]").split(", ")
    lista_notas = [nota.strip('"') for nota in lista_notas]
    notas_dict = {}
    # Recorremos la lista de notas y la limpiamos, finalmente inicializamos un diccionario.
    for nota in lista_notas:
        asignatura = nota.split("->")[0].strip()
        valor = float(nota.split("->")[1].strip())
        notas_dict[asignatura] = valor
        # Partimos cada parte con su variable y asignamos una clave (Asignatura) con un valor (Nota).
    return notas_dict

def mejores_notas(lista_estudiantes):
    mejores = {}
    # Inicializamos un diccionario con las mejores notas de cada asignatura.
    for estudiante in lista_estudiantes:
        notas_dict = obtener_diccionario_notas(estudiante)
        # Obtenemos las notas del diccionario con la función y el estudiante.
        for asignatura, valor in notas_dict.items():
            if asignatura not in mejores or valor > mejores[asignatura]:
                mejores[asignatura] = valor
        # Recorremos el diccionario con las variables que tiene.
        # Y añadimos la asignatura o metemos el valor mayor en el diccionario.
    print("Mejores notas por asignatura:")
    for asignatura, valor in mejores.items():
        print(f" - {asignatura}: {valor}")
        # Finalmente enseñamos los resultados.

def media_general(lista_estudiantes):
    for estudiante in lista_estudiantes:
        notas_dict = obtener_diccionario_notas(estudiante)
        valores = list(notas_dict.values())
        media = sum(valores)/len(valores)
        media = round (media,2)
        # Obtenemos sus notas y lo pasamos a lista, para posteriormente sacar la media y redondear con 2 decimales.
        print (f"El estudiante {estudiante.nombre} tiene {media} como media")


# EJEMPLOS DE USO #
#est = obtener_info("PruebaFicheros.txt")
#enseñar_notas_por_alumno(est)
#mejores_notas(est)
