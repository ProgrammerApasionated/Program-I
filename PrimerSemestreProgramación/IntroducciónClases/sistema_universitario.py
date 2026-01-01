# Ejercicio similar al de introducción_POO.py pero con un diseño más complejo.

class Asignaturas:
    def __init__(self,nombre,horario,profesor):
        self.nombre   = nombre
        self.horario  = horario
        self.profesor = profesor

    def __str__(self):
        return f"La asignatura con nombre {self.nombre} tiene horarios {self.horario} con el profesor {self.profesor}"

    def posibilidades_asignaturas(self):
        print ("n/N para Nombre. ")
        print ("h/H para Horario.")
        print ("p/P para Profesor.")

    def mostrar_info_concreta(self):
        self.posibilidades_asignaturas()
        opc = input ("Introduce la opción que quieres que se muestre. \n")
        opc_validas = ["N","n","H","h","P","p"]
        while opc not in opc_validas:
            self.posibilidades_asignaturas()
            opc = input ("Introduce una opción válida. \n")
        opc = opc.lower()
        if opc == "n":
            print (f"El nombre de la asignatura es {self.nombre}. ")
        elif opc == "h":
            print (f"Los horarios de la asignatura {self.nombre} son {self.horario}. ")
        else:
            print (f"El nombre del profesor que da la asignatura {self.nombre} es {self.profesor}. ")

    def cambiar_info_concreta(self):
        self.posibilidades_asignaturas()
        cambio = input ("Introduce la característica que quieres cambiar")
        while cambio.upper() not in ["P","H","N"]:
            self.posibilidades_asignaturas()
            cambio = input ("Introduce una característica válida. \n")
        cambio = cambio.lower()
        if cambio == "n":
            cambio_nombre = input (f"Introduce el nuevo nombre de la asignatura {self.nombre}. \n")
            while cambio_nombre == "":
                cambio_nombre = input ("Introduce un nombre válido. (Con algún carácter) \n")
            self.nombre = cambio_nombre.title()
            print (self)
        elif cambio == "h":
            cambio_horario = input (f"Introduce un cambio diferente al anterior. ({self.horario}) \n")
            horario_erroneo = ["",self.horario]
            while cambio_horario in horario_erroneo:
                cambio_horario = input ("Introduce un horario válido. (Con un horario distinto o diferente a la cadena vacía) \n")
            self.horario = cambio_horario.title()
            print (self)
        else:
            cambio_profesor = input (f"Introduce un cambio de profesor. {self.profesor} \n")
            profesor_equivocado = ["",self.profesor]
            while cambio_profesor in profesor_equivocado:
                cambio_profesor = input ("Introduce un cambio válido. (Distinto al anterior y con algún nombre) \n")
            self.profesor = cambio_profesor.title()
            print (self)

class Estudiante:
    def __init__(self, nombre, notas, genero):
        self.nombre = nombre
        self.notas = notas
        self.genero = genero

    def __str__(self):
        return f"Tiene nombre {self.nombre}, estas notas {self.notas} y genero {self.genero}"

    def media(self):
        return sum(self.notas) / len(self.notas)

    def racha_aprobados(self):
        racha = 0
        max_racha = 0
        for n in self.notas:
            if n >= 5:
                racha += 1
                max_racha = max(max_racha, racha)
            else:
                racha = 0
        return max_racha

    def tipo(self):
        m = self.media()
        r = self.racha_aprobados()
        if m >= 9 and r == len(self.notas):
            return "Excelente"
        elif m >= 6:
            return "Bueno"
        elif m >= 5:
            return "Aprobado"
        else:
            return "Suspenso"
class GrupoEstudiantes:
    def __init__(self):
        self.estudiantes = []

    def añadir_estudiante (self,estudiante):
        self.estudiantes.append(estudiante)

    def mostrar_info(self):
        for estudiante in self.estudiantes:
            print(estudiante)

    def buscar_estudiante(self):
        print("N/n   -> Nombre")
        print("No/no  -> Notas")
        print("G/g   -> Género")
        buscar = input("Introduce característica a buscar : \n")
        buscar = buscar.lower()
        while buscar not in ["n", "no", "g"]:
            buscar = input("Introduce una opción válida. (n,no,g) \n")
        encontrado = False
        if buscar == "n":
            nombre = input("Introduce el nombre del estudiante: ")
            nombre = nombre.title()
            for estudiante in self.estudiantes:
                if estudiante.nombre == nombre:
                    print(estudiante)
                    encontrado = True
        elif buscar == "no":
            notas = []
            nota = input("Introduce notas una a una. (nota negativa o mayor a 10 para terminar) \n")
            while nota.isdigit() and 0 <= int(nota) <= 10:
                notas.append(int(nota))
                nota = input("Introduce otra nota : (o algo distinto para terminar)  \n")
            for estudiante in self.estudiantes:
                if estudiante.notas == notas:
                    print(estudiante)
                    encontrado = True
        else:
            genero = input("Introduce género (Femenino / Masculino): ")
            while genero not in ["Femenino", "Masculino"]:
                genero = input("Género inválido: ")
            for estudiante in self.estudiantes:
                if estudiante.genero == genero:
                    print(estudiante)
                    encontrado = True
        if not encontrado:
            print("No se ha encontrado ningún estudiante. ")

