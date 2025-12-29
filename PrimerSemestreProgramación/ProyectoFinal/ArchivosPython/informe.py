from estadisticas import *
from rachas import *

def generar_informe(lista_dias):
    """
    Genera un informe completo con estadísticas generales, días destacados,
    clasificación emocional y rachas significativas.
    Devuelve un string con el informe formateado.
    """
    informe = ""
    informe += "=============================================\n"
    informe += "        INFORME DE VIDA — RESUMEN DIARIO     \n"
    informe += "=============================================\n\n"
    total = total_pasos(lista_dias)
    media = media_dormida(lista_dias)
    informe += "📊 ESTADÍSTICAS GENERALES\n"
    informe += "---------------------------------------------\n"
    informe += f"• Pasos acumulados: {total}\n"
    informe += f"• Media de horas dormidas: {media:.2f}\n"
    informe += "\n"
    dia_cal = dia_mas_calorias(lista_dias)
    dia_dist = dia_mas_distancia(lista_dias)
    informe += "🌟 DÍAS DESTACADOS\n"
    informe += "---------------------------------------------\n"
    informe += f"• Día más exigente (calorías): {dia_cal['fecha']} — {dia_cal['calorias']} kcal\n"
    informe += f"• Día más activo (distancia): {dia_dist['fecha']} — {dia_dist['distancia']} km\n"
    informe += "\n"
    clasificacion = resumen_clasificación(lista_dias)
    informe += "🎨 CLASIFICACIÓN DE DÍAS\n"
    informe += "---------------------------------------------\n"
    informe += f"• {clasificacion[0]}\n"
    informe += f"• {clasificacion[1]}\n"
    informe += f"• {clasificacion[2]}\n"
    informe += "\n"
    informe += "🔥 RACHAS — CONSTANCIA Y MOMENTUM\n"
    informe += "---------------------------------------------\n"
    racha, inicio, fin = racha_pasos(lista_dias, 8000)
    informe += f"• Pasos (>8000): {racha} días seguidos (de {inicio} a {fin})\n"
    rach, inci, fi = racha_sueño(lista_dias, 7)
    informe += f"• Sueño (>7h): {rach} días seguidos (de {inci} a {fi})\n"
    rcal, ical, fcal = racha_calorias_bajas(lista_dias, 2000)
    informe += f"• Calorías bajas (<2000): {rcal} días seguidos (de {ical} a {fcal})\n"
    rdis, idis, fdis = racha_distancia(lista_dias, 5)
    informe += f"• Distancia (>5km): {rdis} días seguidos (de {idis} a {fdis})\n"
    informe += "\n"
    informe += "=============================================\n"
    informe += "   Este informe no solo muestra números.\n"
    informe += "   Muestra constancia, hábitos y evolución.\n"
    informe += "   Cada día registrado es un paso más hacia\n"
    informe += "   una versión más consciente y disciplinada.\n"
    informe += "=============================================\n"
    return informe
