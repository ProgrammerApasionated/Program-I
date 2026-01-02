# Programa que hace calculos con un ejercicio inventado.
# Ejercicio de calculos relacionados con la cantidad de lluvia de un sitio.

def obtener_lluvias():
    lista_lluvias = []
    cadena = input ("Introduce la cantidad de lluvia en (mm) (Cadena vacía para acabar) : \n")
    while cadena != "" :
        lista_lluvias.append(int(cadena))
        cadena = input ("Introduce la cantidad de lluvia en (mm) (Cadena vacía para acabar) : \n")
    return lista_lluvias

def lluvia_maxima(lista_lluvias):
    max_lluvias = lista_lluvias[0]
    for maximo in lista_lluvias :
        if maximo > max_lluvias :
            max_lluvias = maximo
    print (f"El máximo de lluvias ha sido de {max_lluvias} mm.")
    return max_lluvias

def lluvias_minimas(lista_lluvias):
    min_lluvias = lista_lluvias [0]
    for minimo in lista_lluvias:
        if minimo < min_lluvias:
            min_lluvias = minimo
    print (f"El mínimo de lluvias ha sido de {min_lluvias} mm.")
    return min_lluvias

def dias_sin_lluvia(lista_lluvias):
    cantidad_dias = 0
    for cantidad in lista_lluvias:
        if cantidad == 0:
            cantidad_dias += 1
    print (f"Lleva {cantidad_dias} dias sin llover.")
    return cantidad_dias

def racha_de_lluvias(lista_lluvias):
    inicio = -1
    longitud = 0
    mayor_inicio = -1
    mayor_longitud = 0
    mayor_final = -1
    i = 0
    while i < len(lista_lluvias):
        if lista_lluvias[i] > 0:
            if longitud == 0:
                inicio = i
            longitud += 1
        else:
            if longitud > mayor_longitud:
                mayor_longitud = longitud
                mayor_inicio = inicio
                mayor_final = i - 1
            longitud = 0
        i += 1
    if longitud > mayor_longitud:
        mayor_longitud = longitud
        mayor_inicio = inicio
        mayor_final = i - 1
    print(f"La racha de lluvias mayor ha sido de {mayor_longitud} dias \n")
    print(f"Ha empezado del dia {mayor_inicio} al dia {mayor_final} \n")
    return mayor_longitud, mayor_inicio, mayor_final
def opciones():
    print ("1.- Cantidad de días sin llover")
    print ("2.- Calcular las lluvias máxima.")
    print ("3.- Obtener las lluvias mínimas")
    print ("4.- Obtener la racha de días con lluvia.")
def main():
    lista_lluvias = obtener_lluvias()
    opciones()
    opcion = input ("Elige la opción deseada (Del 1 al 4, otro número para salir) \n")
    while opcion.isdigit() and 1 <= int(opcion) <= 4:
        opcion = int(opcion)
        if opcion == 1 :
            print ("-" * 40)
            print (f"[Opción] = 1 -> [Diás sin lluvia]")
            dias_sin_lluvia(lista_lluvias)
            print ("-" * 40)
        elif opcion == 2 :
            print ("-" * 40)
            print (f"[Opción] = 2 -> [Lluvias máximas]")
            lluvia_maxima(lista_lluvias)
            print ("-" * 40)
        elif opcion == 3 :
            print ("-" * 40)
            lluvias_minimas(lista_lluvias)
            print ("-" * 40)
        elif opcion == 4 :
            print ("-" * 40)
            print (f"[Opción] = 4 -> [Racha de lluvias]")
            racha_de_lluvias(lista_lluvias)
            print ("-" * 40)
        opciones()
        print ("-" * 40)
        opcion = input("Elige la opción deseada (Del 1 al 4, otro número para salir) \n")
    print ("Saliendo del programa...")
main()