class GrupoAsignaturas:
    def __init__(self):
        self.asignaturas = []

    def añadir_asignaturas (self,asignatura):
        self.asignaturas.append(asignatura)

    def mostrar_info(self):
        for i, asignatura in enumerate(self.asignaturas, start=1):
            print(f"{i}. {asignatura}")

    def cambiar_algo(self,index):
        if 1 <= index <= len(self.asignaturas):
            self.asignaturas[index - 1].cambiar_info_concreta()
        else:
            print ("Indice no válido. ")

class SistemaCompleto:
    def __init__(self):
        self.grupo_estudiantes = GrupoEstudiantes()
        self.grupo_asignaturas = GrupoAsignaturas()

    def guardar_info_estudiante(self, estudiante):
        texto = (
            f"Estudiante: {estudiante.nombre} | "
            f"Notas: {estudiante.notas} | "
            f"Media: {estudiante.media():.2f} | "
            f"Racha: {estudiante.racha_aprobados()} | "
            f"Tipo: {estudiante.tipo()}"
        )
        guardar_en_fichero("FicheroSistema.txt", texto)
        print("Información guardada.")
    def mostrar_info_completa(self):
        nombre = input("Introduce el nombre del estudiante: ")
        for est in self.grupo_estudiantes.estudiantes:
            if est.nombre.lower() == nombre.lower():
                print("-" * 40)
                print(f"Nombre: {est.nombre}")
                print(f"Notas: {est.notas}")
                print(f"Media: {est.media():.2f}")
                print(f"Racha de aprobados: {est.racha_aprobados()}")
                print(f"Tipo de estudiante: {est.tipo()}")
                print("-" * 40)
                return
        print("Estudiante no encontrado. ")

    def guardar_info_completa(self):
        nombre = input("Introduce el nombre del estudiante : \n")
        for est in self.grupo_estudiantes.estudiantes:
            if est.nombre.lower() == nombre.lower():
                self.guardar_info_estudiante(est)
                return
        print("Estudiante no encontrado. ")

    def menu(self):
        while True:
            print("-------- MENÚ SISTEMA --------")
            print("1.-Añadir estudiante.")
            print("2.-Mostrar estudiantes.")
            print("3.-Buscar estudiantes.")
            print("4.-Añadir asignatura.")
            print("5.-Mostrar asignaturas.")
            print("6.-Modificar asignatura.")
            print("7.-Mostrar información completa de un estudiante.")
            print ("8.-Guardar información en fichero")
            print ("9.-Salir")
            linea()
            opcion = input("Introduce la opción deseada: ")
            if opcion == "1":
                linea()
                self.añadir_estudiante()
                linea()
            elif opcion == "2":
                linea()
                self.grupo_estudiantes.mostrar_info()
                linea()
            elif opcion == "3":
                linea()
                self.grupo_estudiantes.buscar_estudiante()
                linea()
            elif opcion == "4":
                linea()
                self.añadir_asignatura()
                linea()
            elif opcion == "5":
                linea()
                self.grupo_asignaturas.mostrar_info()
                linea()
            elif opcion == "6":
                linea()
                self.modificar_asignatura()
                linea()
            elif opcion == "7":
                linea()
                self.mostrar_info_completa()
                linea()
            elif opcion == "8":
                linea()
                self.guardar_info_completa()
                linea()
            elif opcion == "9":
                linea()
                print("Bye Bye...")
                linea()
                break
            else :
                print ("Opción inválida, introduce un número entre 1 y 9. ")
    def añadir_estudiante(self):
        nombre = input ("Introduce el nombre del estudiante. \n")
        while nombre == "":
            nombre = input ("Introduce un nombre válido. \n")
        notas = []
        nota = input ("Introduce cada nota del estudiante : \n")
        while 0 <= int (nota) <= 10:
            notas.append(int(nota))
            nota = input ("Introduce cada nota del estudiante : \n")
        genero = input ("Introduce el género del estudiante. (Femenino, Masculino) ")
        while genero not in ["Femenino","Masculino"]:
            genero = input ("Introduce un género válido. ")
        estudiante_nuevo = Estudiante (nombre,notas,genero)
        self.grupo_estudiantes.añadir_estudiante(estudiante_nuevo)
        print(f"Estudiante {nombre} añadido.")

    def añadir_asignatura(self):
        nombre = input ("Introduce el nombre de la asignatura. \n")
        while nombre == "":
            nombre = input ("Introduce un nombre válido. \n")
        horario = input ("Introduce un horario válido. \n")
        while horario == "":
            horario = input ("Introduce un horario válido. ")
        profesor = input (f"Introduce el nombre del profesor de la asignatura [{nombre}] : \n")
        while profesor == "":
            profesor = input ("Introduce un profesor válido. ")
        asignatura_nueva = Asignaturas (nombre,horario,profesor)
        self.grupo_asignaturas.añadir_asignaturas(asignatura_nueva)

    def modificar_asignatura(self):
        self.grupo_asignaturas.mostrar_info()
        index = int(input("Introduce el número de la asignatura que quieres modificar : \n"))
        self.grupo_asignaturas.cambiar_algo(index)

def guardar_en_fichero(nombre_fichero, texto):
    with open(nombre_fichero, "a") as f:
        f.write(texto + "\n")

def linea():
    print ("-" * 40)

def main():
    sistema = SistemaCompleto()
    sistema.menu()
main()
