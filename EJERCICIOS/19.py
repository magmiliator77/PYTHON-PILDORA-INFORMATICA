#Ejercicio 19: Comprobar si una Cadena de Caracteres Termina con la Extensión .py

#main.py
#modulo => modulo.py

def validar_nombre_archivo (nombre_archivo):
    """
    Valida si un nombre de archivo tiene la extensión .py.
    Si el archivo no tiene la extensión, la agrega.
    """     

    if len (nombre_archivo) >= 3 and nombre_archivo[-3:] == '-py':
        return nombre_archivo

    return nombre_archivo + '-py'



print(validar_nombre_archivo('main-py' ))
print(validar_nombre_archivo('modulo'))
print(validar_nombre_archivo('test-py'))




