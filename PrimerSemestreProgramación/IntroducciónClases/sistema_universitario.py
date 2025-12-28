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
            print (f"El nombre de la asignatura es {self.nombre}. \n")
        elif opc == "h":
            print (f"Los horarios de la asignatura {self.nombre} son {self.horario}. \n")
        else:
            print (f"El nombre del profesor que da la asignatura {self.nombre} es {self.profesor}. \n")

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
    def __init__(self,nombre,notas,genero):
        self.nombre = nombre
        self.notas  = notas
        self.genero = genero

    def __str__(self):
        return f"El estudiante con nombre {self.nombre}, con notas {self.notas} y género {self.genero}."

    def posibilidad_cambios(self):
        print ("N/n    -> Nombre. ")
        print ("No/no  -> Notas.  ")
        print ("G/g    -> Género. ")

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
        buscar = input("Introduce característica a buscar: ")
        buscar = buscar.lower()
        while buscar not in ["n", "no", "g"]:
            buscar = input("Introduce una opción válida (n,no,g) \n")
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
            nota = input("Introduce notas una a una (otra cosa para terminar): ")
            while nota.isdigit() and 0 <= int(nota) <= 10:
                notas.append(int(nota))
                nota = input("Introduce otra nota (o algo distinto para terminar): ")
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
            print("No se ha encontrado ningún estudiante.")

class GrupoAsignaturas:
    def __init__(self):
        self.asignaturas = []

    def añadir_asignaturas (self,asignatura):
        self.asignaturas.append(asignatura)

    def mostrar_info(self):
        for asignatura in self.asignaturas:
            print(asignatura)

    def cambiar_algo(self,index):
        if 1 <= index <= len(self.asignaturas):
            self.asignaturas[index - 1].cambiar_info_concreta()
        else:
            print ("Indice no válido.")

class SistemaCompleto:
    def __init__(self):
        self.grupo_estudiantes = GrupoEstudiantes()
        self.grupo_asignaturas = GrupoAsignaturas()

    def menu(self):
        while True:
            print("----------MENÚ SISTEMA----------")
            print("1.-Añadir estudiante.")
            print("2.-Mostrar estudiantes.")
            print("3.-Buscar estudiantes.")
            print("4.-Añadir asignatura.")
            print("5.-Mostrar asignaturas.")
            print("6.-Modificar asignatura.")
            print("7.-Salir.")
            print("--------------------------------")
            opcion = input("Introduce la opción deseada: ")
            if opcion == "1":
                self.añadir_estudiante()
            elif opcion == "2":
                self.grupo_estudiantes.mostrar_info()
            elif opcion == "3":
                self.grupo_estudiantes.buscar_estudiante()
            elif opcion == "4":
                self.añadir_asignatura()
            elif opcion == "5":
                self.grupo_asignaturas.mostrar_info()
            elif opcion == "6":
                self.modificar_asignatura()
            elif opcion == "7":
                print("Bye Bye...")
                break
            else:
                print("Opción inválida. Introduce un número entre 1 y 7.")
    def añadir_estudiante(self):
        nombre = input ("Introduce el nombre del estudiante. \n")
        while nombre == "":
            nombre = input ("Introduce un nombre válido. ")
        notas = []
        nota = input ("Introduce cada nota del estudiante. ")
        while 0 <= int (nota) <= 10:
            notas.append(nota)
            nota = input ("Introduce cada nota del estudiante. ")
        genero = input ("Introduce el género del estudiante. (Femenino, Masculino) ")
        while genero not in ["Femenino","Masculino"]:
            genero = input ("Introduce un género válido. ")
        estudiante_nuevo = Estudiante (nombre,notas,genero)
        self.grupo_estudiantes.añadir_estudiante(estudiante_nuevo)
        print(f"Estudiante {nombre} añadido.")
    def añadir_asignatura(self):
        nombre = input ("Introduce el nombre de la asignatura. \n")
        while nombre == "":
            nombre = input ("Introduce un nombre válido.")
        horario = input ("Introduce un horario válido. \n")
        while horario == "":
            horario = input ("Introduce un horario válido. ")
        profesor = input (f"Introduce el nombre del profesor de la asignatura {nombre}")
        while profesor == "":
            profesor = input ("Introduce un profesor válido. ")
        asignatura_nueva = Asignaturas (nombre,horario,profesor)
        self.grupo_asignaturas.añadir_asignaturas(asignatura_nueva)

    def modificar_asignatura(self):
        self.grupo_asignaturas.mostrar_info()
        index = int(input("Introduce el número de la asignatura que quieres modificar"))
        self.grupo_asignaturas.cambiar_algo(index)





# Creamos un sistema.
sistema = SistemaCompleto()
# Ejemplos de uso de estudiantes.
estudiante1 = Estudiante("Azul Verdez", [8, 7, 9], "Masculino")
estudiante2 = Estudiante("Medana Rojo", [10, 9, 8], "Femenino")
estudiante3 = Estudiante("Perez Dientes", [6, 7, 5], "Masculino")
# Añadimos los estudiantes en el Grupo Estudiantes.
sistema.grupo_estudiantes.añadir_estudiante(estudiante1)
sistema.grupo_estudiantes.añadir_estudiante(estudiante2)
sistema.grupo_estudiantes.añadir_estudiante(estudiante3)
# Ejemplos de uso de asignaturas.
asignatura1 = Asignaturas("Algebra Lineal", "Lunes 10:00-12:00", "Santiago Joker")
asignatura2 = Asignaturas("Informática Básica", "Martes 09:00-11:00", "Azulez Moradez")
asignatura3 = Asignaturas("Oratoria y Debate", "Miércoles 12:00-14:00", "Debate Interesantez")
# Añadimos las asignaturas en el Grupo Asignaturas.
sistema.grupo_asignaturas.añadir_asignaturas(asignatura1)
sistema.grupo_asignaturas.añadir_asignaturas(asignatura2)
sistema.grupo_asignaturas.añadir_asignaturas(asignatura3)
# Iniciamos el programa con el menú.
sistema.menu()