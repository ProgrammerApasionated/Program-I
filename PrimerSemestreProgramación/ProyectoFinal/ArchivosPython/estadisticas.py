# Sacamos estadísticas a partir de los datos leídos en lector.py.

def total_pasos(lista_dias):
    """
    Función que devuelve la suma total de pasos.
    Con los datos de la lista de diccionarios de antes.
    """
    total_p = 0
    for dia in lista_dias:
        total_p += dia["pasos"]
    return total_p

def media_dormida(lista_dias):
    """
    Función que devuelve la media de horas dormidas.
    Con los datos de la lista de diccionarios de antes.
    """
    total_dorm = 0
    for dia in lista_dias:
        total_dorm += dia["sueño"]
    media = total_dorm / len(lista_dias)
    return media

def dia_mas_calorias(lista_dias):
    """
    Función que devuelve el día con más calorías.
    Con los datos de la lista de diccionarios de antes.
    """
    max_cal = None
    dicc_max = {}
    for dia in lista_dias:
        if max_cal is None or max_cal < dia["calorias"]:
            max_cal = dia["calorias"]
            dicc_max = dia
    return dicc_max

def dia_mas_distancia(lista_dias):
    """
    Función que devuelve el día con más distancia.
    Con los datos de la lista de diccionarios de antes.
    """
    max_distan = None
    dicc_max = {}
    for dia in lista_dias:
        if max_distan is None or max_distan < dia["distancia"]:
            max_distan = dia["distancia"]
            dicc_max = dia
    return dicc_max

def porcentaje_dias_activo(lista_dias, umbral):
    """
    Función que devuelve el porcentaje de días que cumple los pasos del umbral.
    Con los datos de la lista de diccionarios de antes.
    """
    dias_buenos = 0
    for dia in lista_dias:
        if dia["pasos"] > umbral:
            dias_buenos += 1
    porcentaje = (dias_buenos / len(lista_dias)) * 100
    return porcentaje

def clasificar_dia(dia):
    """
    Función que devuelve la calidad del día dependiendo del sueño y pasos.
    Con los datos de la lista de diccionarios de antes.
    Buen día -> + 8000 pasos + 8 horas sueño.
    Regular  -> + 5000 pasos + 7 horas sueño.
    Malo     -> - 5000 pasos - 7 horas sueño.
    """
    pasos = dia["pasos"]
    sueño = dia["sueño"]
    if pasos > 8000 and sueño > 8.0:
        tipo_dia = "Buen día"
    elif pasos >= 5000 and sueño >= 7.0:
        tipo_dia = "Día regular"
    else:
        tipo_dia = "Día malo"
    return tipo_dia

def resumen_clasificación(lista_dias):
    """
    Función que devuelve la calidad de todos los días que hay en el diccionario.
    Con los datos de la lista de diccionarios de antes.
    """
    cant_dias_buenos = 0
    cant_dias_regulares = 0
    cant_dias_malos = 0
    lista_tipo_dias = []
    for dia in lista_dias:
        categoria = clasificar_dia(dia)
        if categoria == "Buen día":
            cant_dias_buenos += 1
        elif categoria == "Día regular":
            cant_dias_regulares += 1
        else:
            cant_dias_malos += 1
    lista_tipo_dias.append(f"Buenos: {cant_dias_buenos}")
    lista_tipo_dias.append(f"Regulares: {cant_dias_regulares}")
    lista_tipo_dias.append(f"Malos: {cant_dias_malos}")
    return lista_tipo_dias
