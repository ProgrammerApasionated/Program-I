# Función principal que muestra el menú y todas las funciones.
from lector import leer_fichero
from informe import generar_informe

def main():
    lista_dias = leer_fichero("DatosPropiosReales.txt")
    informe = generar_informe(lista_dias)
    print(informe)

if __name__ == "__main__":
    main()
