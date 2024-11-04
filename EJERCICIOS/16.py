#Ejercicio 16: Crear una Función para Evaluar un Número y Realizar una Operación

# fn(n): si n <= 15 => 15 - n; (15 - n) * 2
def diferencia(n):
    """
    Calcula la diferencia del valor pasado como argumento.
    Se deben seguir dos reglas.
    """
    if n <= 15:
        return 15 - n
    else:
        return (15 - n) * 2
    
    
print (diferencia (17) )
print(diferencia (3))






