# Prueba de manipulación de ficheros, con un ejercicio similar al del examen.
# Tenemos un caso de unos establecimientos con una información similar a esta.
# Azul#Panadería#Valencia#3.5
# Donde tenemos Nombre#TipoTienda#Localidad#Importe.


class Establecimiento:
    def __init__(self, nombre, localidad):
        self.nombre = nombre
        self.localidad = localidad
        self.total_ventas = 0.0
        self.operaciones = 0

    def añadir_venta(self, importe):
        # Añadimos al total el importe y sumamos una operación.
        self.total_ventas += importe
        self.operaciones += 1

def cargar_establecimientos(nombre_fichero):
    # Leemos la information del fichero y añadimos la venta si tiene.
    lista_establecimientos = []
    fichero = open(nombre_fichero)
    for linea in fichero:
        nombre, tipo_tienda, localidad, importe = linea.strip().split("#")
        importe = float(importe)
        encontrado = False
        for est in lista_establecimientos:
            if est.nombre == nombre:
                est.añadir_venta(importe)
                encontrado = True
                break
        if not encontrado:
            nuevo_est = Establecimiento(nombre,localidad)
            nuevo_est.añadir_venta(importe)
            lista_establecimientos.append(nuevo_est)
    fichero.close()
    return lista_establecimientos

def establecimientos_con_muchas_ventas(lista_est, localidad, minimo):
    # Si un establecimiento de una ciudad x cumple los mínimos de ventas (cantidad importe) se añade a la lista de resultados)
    resultado = []
    for est in lista_est:
        if est.localidad == localidad and est.total_ventas >= minimo:
                resultado.append (est.nombre)
    return resultado