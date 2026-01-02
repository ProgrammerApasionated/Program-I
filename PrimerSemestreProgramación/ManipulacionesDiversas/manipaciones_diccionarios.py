# Ejercicio de práctica con diccionarios.
# Buscamos que el usuario diga los valores que quiera introducir y el valor que está ligado a él.

def conseguir_dict():
    mi_diccionario = {}
    clave = input ("Introduce la clave \n ")
    valor = input ("Introduce el valor que tiene la clave \n")
    while clave != "" and valor != "":
        if valor.isdigit():
            valor = int(valor)
        else:
            try:
                valor = float(valor)
            except ValueError:
                pass
        if clave in mi_diccionario:
            mi_diccionario[clave].append(valor)
        else:
            mi_diccionario[clave] = [valor]
        clave = input("Introduce la clave \n ")
        valor = input("Introduce el valor que tiene la clave \n")
    return mi_diccionario
# Obtenemos el diccionario sin sobreescribir un valor, pero añadiendo la clave aunque esté repetida.
def valores_extremos(diccionario):
    if not diccionario:
        print("No hay valores")
        return
    max_val = None
    min_val = None
    clave_max = clave_min = None
    for clave, lista in diccionario.items():
        actual_max = max(lista)
        actual_min = min(lista)
        if max_val is None or actual_max > max_val:
            max_val = actual_max
            clave_max = clave
        if min_val is None or actual_min < min_val:
            min_val = actual_min
            clave_min = clave
    print(f"Valor máximo: {max_val} (clave: {clave_max})")
    print(f"Valor mínimo: {min_val} (clave: {clave_min})")
# Mediante el diccionario sacamos el valor máximo o mínimo y enseñando su clave.
def mostrar_dict(el_diccionario):
    if not el_diccionario:
        print("El diccionario está vacío")
        return
    for clave, valor in el_diccionario.items():
        print(f"La clave '{clave}' tiene el valor: {valor}")
# Recorremos el diccionario y lo mostramos.
def sacar_media (un_dict, clave):
    if not un_dict:
        print ("El diccionario no tiene elementos.")
        return
    if clave not in un_dict:
        print (f"La clave {clave} no está en el diccionario.")
    valores = un_dict[clave]
    if not isinstance(valores, list):
        valores = [valores]
    media = sum(valores)/ len(valores)
    media = round(media,2)
    print (f"La media de la clave {clave} es {media}")
# Sacamos la media con una clave concreta, si no está salta un error.
sacar_media(conseguir_dict(),"Azul")