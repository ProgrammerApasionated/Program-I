# Esta parte sirve para determinar rachas de condiciones.

def racha_pasos(lista_dias, umbral):
    """
    Calcula la racha más larga de días consecutivos en los que
    se superan los pasos indicados por el umbral.
    Devuelve: (longitud_racha, fecha_inicio, fecha_fin)
    """
    racha_actual = 0
    max_racha = 0
    inicio_actual = None
    inicio_max = None
    fin_max = None
    dia_anterior = None
    for dia in lista_dias:
        if dia["pasos"] > umbral:
            if racha_actual == 0:
                inicio_actual = dia["fecha"]
            racha_actual += 1
        else:
            if racha_actual > max_racha:
                max_racha = racha_actual
                inicio_max = inicio_actual
                fin_max = dia_anterior
            racha_actual = 0
            inicio_actual = None
        dia_anterior = dia["fecha"]
    if racha_actual > max_racha:
        max_racha = racha_actual
        inicio_max = inicio_actual
        fin_max = dia_anterior
    return max_racha, inicio_max, fin_max

def racha_sueño(lista_dias, umbral):
    """
    Función que calcula la racha más larga de días consecutivos
    en los que se superan las horas de sueño indicadas por el umbral.
    Devuelve la longitud de la racha y las fechas de inicio y fin.
    """
    racha_actual = 0
    max_racha = 0
    inicio_actual = None
    inicio_max = None
    fin_max = None
    dia_anterior = None
    for horas in lista_dias:
        if horas["sueño"] > umbral:
            if racha_actual == 0:
                inicio_actual = horas["fecha"]
            racha_actual += 1
        else:
            if racha_actual > max_racha:
                max_racha = racha_actual
                inicio_max = inicio_actual
                fin_max = dia_anterior
            racha_actual = 0
            inicio_actual = None
        dia_anterior = horas["fecha"]
    if racha_actual > max_racha:
        max_racha = racha_actual
        inicio_max = inicio_actual
        fin_max = dia_anterior
    return max_racha, inicio_max, fin_max

def racha_calorias_bajas(lista_dias, umbral):
    """
    Función que calcula la racha más larga de días consecutivos
    en los que las calorías ingeridas son menores que el umbral.
    Devuelve la longitud de la racha y las fechas de inicio y fin.
    """
    racha_actual = 0
    max_racha = 0
    inicio_actual = None
    inicio_max = None
    fin_max = None
    dia_anterior = None
    for calorias in lista_dias:
        if calorias["calorias"] < umbral:
            if racha_actual == 0:
                inicio_actual = calorias["fecha"]
            racha_actual += 1
        else:
            if racha_actual > max_racha:
                max_racha = racha_actual
                inicio_max = inicio_actual
                fin_max = dia_anterior
            racha_actual = 0
            inicio_actual = None
        dia_anterior = calorias["fecha"]
    if racha_actual > max_racha:
        max_racha = racha_actual
        inicio_max = inicio_actual
        fin_max = dia_anterior
    return max_racha, inicio_max, fin_max

def racha_distancia(lista_dias, umbral):
    """
    Función que calcula la racha más larga de días consecutivos
    en los que se supera la distancia indicada por el umbral.
    Devuelve la longitud de la racha y las fechas de inicio y fin.
    """
    racha_actual = 0
    racha_max    = 0
    inicio_actual = None
    inicio_max   = None
    fin_max      = None
    dia_anterior = None
    for dia in lista_dias:
        if dia["distancia"] > umbral:
            if racha_actual == 0:
                inicio_actual = dia["fecha"]
            racha_actual += 1
        else :
            if racha_max < racha_actual:
                racha_max = racha_actual
                inicio_max = inicio_actual
                fin_max = dia_anterior
            racha_actual = 0
            inicio_actual = None
        dia_anterior = dia["fecha"]
    if racha_max < racha_actual:
        racha_max = racha_actual
        inicio_max = inicio_actual
        fin_max = dia_anterior
    return racha_max, inicio_max, fin_max